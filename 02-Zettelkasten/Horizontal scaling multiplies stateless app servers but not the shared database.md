---
created: 2026-07-06
tags: [system-design/scaling]
aliases: [horizontal scaling, scale out, scaling out]
---

**Horizontal scaling** ("scale out") means handling more load by adding *more machines*, not by making one machine bigger (that's **vertical scaling**, "scale up"). It's the default answer to growth: put a load balancer in front, spin up N identical app servers behind it.

The word "horizontal" is the hook — you grow *sideways*, adding boxes in a row, rather than *upward* into a single giant box.

<mark style="background: #FFF3A3A6;">It works cleanly only for stateless tiers — where any server can handle any request.</mark>

---

#### Why it works for the app tier

A [[Stateless vs Stateful Services|stateless]] app server keeps no per-user data between requests; state lives in an external store. So request #2 can hit a different server than request #1 with no difference. The load balancer sprays traffic across the pool, and adding a server just adds capacity. Cloud auto-scaling groups (AWS EC2 ASG, Fargate) automate this.

---

#### Why it silently fails to save you

Adding app servers does **not** add database capacity. All N servers point at the same [[The database is the hardest tier to scale because every app server shares one writer|shared database]]. So:

<mark style="background: #FF9E9EA6;">You scale the tier that was never the bottleneck, and pile even more pressure on the tier that was.</mark>

More app servers → more concurrent DB connections, more queries per second → the database saturates *faster*, not slower. See [[A connection storm from new instances can exhaust the database connection limit]].

---

#### Two things "scale out" cannot fix

- **Shared stateful resources** — one database, one message broker, one cache cluster. Cloning app servers doesn't clone these.
- **Time** — new servers aren't instant. They need to boot and warm up before serving, so scale-out can't absorb a *sudden* burst. See [[A newly launched instance needs warm-up before it can serve traffic]] and [[Auto-scaling is reactive so it always trails a sudden traffic spike]].

---

### Read more
- [[The database is the hardest tier to scale because every app server shares one writer]]
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[A newly launched instance needs warm-up before it can serve traffic]]
- [[Server capacity is bounded by whichever resource saturates first, not just RAM]]
- [[System Design - MOC]]
- [[Distributed Systems - MOC]]
