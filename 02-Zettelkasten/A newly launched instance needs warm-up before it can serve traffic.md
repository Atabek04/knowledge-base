---
created: 2026-07-06
tags: [system-design/scaling]
aliases: [warm-up, cold start, instance warm-up, warm-up lag]
---

A common assumption behind auto-scaling: "the new server is ready the moment it launches." It isn't. Between "instance created" and "instance can actually serve requests" there's a **warm-up** gap of anywhere from tens of seconds to several minutes.

<mark style="background: #FFF3A3A6;">A freshly launched instance is alive but not ready — it must boot and warm up before its first useful response.</mark> This is the same distinction Kubernetes encodes with [[A failing readiness probe removes the pod from Service endpoints|readiness probes]]: alive ≠ ready.

---

#### What has to happen during warm-up

- **Boot** — OS start, container pull, runtime start (JVM/Node), framework init.
- **JIT / class loading** — a JVM runs slow and cold until hot paths compile; first requests are sluggish.
- **Connection setup** — open the database pool, connect to cache and broker. Every new instance does this — at scale it becomes a [[A connection storm from new instances can exhaust the database connection limit|connection storm]].
- **Cold cache** — the local cache is empty, so early requests all miss and fall through to the database. See [[A cold cache sends every request to the database, causing a thundering herd]].

---

#### Why warm-up defeats reactive scaling

The whole point of [[Auto-scaling is reactive so it always trails a sudden traffic spike|auto-scaling]] is to add capacity fast. Warm-up is the reason it can't be fast enough for a burst: <mark style="background: #FF9E9EA6;">the spike peaks in seconds, but a new instance takes minutes to become useful — and its first minutes actively make things worse (cold cache, connection setup) before they get better.</mark>

---

#### How teams shrink the gap

- **Pre-baked images** (AMIs / container images with deps already installed) → cut boot time.
- **Warm pools** — keep idle, already-booted instances on standby, so "scaling" is just routing traffic to them, not building from scratch.
- **Cache pre-loading / request replay** to warm hot paths before taking live traffic.

These are the mechanics behind [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot|pre-warming for known spikes]].

---

### Read more
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[A cold cache sends every request to the database, causing a thundering herd]]
- [[A connection storm from new instances can exhaust the database connection limit]]
- [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[System Design - MOC]]
