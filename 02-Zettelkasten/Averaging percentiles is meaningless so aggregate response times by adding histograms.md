---
aliases: [averaging percentiles, histogram aggregation, percentile aggregation]
created: 2026-09-03
tags: [performance, observability, metrics, ddia]
---

Once you are reporting percentiles, two practical needs arrive immediately: reducing time resolution (a p99 per hour instead of per minute), and combining several machines into one number. The obvious move for both is to average the percentiles together, and it is wrong.

---

### Why it doesn't work

<mark style="background: #FF9E9EA6;">Averaging percentiles is mathematically meaningless.</mark>

A p99 is a **threshold on one distribution** — the value below which 99% of that machine's requests fell. The mean of two thresholds is a threshold on nothing; there is no distribution for which it is the 99th percentile.

Concretely: one server handling 10 requests reports p99 of 2s, another handling 10,000 reports p99 of 50ms. Their average, ~1s, describes neither the fleet nor any user. The number is not merely imprecise — it is not a percentile at all.

---

### The correct aggregation

<mark style="background: #ABF7F7A6;">Add the <b>histograms</b>, then recompute the percentile from the combined data.</mark>

A histogram keeps counts per bucket, so buckets from different machines or different minutes sum cleanly, and the percentile is read off the sum. This is why metrics systems store latency as histograms rather than as pre-computed percentiles.

If your monitoring can only average pre-aggregated p99s across instances, its fleet-wide p99 is a decorative number.

#### Computing them cheaply

Keeping every response time in a rolling window and sorting it each minute is the naive approach and is often too expensive. Approximation algorithms exist for exactly this: **forward decay**, **t-digest**, and **HdrHistogram**.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users]]
