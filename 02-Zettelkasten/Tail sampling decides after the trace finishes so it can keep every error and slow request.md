---
aliases: [tail sampling, tail-based sampling]
created: 2026-10-18
tags: [observability, tracing, opentelemetry]
---

[[Head sampling decides at the first service so it usually drops the rare failing trace|Head sampling]] decides before a request has done anything, so it drops the rare failures. Tail sampling moves the decision to after the request has finished.

---

### The policies

> [!definition] Tail sampling
> **Tail sampling** buffers every span of a trace until the trace is complete, then decides whether to keep it based on what happened.

A typical policy set in the OpenTelemetry Collector's `tail_sampling` processor:
- keep every trace with an error status
- keep every trace slower than a threshold, say 1 s
- keep a small random share, say 1%, as a baseline of healthy traffic

---

### What it costs

Every service sends 100% of its spans to the **OpenTelemetry Collector**, which holds each trace in memory for a few seconds until no more spans arrive.

<mark style="background: #FF5582A6;">All spans of one trace must reach the same Collector instance, or no single instance sees the error; a front layer routes spans by trace ID to guarantee it.</mark>

<mark style="background: #ABF7F7A6;">Tail sampling cuts the storage bill but not the network and memory bill, because everything is still sent and buffered.</mark>

---

### Read more

- [[Observability - MOC]]
- [[Head sampling decides at the first service so it usually drops the rare failing trace]]
- [[Metrics compute percentiles while traces explain why one request was slow]]
