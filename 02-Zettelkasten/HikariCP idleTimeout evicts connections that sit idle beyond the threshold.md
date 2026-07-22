---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [idleTimeout]
---

`idleTimeout` is how long (in ms) a connection can sit unused in the pool before HikariCP removes it — down to the `minimumIdle` floor.

Default: **600 000 ms (10 minutes)**. Minimum: **10 000 ms**.

### Only relevant in elastic mode

`idleTimeout` only kicks in when `minimumIdle < maximumPoolSize`.
In a fixed-size pool (`minimumIdle = maximumPoolSize`, the default), HikariCP never evicts idle connections — they stay until `maxLifetime` retires them normally.

### What it controls

After a traffic spike, the pool may have grown close to `maximumPoolSize`.
`idleTimeout` is the mechanism that shrinks it back down to `minimumIdle` once load drops.

Set it lower than `maxLifetime` — otherwise `maxLifetime` retires connections before `idleTimeout` gets a chance to evict them, making the setting pointless.

---

### Read more
- [[HikariCP minimumIdle sets the floor for idle connections held in reserve]]
- [[HikariCP maxLifetime recycles connections before the database closes them]]
- [[Databases - MOC]]
