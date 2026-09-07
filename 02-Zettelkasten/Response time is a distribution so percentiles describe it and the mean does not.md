---
aliases: [percentiles, p50, p95, p99, median response time, response time distribution]
created: 2026-09-03
tags: [performance, latency, observability, architecture, ddia]
---

Every dashboard offers an average response time, and it is the wrong number. Understanding why is the entry point to everything else about performance measurement.

---

### The same request never takes the same time twice

Issue one identical request repeatedly and every response time differs. The causes are mundane and endless: a context switch to a background process, a lost packet and TCP retransmission, a **garbage collection pause**, a page fault forcing a disk read, even mechanical vibration in the server rack.

<mark style="background: #FFF3A3A6;">So response time is a <b>distribution of values</b>, never a single number.</mark> Any metric that collapses it to one number is discarding the shape — and the shape is where the problems live.

---

### What the mean discards

The arithmetic mean gets dragged around by outliers, but that isn't the main charge against it.

<mark style="background: #FF5582A6;">The mean doesn't tell you <b>how many users</b> actually experienced that delay.</mark> "Average 200ms" is compatible with everyone getting 200ms, and with 90% getting 20ms while 10% get 1.8 seconds. Those are different systems and one of them is on fire.

---

### What percentiles preserve

Sort the response times fastest to slowest and read thresholds off the list.

- **p50** — the median. Half of requests are faster, half slower. The honest answer to "how long do users typically wait."
- **p95, p99, p999** — how bad the outliers are. A p95 of 1.5s means 95 requests in 100 finish under 1.5s and 5 do not.

#### One caveat on the median

The median describes a *single request*. If a user makes several — a session, or a page pulling several resources — the probability that at least one of them is slower than the median is much greater than 50%.

<mark style="background: #ABF7F7A6;">A user's experience is the worst of their requests, not the median of them</mark>, which is the seed of [[Tail latency amplification makes the user-visible p99 worse than any single service behind it|tail latency amplification]].

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is what the client sees while latency is only the time a request spends waiting]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users]]
- [[Tail latency amplification makes the user-visible p99 worse than any single service behind it]]
- [[Averaging percentiles is meaningless so aggregate response times by adding histograms]]
