---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [maxLifetime]
---

`maxLifetime` sets the maximum age of a connection in the pool (in ms). When a connection reaches this age, HikariCP retires it and opens a fresh one to replace it.

Default: **1 800 000 ms (30 minutes)**. Minimum: **30 000 ms**.

### Why it exists

Databases have their own connection timeout on the server side (e.g. MySQL's `wait_timeout`, PostgreSQL's `idle_in_transaction_session_timeout`).
If the pool holds a connection longer than the DB allows, the DB silently closes it — and the next time a thread borrows it, the query fails with a "connection closed" error.

`maxLifetime` prevents this by proactively cycling connections **before** the DB can terminate them.

**Rule:** always set `maxLifetime` to a value a few minutes **shorter** than the database's own idle connection timeout.

### Staggered retirement

HikariCP adds a small random offset to each connection's retirement time so all connections don't expire simultaneously — avoiding a thundering-herd of reconnects.

---

### Read more
- [[HikariCP idleTimeout evicts connections that sit idle beyond the threshold]]
- [[HikariCP keepaliveTime pings idle connections to prevent server-side timeout]]
- [[Databases - MOC]]
