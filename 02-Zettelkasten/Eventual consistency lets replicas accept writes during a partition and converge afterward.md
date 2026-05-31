---
aliases: [Eventual Consistency]
tags: [distributed-systems, database, consistency, architecture]
created: 2026-05-31
---

### What it is

**Eventual consistency** is the guarantee that, if no new writes arrive, all replicas will <mark style="background: yellow">eventually converge to the same value</mark> — but a read in the meantime may return stale data.

It is the consistency model an **AP** system adopts after choosing availability under the [[CAP theorem forces a partitioned system to choose between consistency and availability|CAP]] trade-off.

---

### Why you'd accept staleness

To stay **available** during a network partition, replicas must accept writes without coordinating first.

That means two replicas can briefly hold different values for the same key. The system propagates updates in the background and resolves conflicts (last-write-wins, vector clocks, CRDTs) until they agree.

```
write to replica A ──► A: v2,  B: v1   (briefly divergent)
        ...propagate...
                      ──► A: v2,  B: v2   (converged)
```

---

### Strong vs eventual

| | Strong consistency | Eventual consistency |
|--|--|--|
| **Read after write** | Always sees the write | May see the old value for a while |
| **Availability under partition** | Lower (must coordinate) | Higher (answer locally) |
| **Fits** | Balances, bookings, ledgers | Likes counts, feeds, catalogs, DNS |

---

### When it's the right call

Eventual consistency is fine when a **brief stale read causes no harm** — a view count, a social feed, a cache.

<mark style="background: #f9a8d4">It is wrong where staleness corrupts a decision</mark> — never let a payment or inventory-reservation read stale data. This is the same reasoning behind keeping cross-aggregate updates eventually consistent while protecting invariants *inside* one [[An aggregate is a cluster of objects treated as one consistency boundary|aggregate]].

---

Read more:
- [[CAP theorem forces a partitioned system to choose between consistency and availability]]
- [[An aggregate is a cluster of objects treated as one consistency boundary]]
- [[Distributed Systems - MOC]]
