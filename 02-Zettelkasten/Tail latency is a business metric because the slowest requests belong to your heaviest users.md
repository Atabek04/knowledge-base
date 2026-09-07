---
aliases: [tail latency, p999, high percentiles, SLA percentiles]
created: 2026-09-03
tags: [performance, latency, architecture, ddia]
---

High percentiles of response time are called **tail latencies**. The engineering argument for caring about them is obvious — outliers are bad. The commercial argument is not obvious, and it's the one that gets budget.

---

### Why the slow requests are the valuable ones

Amazon specifies internal service response times at the **99.9th percentile**, even though that affects only 1 request in 1,000.

<mark style="background: #ADCCFFA6;">The reason is a correlation: the customers with the slowest requests are usually the ones with the most data on their accounts, because they have made the most purchases.</mark>

The tail is not a random sample of your users. It is disproportionately your best ones — the accounts with the longest order history, the biggest carts, the most saved items. Slowness is selecting for value.

The measured stakes: a **100 ms** increase in response time cost Amazon about **1% of sales**, and others report a **1-second** slowdown moving a customer satisfaction metric by **16%**.

---

### Where to stop

<mark style="background: #FFB8EBA6;">Amazon deemed optimizing the 99.99th percentile — the slowest 1 in 10,000 — not worth the cost.</mark>

Response times at very high percentiles are dominated by random events outside your control, so effort stops converting into improvement. The extreme tail eventually stops being your fault, and chasing it is a real trap.

#### This is what percentiles are for contractually

**SLOs** and **SLAs** are written in percentiles for exactly this reason. An SLA might define the service as up if the median is under 200ms and p99 under 1s, and require that for 99.9% of the time — with a refund if missed.

A mean cannot be written into a contract usefully, because it makes no promise to any individual request.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Tail latency amplification makes the user-visible p99 worse than any single service behind it]]
- [[Queueing delay is invisible to server-side metrics and to closed-loop load generators]]
