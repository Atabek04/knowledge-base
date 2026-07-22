---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [maximumPoolSize]
---

`maximumPoolSize` is the single most important HikariCP parameter — it sets the hard ceiling on how many physical database connections the pool can ever hold (both idle and active combined).

Default: **10**.

When all connections are borrowed and a new request arrives, it waits up to `connectionTimeout` milliseconds before HikariCP throws a `SQLException`.

### Why bigger is not better

More connections ≠ more throughput.
Each connection is a thread on the DB server side.
Too many → context-switch overhead, lock contention, memory pressure.

HikariCP's own sizing formula (from the [pool sizing article](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing)):

```
pool size = (core count × 2) + effective spindle count
```

For a 4-core machine with an SSD: `(4 × 2) + 1 = 9` — close to the default of 10.

### Relationship with minimumIdle

By default `minimumIdle` equals `maximumPoolSize`, making the pool **fixed-size**.
HikariCP recommends keeping this default — a fixed pool avoids the overhead of growing and shrinking under load.

---

### Read more
- [[HikariCP minimumIdle sets the floor for idle connections held in reserve]]
- [[HikariCP connectionTimeout is the max wait before throwing an exception]]
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[Databases - MOC]]
