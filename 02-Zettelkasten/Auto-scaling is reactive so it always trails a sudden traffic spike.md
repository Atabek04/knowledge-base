---
created: 2026-07-06
tags: [system-design/scaling]
aliases: [auto-scaling, autoscaling, reactive scaling]
---

**Auto-scaling** watches a metric (CPU %, request count, queue depth) and adds instances when it crosses a threshold, removes them when it drops. It's marketed as "handles any traffic automatically" — which quietly hides a timing problem.

<mark style="background: #FFF3A3A6; font-weight: bold;">Auto-scaling is reactive: it can only respond *after* the metric has already crossed the line. By definition it starts scaling once you're already overloaded.</mark>

---

#### The lag, step by step

1. Traffic spikes — metric climbs.
2. Metric must *stay* above threshold for an evaluation window (often 1–5 min) to avoid flapping.
3. Alarm fires → scaling action requested.
4. New instances launch and [[A newly launched instance needs warm-up before it can serve traffic|warm up]] — another 1–5 min.
5. Only *now* do they take traffic.

<mark style="background: #FF9E9EA6; font-weight: bold;">That's several minutes of lag. A viral moment or a crowd hitting the app peaks in seconds — users have already errored out before new capacity arrives.</mark>

---

#### Why the name is a trap

It's an autoscaler, not an *anticipator*. It reads a thermometer and reacts to the current temperature; it cannot see the spike coming. For **predictable** spikes (Pride, Black Friday, a scheduled event) the fix is to *not* be reactive at all — [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot|pre-warm capacity before the event]].

---

#### When reactive scaling is fine vs not

- **Fine:** gradual, sustained growth — traffic ramps over minutes/hours, lag is invisible.
- **Not fine:** instantaneous bursts — flash sales, breaking news, a physical crowd. The spike outruns the loop. See [[Server capacity is bounded by whichever resource saturates first, not just RAM|the resource that saturates first]] gives out during the lag window.

---

### Read more
- [[A newly launched instance needs warm-up before it can serve traffic]]
- [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot]]
- [[Horizontal scaling multiplies stateless app servers but not the shared database]]
- [[Load shedding drops excess requests to keep the core service alive]]
- [[System Design - MOC]]
