---
aliases: [distributed tracing, trace ID, tracing]
created: 2026-10-18
tags: [observability, tracing, microservices]
---

In a microservice system one user click fans out into calls across many services. When that click is slow or fails, you need to know which hop caused it, and neither metrics nor logs can tell you on their own.

---

### Glossary

- **Trace**: <mark style="background: #FFF3A3A6;">the full record of one request's path through every service it touched</mark>.
- **Trace ID**: a random identifier created at the first service and carried by every later hop of the same request.
- **Tracer**: a system such as Jaeger, Zipkin or Grafana Tempo that collects, stores and draws traces.

---

### Why metrics and logs cannot follow one request

A checkout goes `Gateway → OrderService → PaymentService → FraudService`, plus `InventoryService` and `NotificationService`. One user reports 4.2 s instead of the usual 300 ms.

Metrics are aggregates. Every service's p99 is up a little, and none stands out, because a metric describes all requests, never one.

Logs are local. `PaymentService` logs "charge done in 3.1s" and `OrderService` logs "request done in 4.2s", but a thousand other checkouts ran in the same minute and nothing ties those two lines to the same click.

---

### The trace ID ties the hops together

<mark style="background: #ABF7F7A6;">The first service generates a trace ID, every call passes it to the next service, and every service stamps it on what it records, so one request can be pulled out of millions.</mark>

The ID only works if every hop forwards it. A service that drops it breaks the chain at that point; how it travels is covered in [[Trace context propagates in the traceparent header across HTTP and in record headers across Kafka|trace context propagation]].

Grouping by trace ID gives you the lines of one request. To see where its time went, each line also needs timing and a parent, which is what a [[A span records one timed unit of work and its parent span ID builds the trace into a tree|span]] adds.

---

### Read more

- [[Observability - MOC]]
- [[A span records one timed unit of work and its parent span ID builds the trace into a tree]]
- [[Trace context propagates in the traceparent header across HTTP and in record headers across Kafka]]
- [[Metrics compute percentiles while traces explain why one request was slow]]
- [[Tail latency amplification makes the user-visible p99 worse than any single service behind it]]
