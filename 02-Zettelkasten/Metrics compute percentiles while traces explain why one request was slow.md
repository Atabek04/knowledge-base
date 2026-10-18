---
aliases: [metrics vs traces, exemplars, percentiles from histograms]
created: 2026-10-18
tags: [observability, tracing, metrics]
---

Metrics and traces both measure latency, so it is tempting to compute p99 from traces. They answer different questions, and each is wrong at the other's job.

---

### Percentiles come from histograms

Each service counts every request into histogram buckets ("under 100 ms", "under 250 ms" and so on). In Spring Boot, Micrometer exposes `http_server_requests_seconds`, and Prometheus estimates the percentile from the bucket counts:

```promql
histogram_quantile(0.99, sum by (le) (rate(http_server_requests_seconds_bucket[5m])))
```

A histogram is a set of counters, so it covers 100% of requests at almost no cost.

---

### Why traces make bad percentiles

<mark style="background: #FF5582A6;">Traces are sampled, so a p99 computed from them rests on a handful of slow requests, and tail sampling skews the sample toward slow ones on purpose.</mark>

---

### Each signal has one job

<mark style="background: #ADCCFFA6;">Use metrics to detect that something is wrong and to alert, and traces to explain why one specific request was slow.</mark>

#### Exemplars link the two

An **exemplar** is a sample trace ID stored next to a histogram bucket. In Grafana you click a spike on the p99 graph and jump to a real trace from that spike, then to its logs through the same trace ID.

---

### Read more

- [[Observability - MOC]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Averaging percentiles is meaningless so aggregate response times by adding histograms]]
- [[Distributed tracing follows one request across services by sharing a trace ID]]
- [[Head sampling decides at the first service so it usually drops the rare failing trace]]
