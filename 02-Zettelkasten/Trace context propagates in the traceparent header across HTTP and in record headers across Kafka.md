---
aliases: [context propagation, traceparent, W3C Trace Context]
created: 2026-10-18
tags: [observability, tracing, kafka]
---

A trace only exists if every service learns which trace it is part of and which span called it. Passing that information along is called context propagation.

---

### The traceparent header over HTTP

> [!definition] Trace context
> The **trace context** is the trace ID, the caller's span ID and the sampling flag, passed from one service to the next so the receiver's span becomes a child of the caller's.

The W3C Trace Context standard carries it in one header:

```
traceparent: 00-<trace_id>-<parent_span_id>-01
```

The last field is the sampling flag: `01` keep, `00` drop. The OpenTelemetry Java agent injects and reads this header for `RestTemplate`, `WebClient` and Feign automatically.

---

### Record headers over Kafka

An event published to Kafka has no HTTP request to carry a header. <mark style="background: #ABF7F7A6;">The producer writes the trace context into the Kafka record headers, and the consumer reads it to start its span as a child, so an asynchronous hop joins the same trace.</mark>

Headers keep it out of the JSON payload, so business data stays clean. The agent handles `KafkaTemplate` and `@KafkaListener` for you.

<mark style="background: #FF5582A6;">Context is lost wherever code leaves the instrumented path, such as a hand-rolled thread pool or a message sent without headers, and the trace splits in two at that point.</mark>

---

### Read more

- [[Observability - MOC]]
- [[Distributed tracing follows one request across services by sharing a trace ID]]
- [[A span records one timed unit of work and its parent span ID builds the trace into a tree]]
- [[Head sampling decides at the first service so it usually drops the rare failing trace]]
