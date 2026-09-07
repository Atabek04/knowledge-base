---
aliases: [queueing delay, head-of-line blocking, closed loop load testing, client-side measurement]
created: 2026-09-03
tags: [performance, latency, observability, testing, ddia]
---

Queueing delay accounts for a large part of response time at high percentiles. It is also the component your instruments are structurally worst at seeing — and there are two separate blind spots, one in production and one in load testing.

---

### Head-of-line blocking

A server processes only a small number of requests in parallel, bounded by something like its CPU core count.

<mark style="background: #FFF3A3A6;">So it takes only a handful of slow requests to hold up everything queued behind them.</mark> The requests stuck in line are **fast to process and slow to return** — the handler runs in 5ms after waiting 800ms for its turn.

The name is literal: the request at the head of the line blocks every request behind it, regardless of how cheap those are.

---

### Blind spot one — server-side metrics

The server's own timer starts when it picks the request up. The 800ms of waiting happened before that, so server-side timing shows a healthy 5ms while the client experiences 805ms.

<mark style="background: #FF5582A6;">Response times must be measured on the client side.</mark> A server-side latency dashboard cannot see its own queue, and will report green through a saturation incident.

---

### Blind spot two — the load generator

The same effect corrupts load tests, in a way that makes results look better than reality.

If the load-generating client waits for the previous request to complete before sending the next, it **artificially keeps the queues shorter than they would be in production**. The generator throttles itself in exact proportion to how slow the system is — so the harder the system struggles, the gentler the test becomes.

<mark style="background: #FFB8EBA6;">A load generator must keep sending requests independently of response time</mark>, or the numbers are a comfortable lie.

Same failure shape as [[Auto-scaling is reactive so it always trails a sudden traffic spike|autoscaling lagging a spike]]: a gradual ramp never produces the queue that a real step change does.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is what the client sees while latency is only the time a request spends waiting]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users]]
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[A newly launched instance needs warm-up before it can serve traffic]]
