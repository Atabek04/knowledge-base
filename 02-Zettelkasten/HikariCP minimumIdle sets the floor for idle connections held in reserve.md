---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [minimumIdle]
---

`minimumIdle` controls how many idle connections HikariCP keeps open even when no requests are coming in.

Default: **same as `maximumPoolSize`** — meaning HikariCP defaults to a **fixed-size pool**.

### Fixed vs elastic pool

| Mode | When | Trade-off |
|------|------|-----------|
| Fixed (`minIdle = maxPoolSize`) | Always-on services | Predictable latency, higher idle DB cost |
| Elastic (`minIdle < maxPoolSize`) | Bursty / batch workloads | Saves DB connections at rest, but spikes cause growth latency |

HikariCP explicitly recommends **not changing this** from the default.
The overhead of growing and shrinking a pool under load cancels out any DB-side savings in most web services.

### When elastic makes sense

- Batch jobs that sit idle for long stretches
- Services where the DB charges per open connection (e.g. managed cloud DBs with connection limits)

If you do set `minimumIdle < maximumPoolSize`, also configure `idleTimeout` to control how fast excess idle connections are evicted.

---

### Read more
- [[HikariCP maximumPoolSize caps the total number of live database connections]]
- [[HikariCP idleTimeout evicts connections that sit idle beyond the threshold]]
- [[Databases - MOC]]
