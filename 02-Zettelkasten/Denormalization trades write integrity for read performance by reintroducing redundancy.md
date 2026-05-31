---
aliases: [Denormalization]
tags: [database, data-modeling, performance, normalization, olap]
created: 2026-05-31
---

### What is denormalization?

**Denormalization** is the deliberate reintroduction of redundancy into a normalized schema to make <mark style="background: yellow">reads faster</mark>.

It is not "failing to normalize." It is normalizing first, then knowingly breaking specific rules where the read cost of JOINs outweighs the write cost of duplication.

---

### Why you'd break the rules

[[Normalization eliminates redundancy to prevent insert update and delete anomalies|Normalization]] spreads one logical record across many tables. Reassembling it needs JOINs, and at scale JOINs get expensive.

Denormalization pre-joins or pre-aggregates the data so a read touches **one place** instead of many.

Common techniques:
- **Duplicating a column** (store `customer_name` on `orders` to avoid joining `customers`)
- **Precomputed aggregates** (store `order_total` instead of summing lines each read)
- **Materialized views** that flatten a join graph

---

### The trade-off you're accepting

| | Normalized | Denormalized |
|--|--|--|
| **Reads** | More JOINs, slower | Fewer JOINs, faster |
| **Writes** | One fact, one place | Same fact in many places |
| **Risk** | Low — no anomalies | <mark style="background: #f9a8d4">Update anomalies — must keep copies in sync</mark> |

You are buying read speed with write complexity. The duplicated data can drift out of sync, so you need a discipline to keep copies consistent.

---

### Where this is the default, not the exception

Analytical (OLAP) systems denormalize aggressively — star schemas, wide flat tables — because they are read-heavy and append-mostly.

This is exactly why analytics often lives in a separate column-oriented store, fed from the normalized OLTP database — see the [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics|dual-write pattern]].

---

Read more:
- [[Normalization eliminates redundancy to prevent insert update and delete anomalies]]
- [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics]]
- [[ClickHouse - MOC]]
- [[Databases - MOC]]
