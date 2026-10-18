TARGET DECK: Tech-KB::Observability::Distributed Tracing
Tags: observability tracing
**Related:** [[Observability - MOC]]

START
Coding Questions
Why can't metrics or per-service logs alone show where one slow microservice request spent its time?
Back:
- **Metrics** are aggregates over all requests, never one request
- **Logs** are local to each service, and nothing ties lines from different services to the same request
Tags: observability tracing
<!--ID: 1792287964878-->
END

START
Coding Questions
What ties all the records of one request together across services?
Back: A **trace ID**, created at the first service and forwarded on every call, stamped on every span and log line.
Tags: observability tracing
<!--ID: 1792287964881-->
END

START
Coding Questions
What is a **span**?
Back: One timed unit of work inside a trace: its own span ID, its **parent span ID**, a start time and a duration.
Tags: observability tracing
<!--ID: 1792287964882-->
END

START
Coding Questions
PaymentService span lasts 3100 ms; its child FraudService span lasts 2900 ms. What is Payment's self time and what does it tell you?
Back: 3100 minus 2900 = **200 ms**. Payment is mostly waiting; FraudService is the real bottleneck.
Tags: observability tracing
<!--ID: 1792287964883-->
END

START
Coding Questions
How does a trace show that two calls ran in parallel?
Back: Nothing stores "parallel". Two sibling spans (same parent) whose **time ranges overlap** ran in parallel; if one starts after the other ends, they were sequential.
Tags: observability tracing
<!--ID: 1792287964885-->
END

START
Coding Questions
What does the auto-instrumentation agent create spans for, and why not one per method?
Back: Incoming requests, outgoing calls (HTTP, gRPC, Kafka) and DB queries. A span per method is noise and cost with no new insight.
Tags: observability tracing
<!--ID: 1792287964887-->
END

START
Coding Questions
How does trace context cross an HTTP call?
Back: In the W3C `traceparent` header: `00-<trace_id>-<parent_span_id>-<flag>`; the receiver starts its span as a child of the caller's.
Tags: observability tracing
<!--ID: 1792287964889-->
END

START
Coding Questions
How does trace context cross a Kafka hop?
Back: In the **Kafka record headers** (not the JSON payload); the consumer reads them and starts its span as a child.
Tags: observability tracing kafka
<!--ID: 1792287964890-->
END

START
Coding Questions
Should you compute p99 from traces or from metrics? Why?
Back: From **metric histograms**: they count 100% of requests cheaply. Traces are sampled (and tail sampling skews toward slow ones), so their percentiles are wrong.
Tags: observability tracing metrics
<!--ID: 1792287964891-->
END

START
Coding Questions
What is an **exemplar**?
Back: A sample trace ID stored next to a histogram bucket, so you can click a spike on a latency graph and open a real trace from it.
Tags: observability tracing metrics
<!--ID: 1792287964892-->
END

START
Coding Questions
Why are traces sampled, and what does a dropped request lose?
Back: Cost: e.g. 10k req/s × 20 spans × 1 KB ≈ 200 MB/s. Only the spans (the waterfall) are dropped; metrics and logs with the trace ID remain.
Tags: observability tracing
<!--ID: 1792287964893-->
END

START
Coding Questions
1% head sampling, 30 failed checkouts out of 10,000. How many failed traces end up in Jaeger, and why?
Back: About 30 × 0.01 = **0.3**, so most likely none. Head sampling flips the coin at the first service, before anyone knows the request will fail.
Tags: observability tracing
<!--ID: 1792287964894-->
END

START
Coding Questions
What is **tail sampling** and what policies does it typically use?
Back: Buffer all spans until the trace finishes, then decide. Keep every error, every trace above a latency threshold, plus a small random baseline.
Tags: observability tracing
<!--ID: 1792287964895-->
END

START
Coding Questions
What does tail sampling require from the Collector setup, and what does it still cost?
Back: All spans of one trace must reach the **same Collector instance** (route by trace ID). It saves storage but not network or memory: 100% of spans are still sent and buffered.
Tags: observability tracing
<!--ID: 1792287964896-->
END
