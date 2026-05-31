---
aliases: [Graph Database]
tags: [database, nosql, data-modeling]
created: 2026-05-31
---

### What it is

A **graph database** stores data as **nodes** and **edges**, making <mark style="background: yellow">relationships first-class citizens</mark> rather than something reconstructed with joins.

Examples: Neo4j, Amazon Neptune. A node is an entity; an edge is a typed, directed relationship between two nodes.

---

### Why joins are the problem it solves

In a relational DB, "find friends of friends of friends" means JOINing the same table three times — and cost explodes with depth.

A graph database stores each relationship as a direct pointer, so traversal is following edges, not matching keys. <mark style="background: #93d4d4">Deep relationship queries stay cheap regardless of total data size.</mark>

```
(Ali)-[:FRIEND]->(Sara)-[:FRIEND]->(Omar)
```

---

### Strengths

- **Traversal performance** — multi-hop queries don't degrade like recursive joins
- **Relationships carry data** — edges have types and properties
- Natural fit for **connected data**: social graphs, recommendations, fraud rings, access/permission graphs, knowledge graphs

---

### Weaknesses

- <mark style="background: #f9a8d4">Wrong tool for aggregate-heavy or tabular analytics</mark> — "sum all order totals this month" is awkward
- Harder to shard than key-value (relationships cross partitions)

Best fit: when the **connections between entities** are the most important thing you query.

---

Read more:
- [[A column-family store groups columns into families for wide sparse write-heavy tables]]
- [[Relational databases enforce a fixed schema and ACID while NoSQL relaxes them for scale]]
- [[Databases - MOC]]
