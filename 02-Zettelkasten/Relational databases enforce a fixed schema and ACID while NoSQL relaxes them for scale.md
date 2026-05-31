---
aliases: [Relational vs NoSQL, SQL vs NoSQL]
tags: [database, data-modeling, nosql, relational-model, architecture]
created: 2026-05-31
---

### The core difference

A **relational database** enforces a <mark style="background: yellow">fixed schema and ACID transactions</mark>. A **NoSQL** database relaxes one or both of those to gain horizontal scale and flexibility.

It is a trade, not a ranking. You give up guarantees to get something else.

---

### What relational gives you

- **Schema on write** — the table shape is enforced at insert time; bad data is rejected
- **ACID** — multi-row, multi-table changes are atomic and consistent
- **Joins** — relationships are first-class, normalized across tables
- **Strong consistency** — a read after a write sees the write

Best fit: data with clear relationships and **strong integrity needs** — payments, orders, inventory, anything where a wrong number is unacceptable.

---

### What NoSQL trades for

NoSQL is an umbrella over several models (document, key-value, column-family, graph). What they tend to share:

- **Schema on read** — flexible/evolving structure, no migration to add a field
- **Horizontal scale** — designed to shard across many nodes
- **Often eventual consistency** — accept temporary divergence for availability (the [[CAP theorem forces a partitioned system to choose between consistency and availability|CAP]] trade)

Best fit: <mark style="background: #93d4d4">huge volume, flexible shape, or extreme read/write rates</mark> where rigid schema and cross-shard joins would be the bottleneck.

---

### How to decide

Don't ask "SQL or NoSQL?" Ask:

- Do I need multi-record **transactions**? → relational
- Are **relationships and joins** central? → relational (or graph)
- Is the data shape **unstable or schemaless**? → document
- Do I need to scale **writes past one machine**? → a NoSQL model
- Can I tolerate **stale reads** for availability? → NoSQL is on the table

<mark style="background: #f9a8d4">Relational is the right default until a specific requirement forces you off it.</mark>

---

Read more:
- [[A document database stores self-describing records queried by their nested content]]
- [[Choosing a database means matching its model and guarantees to non-functional requirements]]
- [[CAP theorem forces a partitioned system to choose between consistency and availability]]
- [[Databases - MOC]]
