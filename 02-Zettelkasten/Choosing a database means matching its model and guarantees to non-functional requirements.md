---
aliases: [Database Selection, Choosing a Database, DB selection]
tags: [database, data-modeling, architecture, nfr]
created: 2026-05-31
---

### The decision is requirement-driven

Picking a database is not about which one is "best" — it's about matching a store's **data model and guarantees** to your <mark style="background: yellow">non-functional requirements</mark> (NFRs).

Start from what the system must promise — consistency, scale, latency, query shape — then pick the model that gives it cheapest.

---

### A decision heuristic

Walk the NFRs in priority order:

| If the dominant requirement is… | Lean toward… |
|--|--|
| Multi-record **transactions / strong integrity** | Relational |
| **Flexible / evolving** record shape | [[A document database stores self-describing records queried by their nested content\|Document]] |
| **Lowest-latency** lookups by known key | [[A key-value store maps opaque keys to values for the fastest possible lookups\|Key-value]] |
| **Massive write throughput**, time-series, sparse | [[A column-family store groups columns into families for wide sparse write-heavy tables\|Column-family]] |
| **Deep relationship traversal** | [[A graph database makes relationships first-class for traversal-heavy queries\|Graph]] |
| **Analytical scans / aggregations** | Columnar OLAP ([[ClickHouse - MOC\|ClickHouse]]) |

---

### Two rules that keep you honest

**Model around your access patterns.** In NoSQL especially, you design tables for the queries you'll run, not for the entities. The dominant *query* often picks the database.

**Polyglot persistence is normal.** One system can use several stores — Postgres for orders, Redis for sessions, ClickHouse for analytics. Each NFR set goes to the store that serves it best (the [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics|dual-write pattern]] is exactly this).

<mark style="background: #f9a8d4">Don't reach for a specialized store until a requirement forces it</mark> — every extra database is operational cost.

---

Read more:
- [[Relational databases enforce a fixed schema and ACID while NoSQL relaxes them for scale]]
- [[CAP theorem forces a partitioned system to choose between consistency and availability]]
- [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics]]
- [[Databases - MOC]]
- [[Distributed Systems - MOC]]
