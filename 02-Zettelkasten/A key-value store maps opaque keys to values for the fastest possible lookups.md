---
aliases: [Key-Value Store, KV Store]
tags: [database, nosql, data-modeling, caching]
created: 2026-05-31
---

### What it is

A **key-value store** is the simplest data model: a giant distributed hash map from a <mark style="background: yellow">unique key to an opaque value</mark>.

Examples: Redis, DynamoDB, etcd. You already know the shape — it's a `HashMap` that survives across processes and machines.

---

### The defining constraint

The store knows **nothing about the value's contents**. It's a blob.

That's the whole bargain: because it never inspects values, lookup by key is **O(1)** and trivially shardable (hash the key → pick a node).

```
GET user:42        → the value
SET user:42 {...}  → store it
```

---

### Strengths

- **Fastest reads/writes** of any model — single-key access, no query planning
- **Trivial horizontal scaling** — keys partition cleanly across nodes
- Ideal for **caching, sessions, rate-limit counters, feature flags**

---

### Weaknesses

- <mark style="background: #f9a8d4">You can only query by key.</mark> No "find all users in London" — the store can't see inside values
- No relationships, no joins, no secondary indexes (unless bolted on)

Best fit: lookups where you **always know the exact key** and need them blazing fast — the canonical cache-aside pattern in front of a relational DB.

---

Read more:
- [[A document database stores self-describing records queried by their nested content]]
- [[A column-family store groups columns into families for wide sparse write-heavy tables]]
- [[Databases - MOC]]
