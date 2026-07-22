---
created: 2026-07-06
tags: [system-design/scaling, system-design/reliability]
aliases: [pre-warming, pre-scaling, headroom, overprovisioning]
---

[[Auto-scaling is reactive so it always trails a sudden traffic spike|Reactive auto-scaling]] can't catch a burst: it starts scaling *after* you're overloaded, and new instances need [[A newly launched instance needs warm-up before it can serve traffic|warm-up]]. So the fix for spiky traffic is to have the capacity **already there** before the spike lands.

Two complementary tactics: pre-warm for spikes you can predict, keep headroom for the ones you can't.

---

#### Pre-warming — capacity ready before a known spike

For **predictable** events (Pride, Black Friday, a product launch, a scheduled broadcast), don't wait for a metric to trip. Scale up *ahead of time* on a schedule.

- **Scheduled scaling** — grow the fleet at a fixed time, before traffic arrives.
- **Warm pools** — keep idle, already-booted instances on standby so activation is instant, skipping warm-up.
- **Pre-load caches** so instances start warm, avoiding the [[A cold cache sends every request to the database, causing a thundering herd|cold-cache thundering herd]].

<mark style="background: #FFF3A3A6; font-weight: bold;">Pre-warming replaces "react after overload" with "already provisioned before the wave."</mark>

---

#### Headroom — run below the ceiling on purpose

For **unpredictable** bursts, keep every tier running at moderate utilization (say 40–60%), not 90%. That spare margin is **headroom** — it absorbs a sudden jump instantly, buying the minutes that reactive scaling needs to add real capacity.

<mark style="background: #FF9E9EA6; font-weight: bold;">A system pinned at 90% utilization has no buffer — the smallest spike tips it over before autoscaling can react.</mark> Headroom trades some idle cost for survivability.

---

#### The trade-off

Both cost money — you pay for capacity you're not fully using. That's the deliberate exchange: <mark style="background: #ADCCFFA6; font-weight: bold;">spend on idle headroom to buy resilience against bursts.</mark> When even pre-warming and headroom aren't enough, the last line of defense is to shed load — [[Load shedding drops excess requests to keep the core service alive]].

---

### Read more
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[A newly launched instance needs warm-up before it can serve traffic]]
- [[A cold cache sends every request to the database, causing a thundering herd]]
- [[Load shedding drops excess requests to keep the core service alive]]
- [[System Design - MOC]]
