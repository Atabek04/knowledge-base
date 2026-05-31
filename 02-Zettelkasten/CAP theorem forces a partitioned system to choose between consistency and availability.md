---
aliases: [CAP Theorem, CAP, CP, AP]
tags: [distributed-systems, database, consistency, architecture]
created: 2026-05-31
---

### The three properties

The **CAP theorem** describes a distributed data store in terms of three properties:

- **C — Consistency**: every read sees the most recent write (one agreed-upon value)
- **A — Availability**: every request gets a non-error response
- **P — Partition tolerance**: the system keeps working when the network drops messages between nodes

---

### The real statement (not "pick 2 of 3")

The popular "pick any 2" framing is misleading. In any real distributed system, <mark style="background: yellow">network partitions *will* happen — P is not optional.</mark>

So the actual choice is: **when a partition occurs, do you sacrifice C or A?**

```
Partition happens
   ├── keep Consistency → reject/block requests on the cut-off side  → CP
   └── keep Availability → answer with possibly-stale data           → AP
```

---

### CP vs AP

| | Sacrifices | Behavior under partition | Example |
|--|--|--|--|
| **CP** | Availability | Refuse or block to avoid serving stale data | A bank ledger, etcd, ZooKeeper |
| **AP** | Consistency | Answer anyway, reconcile later | A shopping cart, DNS, Cassandra |

<mark style="background: #f9a8d4">Neither is "better"</mark> — a payment system must be CP (wrong balance is unacceptable); a product catalog can be AP (a slightly stale price is fine).

---

### Where the AP path leads

Choosing A under partition means replicas temporarily disagree, then reconcile. That reconciliation model is [[Eventual consistency lets replicas accept writes during a partition and converge afterward|eventual consistency]].

> When there's **no** partition, a system can offer *both* low latency and consistency — the **PACELC** extension captures this: *if Partition then C-or-A, Else Latency-or-Consistency.*

---

Read more:
- [[Eventual consistency lets replicas accept writes during a partition and converge afterward]]
- [[Choosing a database means matching its model and guarantees to non-functional requirements]]
- [[Distributed Systems - MOC]]
