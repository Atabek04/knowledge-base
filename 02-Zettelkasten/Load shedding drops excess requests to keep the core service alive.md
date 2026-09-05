---
created: 2026-07-06
tags: [system-design/reliability]
aliases: [load shedding, graceful degradation]
---

When traffic exceeds capacity and there's no time left to add more, a system has two choices: try to serve *everyone* and collapse under the weight, or deliberately refuse *some* requests so the rest succeed. **Load shedding** is choosing the second.

<mark style="background: #FFF3A3A6;">Load shedding intentionally drops or rejects excess requests once the system is at its limit, so the core keeps working instead of everything failing at once.</mark>

The name is literal — like an overloaded power grid **sheds load** by cutting some districts to keep the rest lit, rather than browning out the whole city.

---

#### Why refusing some requests beats serving all of them

Past capacity, an un-shed system doesn't serve everyone slowly — it enters the [[Server capacity is bounded by whichever resource saturates first, not just RAM|saturation feedback loop]]: queues back up, latency explodes, timeouts trigger client retries, retries add *more* load, total collapse. <mark style="background: #FF9E9EA6;">Trying to serve 100% of a 200%-overload request rate yields 0% served. Shedding the excess 100% keeps the other 100% healthy.</mark>

---

#### How it's applied

- **Rate limiting** — cap requests per client/endpoint; reject over-limit ones fast (HTTP 429) before they consume real work.
- **Priority shedding** — drop low-value traffic first (analytics, non-critical reads), protect the critical path (login, checkout).
- **Queue bounds + fast-fail** — cap the request queue; reject immediately when full instead of letting it grow unboundedly.

This is **graceful degradation**: some features fail, the core survives.

---

#### Related resilience patterns

Load shedding is the "reject inbound excess" tool. Two neighbours handle related failure modes and deserve their own notes:

- <mark style="background: #ADCCFFA6;">**Backpressure**</mark> — flow control *within* a pipeline: a slow consumer signals upstream producers to slow down instead of dropping. (See TCP's version: [[TCP write() blocks when send buffer is full|the send buffer blocking the writer]].)
- <mark style="background: #ADCCFFA6;">**Circuit breaker**</mark> — stop calling a *failing dependency* so its failure doesn't cascade back into your service.

---

### Read more
- [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot]]
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[Server capacity is bounded by whichever resource saturates first, not just RAM]]
- [[TCP write() blocks when send buffer is full]]
- [[System Design - MOC]]
