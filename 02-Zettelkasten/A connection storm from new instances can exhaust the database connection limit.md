---
created: 2026-07-06
tags: [system-design/scaling, databases/scaling]
aliases: [connection storm, connection exhaustion, DB connection limit]
---

Scaling out to fight overload can *cause* an outage in a way that surprises people. You add app servers to spread the load — and the database dies anyway, refusing everyone including healthy traffic. The reason is connections.

A database accepts only a **bounded number of concurrent connections** (Postgres defaults ~100). Each app server opens its own [[Connection pooling manages multiple pre-established connections|connection pool]]. <mark style="background: #FFF3A3A6;">When many instances launch at once, their pools collectively demand far more connections than the database allows — a connection storm — and the database starts rejecting new connections.</mark>

---

#### The arithmetic that bites

Say each instance opens a pool of 20 connections, and the DB cap is 100.

<mark style="background: #FF9E9EA6;">5 instances × 20 = 100 → cap reached. The 6th instance's connections are refused. Auto-scaling to 20 instances doesn't add capacity — it locks everyone out.</mark>

Worse, a rejected connection isn't free: the DB spends CPU refusing them, and each connection it *does* accept costs memory and a backend process — so more connections can slow the DB even below the hard cap.

---

#### Why scaling out makes it worse, not better

[[Horizontal scaling multiplies stateless app servers but not the shared database|Adding app servers]] multiplies pools pointing at one database. The tier you scaled (stateless app) isn't the constraint; the shared connection budget is. This is a concrete face of [[Server capacity is bounded by whichever resource saturates first, not just RAM|the first-resource-to-saturate rule]] — here the saturating resource is *DB connections*, not CPU or RAM.

---

#### The fix: a connection pooler in front of the DB

Put a **connection pooler** (PgBouncer, RDS Proxy) *between* the app servers and the database. App servers connect to the pooler; the pooler multiplexes thousands of client connections onto a small, fixed set of real DB connections.

<mark style="background: #ADCCFFA6;">Now the number of app servers is decoupled from the number of DB connections — you can scale out without a storm.</mark>

---

### Read more
- [[The database is the hardest tier to scale because every app server shares one writer]]
- [[Horizontal scaling multiplies stateless app servers but not the shared database]]
- [[Server capacity is bounded by whichever resource saturates first, not just RAM]]
- [[A newly launched instance needs warm-up before it can serve traffic]]
- [[Connection pooling manages multiple pre-established connections]]
- [[System Design - MOC]]
- [[Databases - MOC]]
