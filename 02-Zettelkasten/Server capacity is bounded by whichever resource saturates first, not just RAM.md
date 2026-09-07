---
created: 2026-07-06
tags: [system-design/scaling]
aliases: [server capacity, capacity limit, resource saturation]
---

When people say a server "crashed under load," the mental model is often "it ran out of RAM." That's usually wrong. A server has *many* resources, and it dies the moment **any one** of them hits its ceiling — whichever one gets there first.

<mark style="background: #FFF3A3A6;">Capacity is set by the first resource to saturate, not by a single number like memory.</mark> The saturating resource is called the **bottleneck**, and until you fix *that* one, adding any other resource does nothing.

---

#### The resources that can each be "the ceiling"

- **CPU** — request parsing, serialization, business logic, TLS. Maxes on compute-heavy work.
- **RAM** — in-memory sessions, caches, large response buffers. Maxes on memory-heavy work.
- **Database connections** — each request may hold one; the pool and the DB have a hard cap. Often the *real* first ceiling. See [[A connection storm from new instances can exhaust the database connection limit]].
- **Network bandwidth** — bytes in/out per second on the NIC.
- **File descriptors / sockets** — every open connection consumes one; the OS caps them.
- **Thread pool / event loop** — a bounded worker pool; when all workers are busy, new requests queue and time out.

<mark style="background: #FF9E9EA6;">Whichever hits its limit first is the bottleneck — the rest sit idle while the server still falls over.</mark>

---

#### Why "just add RAM" often fixes nothing

If your bottleneck is DB connections or CPU, doubling RAM leaves you at the exact same throughput ceiling — you've paid for headroom on a resource that was never the constraint.

<mark style="background: #ADCCFFA6;">Find the saturating resource first, then scale that.</mark> This is why [[The database is the hardest tier to scale because every app server shares one writer|the database]] is so often the culprit: it's the resource that scales *least* easily when everything else scales freely.

---

#### What "crash" actually looks like

Rarely a clean stop. Usually: latency climbs → request queue backs up → timeouts → clients retry → load *increases* → total collapse. The saturating resource triggers a feedback loop, not a single graceful failure.

---

### Read more
- [[The database is the hardest tier to scale because every app server shares one writer]]
- [[A connection storm from new instances can exhaust the database connection limit]]
- [[Horizontal scaling multiplies stateless app servers but not the shared database]]
- [[System Design - MOC]]
