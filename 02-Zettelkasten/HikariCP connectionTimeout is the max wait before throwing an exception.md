---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [connectionTimeout]
---

`connectionTimeout` is how long (in ms) a caller blocks waiting for HikariCP to hand it a connection from the pool before giving up and throwing a `SQLException`.

Default: **30 000 ms (30 seconds)**. Minimum allowed: **250 ms**.

### What it guards against

When the pool is exhausted (all `maximumPoolSize` connections are in use), new requests queue here.
A long `connectionTimeout` masks pool exhaustion — requests pile up silently for 30 s before failing.

In production, set it much lower (e.g. **5 000 ms**) so callers fail fast and circuit breakers / retries can react promptly.

### Not the same as network timeout

`connectionTimeout` is the wait-in-queue time — it does not control how long a TCP handshake to the DB server is allowed to take.
Network-level timeouts are configured on the JDBC driver (e.g. `socketTimeout` on the JDBC URL).

---

### Read more
- [[HikariCP maximumPoolSize caps the total number of live database connections]]
- [[Databases - MOC]]
