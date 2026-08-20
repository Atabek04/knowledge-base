TARGET DECK: Tech-KB::System Design::Scaling & Resilience
Tags: system-design scaling resilience
**Related:** [[System Design - MOC]]

---

START
Coding Questions
When a server "crashes under load," what actually sets its capacity limit?
Back: The **first resource to saturate** — not just RAM. Capacity is bounded by whichever resource hits its ceiling first (the **bottleneck**):
- CPU, RAM, **DB connections**, network bandwidth, file descriptors, thread pool
Until you fix *that* one, adding any other resource does nothing.
Tags: system-design scaling capacity
<!--ID: 1787201882983-->
END

START
Coding Questions
Why does "just add more RAM" often fail to fix an overloaded server?
Back: Because RAM may not be the **bottleneck**. If the saturating resource is CPU or DB connections, doubling RAM leaves you at the exact same throughput ceiling — you paid for headroom on a resource that was never the constraint.
Tags: system-design scaling capacity
<!--ID: 1787201882985-->
END

START
Coding Questions
Why is the database the hardest tier to scale?
Back: It is **stateful** and **shared** — every app server points at the same DB, and writes funnel through a **single primary**.
- You can clone stateless app servers freely, but not the one source of truth
- Scaling the app tier just moves pressure downstream onto the DB
Tags: system-design scaling database
<!--ID: 1787201882987-->
END

START
Coding Questions
Horizontal scaling adds app servers — why doesn't that add database capacity?
Back: Horizontal scaling multiplies **stateless app servers**, but they all point at the same **shared database**. More app servers → more concurrent connections and queries → the DB saturates *faster*, not slower. The bottleneck relocates, it doesn't disappear.
Tags: system-design scaling horizontal
<!--ID: 1787201882989-->
END

START
Coding Questions
What is the difference between horizontal and vertical scaling?
Back:
- **Horizontal (scale out)** — add *more machines* behind a load balancer; grow sideways. Works for stateless tiers.
- **Vertical (scale up)** — make *one machine bigger* (more CPU/RAM); grow upward.
Tags: system-design scaling horizontal
<!--ID: 1787201882991-->
END

START
Coding Questions
Why can't reactive auto-scaling absorb a sudden traffic spike?
Back: Auto-scaling is **reactive** — it only acts *after* a metric crosses a threshold, so it starts scaling once you're already overloaded. Add the evaluation window (1–5 min) plus new-instance **warm-up** (1–5 min) and there are several minutes of lag. A burst peaks in seconds — users error out before capacity arrives.
Tags: system-design scaling autoscaling
<!--ID: 1787201882992-->
END

START
Coding Questions
Why is a newly launched instance not ready to serve traffic immediately?
Back: It's **alive but not ready** — it needs **warm-up** first:
- Boot (OS, container, runtime)
- JIT / class loading (slow while cold)
- Open DB pool, cache, broker connections
- Warm its cache (starts empty → early requests all miss)
Same as Kubernetes readiness: alive ≠ ready.
Tags: system-design scaling warmup
<!--ID: 1787201882994-->
END

START
Coding Questions
How do teams shrink instance warm-up time?
Back:
- **Pre-baked images** (AMIs / container images with deps installed) → faster boot
- **Warm pools** — idle, already-booted instances on standby
- **Cache pre-loading** — start warm, avoid cold-cache misses
Tags: system-design scaling warmup
<!--ID: 1787201882996-->
END

START
Coding Questions
What is a connection storm, and how can scaling out cause an outage?
Back: A DB accepts a **bounded number of connections** (~100 in Postgres). Each app server opens its own pool. When many instances launch at once, their pools collectively demand more connections than the DB allows — the **connection storm** — and the DB rejects new connections.
Example: 20 conns/instance × 5 instances = 100 → cap hit → 6th instance locked out.
Tags: system-design scaling connections
<!--ID: 1787201882998-->
END

START
Coding Questions
How do you prevent a connection storm when scaling out?
Back: Put a **connection pooler** (PgBouncer, RDS Proxy) *between* app servers and the DB. It multiplexes thousands of client connections onto a small fixed set of real DB connections — decoupling instance count from DB connection count.
Tags: system-design scaling connections
<!--ID: 1787201883000-->
END

START
Coding Questions
What is a thundering herd (cache stampede) and what triggers it?
Back: A **cold cache** means every request misses and falls straight through to the DB at once — a herd of requests thundering at the DB, crushing what the cache was meant to protect.
Triggers:
- **New instance** with an empty local cache
- **Synchronized expiry** — many keys cached together with the same TTL expire at once
Tags: system-design caching stampede
<!--ID: 1787201883002-->
END

START
Coding Questions
What are the standard defenses against a cache stampede?
Back:
- **TTL jitter** — random offset per key so they don't all expire together
- **Request coalescing (single-flight)** — one request repopulates, the rest wait
- **Cache warming** — pre-load hot keys before serving
- **Stale-while-revalidate** — serve the old value while one request refreshes
Tags: system-design caching stampede
<!--ID: 1787201883004-->
END

START
Coding Questions
For a *predictable* spike (Pride, Black Friday), why is pre-warming better than reactive auto-scaling?
Back: Reactive auto-scaling starts *after* overload and needs warm-up. **Pre-warming** provisions capacity *ahead of time* on a schedule (scheduled scaling, warm pools, pre-loaded caches) — capacity is already there before the wave lands, replacing "react after overload" with "already provisioned."
Tags: system-design scaling prewarming
<!--ID: 1787201883006-->
END

START
Coding Questions
What is headroom, and why run below full utilization on purpose?
Back: **Headroom** = running each tier at moderate utilization (40–60%), not 90%. The spare margin absorbs a sudden burst *instantly*, buying the minutes reactive scaling needs. A system pinned at 90% has no buffer — the smallest spike tips it over. Trade-off: pay for idle capacity to buy resilience.
Tags: system-design scaling headroom
<!--ID: 1787201883008-->
END

START
Coding Questions
What is load shedding, and why does refusing some requests beat serving all of them?
Back: **Load shedding** deliberately drops/rejects excess requests once at capacity, so the core keeps working. Past capacity, serving everyone triggers a feedback loop: queues back up → timeouts → retries → more load → collapse.
Serving 100% of a 200%-overload rate yields 0% served; shedding the excess keeps the other 100% healthy.
Tags: system-design resilience load-shedding
<!--ID: 1787201883010-->
END

START
Coding Questions
How is load shedding applied, and how does it differ from backpressure and circuit breakers?
Back: Applied via **rate limiting** (429), **priority shedding** (drop low-value first), **bounded queues + fast-fail**.
- **Load shedding** — reject inbound excess
- **Backpressure** — signal upstream producers to slow down within a pipeline
- **Circuit breaker** — stop calling a *failing dependency* to prevent cascade
Tags: system-design resilience load-shedding
<!--ID: 1787201883012-->
END
