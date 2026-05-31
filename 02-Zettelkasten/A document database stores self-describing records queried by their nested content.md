---
aliases: [Document Database, Document Store]
tags: [database, nosql, data-modeling]
created: 2026-05-31
---

### What it is

A **document database** stores data as self-describing documents — typically JSON/BSON — where each document <mark style="background: yellow">carries its own structure</mark> and can be queried by its nested fields.

Examples: MongoDB, Couchbase. A document ≈ a row, but it can nest arrays and sub-objects instead of being flat.

---

### Why it's different from a row

A relational row is flat and must match the table schema. A document can hold the whole aggregate in one place:

```json
{ "orderId": 1, "customer": "Ali",
  "lines": [ {"sku":"A","qty":2}, {"sku":"B","qty":1} ] }
```

The order *and* its lines live in one document — no join to reassemble them. This maps naturally to a DDD [[An aggregate is a cluster of objects treated as one consistency boundary|aggregate]].

---

### Strengths

- **Flexible schema** — add a field to one document without migrating others
- **Locality** — read the whole aggregate in one fetch, no joins
- **Developer fit** — the document mirrors the object you already work with

---

### Weaknesses

- **Duplication across documents** — no normalization, so shared facts get copied (an [[Denormalization trades write integrity for read performance by reintroducing redundancy|denormalization]] trade)
- **Weak cross-document joins** — relationships between documents are awkward
- <mark style="background: #f9a8d4">Easy to model badly</mark> — flexibility lets inconsistent shapes accumulate

Best fit: content, catalogs, user profiles, event payloads — data read and written as a **whole unit**.

---

Read more:
- [[A key-value store maps opaque keys to values for the fastest possible lookups]]
- [[Relational databases enforce a fixed schema and ACID while NoSQL relaxes them for scale]]
- [[Databases - MOC]]
