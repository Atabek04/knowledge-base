---
aliases: [head sampling, trace sampling, TraceIdRatioBasedSampler]
created: 2026-10-18
tags: [observability, tracing]
---

Storing every trace is too expensive, so a tracer keeps a sample. The question is when the keep-or-drop decision is made.

---

### Why traces are dropped at all

At 10,000 requests per second with 20 spans each and roughly 1 KB per span, that is 200,000 spans and about 200 MB every second, around 17 TB a day. Most of it repeats "checkout, 300 ms, OK".

<mark style="background: #FF5582A6;">Sampling drops only the trace's spans; metrics still count every request and logs still carry the trace ID.</mark> What a dropped request loses is its waterfall.

---

### How head sampling decides

> [!definition] Head sampling
> **Head sampling** makes the keep-or-drop decision at the first service, when the request starts, and passes it downstream in the sampling flag.

OpenTelemetry's `TraceIdRatioBasedSampler` with ratio `0.01` treats the random trace ID as a number and keeps the trace when it falls in the lowest 1%. It is a fair coin that lands "keep" once in a hundred.

---

### Why it misses failures

<mark style="background: #ABF7F7A6;">The coin is flipped before the request has done anything, so it cannot favour requests that will later fail or run slow.</mark>

Of 10,000 checkouts, 30 fail in `FraudService`. At 1%, the expected number of kept failures is 30 times 0.01, which is 0.3, so most likely Jaeger holds none of them. [[Tail sampling decides after the trace finishes so it can keep every error and slow request|Tail sampling]] fixes this by deciding at the end.

---

### Read more

- [[Observability - MOC]]
- [[Tail sampling decides after the trace finishes so it can keep every error and slow request]]
- [[Trace context propagates in the traceparent header across HTTP and in record headers across Kafka]]
