---
created: 2026-07-06
tags: [system-design/scaling, databases/scaling]
aliases: [database bottleneck, shared writer bottleneck]
---

When traffic spikes, teams add more app servers and expect the problem to disappear. It often doesn't — because the app tier and the database tier scale in completely different ways.

The app tier is usually **stateless**: any server can handle any request, so you just add more of them. The database is **stateful**: it holds the single source of truth. <mark style="background: #FFF3A3A6;">Every one of those new app servers points at the same database, so the database is the one tier you cannot clone away.</mark>

---

#### Why the writer is the choke point

A relational database typically has **one primary that accepts writes**. You can add read replicas to spread out reads, but every write still funnels through that single primary. Add 100 app servers and they all hammer one writer.

<mark style="background: #FF9E9EA6;">Scaling the stateless tier just moves the pressure downstream onto the database — the bottleneck relocates, it doesn't disappear.</mark> This is the concrete reason [[Horizontal scaling multiplies stateless app servers but not the shared database|horizontal scaling alone stalls]].

---

#### The ways the database *can* scale — all with costs

- **Read replicas** — copies that serve reads only; help read-heavy load, do nothing for writes, and lag behind the primary (stale reads).
- **Sharding** — split data across multiple primaries by a key (e.g. user ID, geography). Scales writes, but adds routing logic, cross-shard queries, and a <mark style="background: #FF9E9EA6;">hot-shard risk when one key gets a traffic spike</mark> (a crowd in one city → one shard melts).
- **Connection pooler** (PgBouncer) — caps how many connections reach the DB so app servers can't overwhelm it. See [[A connection storm from new instances can exhaust the database connection limit]].
- **Caching** — absorb reads *before* they reach the DB. See [[A cold cache sends every request to the database, causing a thundering herd]].

---

#### Why this matters for outages

Most "the servers crashed" stories are really "the database saturated." Because it's the shared, stateful, single-writer tier, it is <mark style="background: #ADCCFFA6;">the resource that most often becomes [[Server capacity is bounded by whichever resource saturates first, not just RAM|the first to saturate]]</mark> — and the hardest to relieve mid-incident.

---

### Read more
- [[Server capacity is bounded by whichever resource saturates first, not just RAM]]
- [[Horizontal scaling multiplies stateless app servers but not the shared database]]
- [[A connection storm from new instances can exhaust the database connection limit]]
- [[A cold cache sends every request to the database, causing a thundering herd]]
- [[System Design - MOC]]
- [[Databases - MOC]]
