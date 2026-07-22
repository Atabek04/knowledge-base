TARGET DECK: Tech-KB::Databases::Connection Pooling
Tags: databases hikaricp connection-pool
**Related:** [[Databases - MOC]]

START
Coding Questions
What does `maximumPoolSize` control in HikariCP, and what is its default?
Back: **Caps** the total number of physical DB connections (idle + active) the pool can ever hold.
Default: **10**
END

START
Coding Questions
What happens when a HikariCP pool is exhausted and a new request arrives?
Back: Request **blocks** and waits up to `connectionTimeout` ms.
If no connection is freed in time → **`SQLException`** is thrown.
END

START
Coding Questions
Why does a larger `maximumPoolSize` not always mean better throughput?
Back: Each connection = a dedicated **OS process** on the PostgreSQL server (~5–10 MB RAM).
Too many processes → context-switch overhead, lock contention, memory pressure.
More connections ≠ more throughput.
END

START
Coding Questions
What is the HikariCP pool sizing formula?
Back: `pool size = (core count × 2) + effective spindle count`
Example: 4-core machine + SSD → `(4 × 2) + 1 = 9`
END

START
Coding Questions
What does `minimumIdle` control in HikariCP, and what is its default?
Back: **Sets the floor** — minimum number of idle connections kept open at all times.
Default: **same as `maximumPoolSize`** → fixed-size pool.
END

START
Coding Questions
What is the difference between a fixed-size and elastic HikariCP pool?
Back:
- **Fixed** (`minIdle = maxPoolSize`): pool size never changes — predictable latency, always holds connections open
- **Elastic** (`minIdle < maxPoolSize`): pool shrinks at rest, grows under load — saves DB connections but adds growth latency on spikes

HikariCP recommends **fixed** for most web services.
END

START
Coding Questions
When does `idleTimeout` become relevant in HikariCP?
Back: Only when `minimumIdle < maximumPoolSize` (elastic pool).
In a **fixed-size pool** (`minimumIdle = maximumPoolSize`) `idleTimeout` has no effect — connections stay until `maxLifetime` retires them.
END

START
Coding Questions
What does `connectionTimeout` control in HikariCP, and what is its default?
Back: **Max time a caller blocks** waiting for a connection from the pool before HikariCP throws `SQLException`.
Default: **30 000 ms (30 s)**. Minimum: 250 ms.
END

START
Coding Questions
How does `connectionTimeout` differ from a JDBC network/socket timeout?
Back:
- `connectionTimeout` → **wait-in-queue** time when the pool is exhausted
- **Socket timeout** → how long the TCP handshake to the DB server is allowed to take (configured on the JDBC URL/driver)

They guard different failure modes.
END

START
Coding Questions
What does `maxLifetime` control in HikariCP, and why should it be shorter than the DB's own idle timeout?
Back: **Recycles** connections that have reached a maximum age (default: **30 min**).

Set it **shorter than the DB's idle timeout** so HikariCP retires the connection first — before the DB silently closes it and causes a "connection closed" error on the next query.
END

START
Coding Questions
What is staggered retirement in HikariCP's `maxLifetime`?
Back: HikariCP adds a **small random offset** to each connection's retirement time so all connections don't expire simultaneously — avoiding a thundering-herd of reconnects under load.
END

START
Coding Questions
What does `idleTimeout` control in HikariCP?
Back: **Evicts** connections that have been idle longer than the threshold (default: **10 min**), shrinking the pool back down toward `minimumIdle` after a traffic spike.
END

START
Coding Questions
What does `keepaliveTime` control in HikariCP?
Back: **Frequency of keepalive pings** sent to idle connections (default: **2 min**).
HikariCP sends a lightweight query (e.g. `SELECT 1`) to prove the connection is still alive before the firewall/NAT device drops it.
END

