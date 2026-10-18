---
aliases: [span, parent span, self time]
created: 2026-10-18
tags: [observability, tracing]
---

A [[Distributed tracing follows one request across services by sharing a trace ID|trace ID]] groups the records of one request, but a flat group cannot say who waited on whom. Spans add that structure.

---

### What a span records

> [!definition] Span
> A **span** is one timed unit of work inside a trace, with its own span ID, the ID of its parent span, a start time and a duration.

Spans are not created per method. The OpenTelemetry Java agent creates one per incoming request, per outgoing call (HTTP, gRPC, Kafka publish) and per database query. You add a custom span, for example with `@WithSpan`, only for a slow in-process step worth seeing.

<mark style="background: #FF5582A6;">A span per method floods the tracer with noise and cost without explaining anything new.</mark>

---

### Self time exposes the real culprit

Start times are in milliseconds from the start of the request.

| span | parent | name | start | duration |
|---|---|---|---|---|
| A | none | OrderService | 0 | 4200 |
| B | A | PaymentService | 50 | 3100 |
| C | B | FraudService | 100 | 2900 |
| D | A | InventoryService | 60 | 400 |

`PaymentService` lasts 3100 ms, but 2900 ms of that is its child `FraudService`. Its own work is 3100 minus 2900, about 200 ms.

<mark style="background: #FFF3A3A6;">Self time is a span's duration minus the time covered by its children.</mark>

#### Database spans

Each JDBC span carries the query text and its duration. One 2.5 s span is a slow query; 200 sibling spans of 5 ms each running the same query is an N+1 loop.

<mark style="background: #FF5582A6;">A span shows where time went, never why a query was slow; that still needs the query plan from EXPLAIN ANALYZE.</mark>

---

### Parallel calls are inferred from overlap

No field says "parallel". B and D share parent A, so they are siblings. B runs 50 to 3150 ms and D runs 60 to 460 ms; the ranges overlap, so they ran at the same time.

<mark style="background: #ABF7F7A6;">Siblings whose time ranges overlap ran in parallel; siblings where one starts after the other ends ran in sequence.</mark>

Jaeger's waterfall view draws exactly this: overlapping bars are parallel, a staircase is sequential.

---

### Read more

- [[Observability - MOC]]
- [[Distributed tracing follows one request across services by sharing a trace ID]]
- [[Trace context propagates in the traceparent header across HTTP and in record headers across Kafka]]
