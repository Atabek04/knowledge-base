---
aliases: [Column-Family Store, Wide-Column Store, Column-Family]
tags: [database, nosql, data-modeling]
created: 2026-05-31
---

### What it is

A **column-family store** (wide-column store) organizes data by <mark style="background: yellow">rows that can each hold different columns</mark>, grouped into "column families" and stored physically by column group.

Examples: Apache Cassandra, HBase, Google Bigtable.

> ⚠️ Don't confuse this with a **column-oriented OLAP** store like [[ClickHouse - MOC|ClickHouse]]. Both store by column, but wide-column NoSQL targets huge write-heavy OLTP-style workloads, while OLAP columnar stores target analytical scans.

---

### The model

Picture a table where every row can have a **different set of columns**, and millions of columns are possible per row:

```
row "user:42"  → { name: "Ali", email: "...", login:2026-05-01: "ok", ... }
row "user:99"  → { name: "Sara", phone: "..." }
```

Rows are sparse — a missing column costs nothing. This suits data that is **wide and irregular**.

---

### Strengths

- **Massive write throughput** — append-optimized, distributes across many nodes
- **Sparse data is free** — no NULL columns wasted on absent fields
- **Linear horizontal scale** — built for clusters from day one

---

### Weaknesses

- <mark style="background: #f9a8d4">Query patterns must be designed up front</mark> — you model tables around the queries you'll run, not around the entities
- Weak ad-hoc querying and joins; eventual consistency is common

Best fit: time-series, event logging, IoT, messaging — **high-volume writes** with known access patterns.

---

Read more:
- [[A key-value store maps opaque keys to values for the fastest possible lookups]]
- [[A graph database makes relationships first-class for traversal-heavy queries]]
- [[Databases - MOC]]
