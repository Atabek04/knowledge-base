---
created: 2026-06-23
tags: [databases/postgresql, linux/process]
---

When `max_connections` is set too high, PostgreSQL doesn't just use more RAM — it triggers a CPU death spiral through context-switch thrashing.

![[db_max_connections_meme.jpg]]

### The cascade

```
more connections
  → more OS backend processes
    → more processes competing for the same CPU cores
      → OS scheduler slices CPU time thinner
        → constant save/load of register state, TLB flushes, cache invalidation
          → CPU spends >80% of cycles on switching, <20% on actual query work
```

This is pure **CPU context switching** overhead — not swap memory. Adding RAM lets you hold more processes without OOM, but it makes thrashing *worse* by enabling even more concurrent processes to fight over cores.

### Why more hardware doesn't fix it

| "Fix" | What actually happens |
|-------|-----------------------|
| More RAM | Pool can grow larger → more processes → more thrashing |
| More CPU | Marginally better, but scheduler overhead scales faster than cores |
| Connection pool | Fewer OS processes → less context switching → throughput recovers |

The only real fix is **fewer connections** via a pool. PostgreSQL's own docs cite the formula `(core_count × 2) + spindle_count` as the target for active connections — on a 4-core/SSD machine that's ~9, close to HikariCP's default of 10.

### Thrashing threshold

There's no single number. The knee of the performance curve is typically well below 100 simultaneous *active* connections on most hardware. Idle connections cost RAM but don't cause thrashing — it's the *active* ones competing for CPU that matter.

---

### Read more
- [[PostgreSQL spawns a dedicated OS process for each client connection]]
- [[PostgreSQL max_connections sets the server-side ceiling on simultaneous connections]]
- [[Context switch allows one CPU core to execute multiple processes by rapidly switching between them]]
- [[HikariCP maximumPoolSize caps the total number of live database connections]]
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[PostgreSQL - MOC]]