START
Coding Questions
What problem does `keepaliveTime` solve that `maxLifetime` does not?
Back:
- `keepaliveTime` → prevents **firewalls/NAT devices** from silently dropping idle TCP connections
- `maxLifetime` → prevents the **DB server** from closing aged connections

A connection can be killed by either; both params can be needed at the same time.
END

START
Coding Questions
What does `leakDetectionThreshold` control in HikariCP?
Back: **Time a borrowed connection can stay out** of the pool before HikariCP logs a warning that it may have been leaked.
Default: **0 (disabled)**. Minimum to enable: 2 000 ms.
END

START
Coding Questions
What does HikariCP log when `leakDetectionThreshold` is exceeded?
Back: A **WARN** with the **stack trace of the borrowing thread** — pinpointing exactly where in the code the connection was taken and not returned.
END

START
Coding Questions
What are the two most common causes of a connection leak in HikariCP?
Back:
- `Connection` opened **without `try-with-resources`** → `close()` never called on exception
- A **long-running transaction or query** holds the connection far beyond normal operation time
END

START
Coding Questions
What connection model does PostgreSQL use, and what happens at the OS level on each connect?
Back: **Process-per-connection** — the `postmaster` supervisor **forks a new OS backend process** for every client.
Each backend is a full isolated OS process (not a thread) dedicated to that client for the lifetime of the connection.
END

START
Coding Questions
How much RAM does an idle PostgreSQL connection consume, and where does it come from?
Back: ~**5–10 MB** per idle connection.
Sources:
- Process overhead (stack, OS structures): ~5 MB
- `work_mem` (4 MB default): allocated per sort/hash *operation*, not per connection
- `temp_buffers` (8 MB default): only when the session uses temporary tables
END

START
Coding Questions
Why does PostgreSQL use processes instead of threads for connections?
Back: Two reasons:
- PostgreSQL **predates** the era of mature kernel threading
- Process **isolation** gives hard memory boundaries — a misbehaving backend cannot corrupt another's memory

Downside: fork overhead and per-process RAM cost scale linearly with connection count.
END

START
Coding Questions
What does PostgreSQL's `max_connections` control, and what is its default?
Back: **Server-side ceiling** on total simultaneous client connections across all apps, tools, and admin sessions.
Default: **100**. Requires a **server restart** to change.
END

START
Coding Questions
How does `max_connections` differ from HikariCP's `maximumPoolSize`?
Back:
- `max_connections` → **PostgreSQL server**, caps total connections from *all* sources combined
- `maximumPoolSize` → **HikariCP (app layer)**, caps one application's pool only

Pool size must be well **below** `max_connections`, leaving room for other apps, migration tools, admin sessions.
END

START
Coding Questions
How many connection slots does PostgreSQL reserve for superusers by default, and why?
Back: **3 slots** (`superuser_reserved_connections = 3`).
Ensures admins can always connect to diagnose or fix a server that has reached its connection limit — normal clients fill up to `max_connections - 3` only.
END

START
Coding Questions
What is the cascade from too many PostgreSQL connections to CPU thrashing?
Back:
1. More connections → more OS backend processes
2. More processes compete for the same CPU cores
3. OS scheduler slices CPU time thinner
4. Each switch = register save/restore, TLB flush, cache invalidation
5. CPU spends **>80% of cycles switching**, <20% on actual query work
END

START
Coding Questions
Why does adding more RAM make PostgreSQL connection-count thrashing *worse*?
Back: More RAM prevents OOM → allows **even more processes** to stay resident → more processes fight over CPU cores → more context switching.
RAM enables the pathology; it doesn't cure it.
The fix is **fewer connections** via a pool, not more hardware.
END

START
Coding Questions
Is PostgreSQL connection-count thrashing a CPU or swap memory problem?
Back: **CPU context switching** — not swap.
The OS scheduler must rapidly rotate thousands of processes across a small number of cores.
Swap would add *extra* pain (page faults), but the root cause is scheduler overhead from too many competing OS processes.
END
