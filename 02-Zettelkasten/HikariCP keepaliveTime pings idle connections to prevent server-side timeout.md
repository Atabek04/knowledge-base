---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [keepaliveTime]
---

`keepaliveTime` tells HikariCP how often (in ms) to send a lightweight ping to each idle connection to prove it is still alive.

Default: **120 000 ms (2 minutes)**. Minimum: **30 000 ms**. Must be less than `maxLifetime`.

### Why it exists

Firewalls, NAT devices, and load balancers silently drop TCP connections that carry no traffic for some threshold (often 5–10 minutes).
The DB pool has no idea — it still thinks the connection is healthy.
The next thread to borrow that connection gets a "broken pipe" error.

`keepaliveTime` prevents this by sending a ping (e.g. a `SELECT 1`) before the firewall's idle timer fires.

### keepaliveTime vs maxLifetime

| Concern | Parameter |
|---------|-----------|
| Network device drops idle TCP connection | `keepaliveTime` |
| DB server closes connection after max age | `maxLifetime` |

Both can be needed simultaneously — a connection can survive the DB's lifetime limit but be killed by the firewall before that, or vice versa.

---

### Read more
- [[HikariCP maxLifetime recycles connections before the database closes them]]
- [[Databases - MOC]]
