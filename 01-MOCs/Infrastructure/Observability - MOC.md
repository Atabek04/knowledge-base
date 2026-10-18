> Monitor and debug distributed systems

---

## Progress

- [ ] Logging (SLF4J, ELK)
- [ ] Metrics (Prometheus, Grafana)
- [ ] Distributed tracing
- [ ] Alerting
- [ ] Performance profiling

---

## Topics

### The Three Pillars
- [ ] Monitoring vs observability: known unknowns vs unknown unknowns
- [ ] Logs: what happened
- [ ] Metrics: aggregated measurements
- [ ] Traces: request flow across services
- [ ] Why "three pillars" is criticised: wide structured events
- [ ] Correlating signals: exemplars link a metric to a trace, trace ID in every log line
- [ ] OpenTelemetry Collector as the vendor-neutral pipeline

### Logging

#### Basics
- [ ] Log levels (TRACE, DEBUG, INFO, WARN, ERROR)
- [ ] Structured logging (JSON)
- [ ] SLF4J and Logback
- [ ] Log context (MDC)
- [ ] Correlation IDs

#### Log Aggregation (ELK Stack)
- [ ] Elasticsearch
- [ ] Logstash / Fluentd
- [ ] Kibana
- [ ] Log parsing and indexing
- [ ] Log retention and rotation
- [ ] Grafana Loki as a label-indexed alternative to ELK

#### Logging pitfalls and anti-patterns
- [ ] Logging secrets and personal data
- [ ] Unstructured messages that cannot be queried
- [ ] Logging in hot loops: volume, cost, and latency
- [ ] Missing correlation ID, so one request cannot be followed across services
- [ ] Logging an exception at every layer it passes through

### Metrics

#### Fundamentals
- [ ] Metric types (Counter, Gauge, Histogram, Summary)
- [ ] Micrometer
- [ ] Spring Boot Actuator metrics
- [ ] Custom metrics

#### Prometheus & Grafana
- [ ] Prometheus architecture
- [ ] PromQL basics
- [ ] Scrape configuration
- [ ] Grafana dashboards
- [ ] Alert rules
- [ ] rate() vs irate() vs increase() on counters

#### What to measure: the methods
- [ ] Four golden signals: latency, traffic, errors, saturation
- [ ] RED method for services: rate, errors, duration
- [ ] USE method for resources: utilization, saturation, errors

#### Latency and percentiles
- [[Response time is what the client sees while latency is only the time a request spends waiting|Response time vs latency: client view vs waiting time]]
- [[Response time is a distribution so percentiles describe it and the mean does not|Percentiles: p50, p95, p99 describe a distribution, the mean does not]]
    - [[Averaging percentiles is meaningless so aggregate response times by adding histograms|Aggregating percentiles: add histograms, never average]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users|Tail latency: the slowest requests belong to the best users]]
- [[Tail latency amplification makes the user-visible p99 worse than any single service behind it|Tail amplification: fan-out makes the user p99 worse than any service]]
- [[Queueing delay is invisible to server-side metrics and to closed-loop load generators|Queueing delay: invisible to server metrics and closed-loop load tests]]
- [ ] Histogram bucket boundaries decide percentile accuracy in Prometheus
- [ ] Measure latency of successes and failures separately

#### What to measure per component
- [ ] HTTP and gRPC: request rate, error rate by status, latency percentiles per endpoint
- [ ] Database: query latency, reads and writes per second, slow queries, replication lag
- [ ] Connection pool: active, idle, pending, acquire wait time (HikariCP)
- [ ] Cache: hit ratio, misses, evictions, memory, latency
- [ ] Message queues: consumer lag, queue depth, processing time, dead-letter count
- [ ] Outbound calls: dependency latency, timeouts, retries, circuit breaker state
- [ ] JVM: heap, GC pause time, threads
- [ ] Host and network: CPU saturation, memory, disk I/O, TCP retransmits, DNS latency
- [ ] Business metrics: orders, sign-ups, payments per minute

#### Metrics pitfalls and anti-patterns
- [ ] High-cardinality labels (user ID, raw URL) explode Prometheus memory
- [ ] Averages hiding the tail
- [ ] Hit ratio without request volume: 99% of 10 requests means nothing
- [ ] Measuring causes (CPU) instead of user-facing symptoms
- [ ] Dashboards with no question behind them
- [ ] Coordinated omission in load tests

### Health Checks
- [[Kubernetes probes let the kubelet check container health the app reports|Probes: the app reports health, the kubelet checks and reacts]]
    - [[A failing liveness probe makes the kubelet restart the container|Liveness failure: the kubelet restarts the container]]
    - [[A failing readiness probe removes the pod from Service endpoints|Readiness failure: Pod leaves Service endpoints, no restart]]
    - [[A startup probe delays liveness and readiness checks until a slow app finishes booting|Startup probe: shields a slow boot from liveness restarts]]
    - [[Liveness probes must stay shallow while readiness probes can check dependencies|Probe depth: liveness shallow, readiness may check dependencies]]
    - [[Spring Boot Actuator exposes ready-made liveness and readiness probe groups|Actuator probe groups: liveness and readiness wired for free]]
- [[A newly launched instance needs warm-up before it can serve traffic|Warm-up: a new instance is not ready the moment it starts]]

#### Health check pitfalls and anti-patterns
- [ ] A shared dependency in readiness takes every pod out at once
- [ ] Liveness checking the database restarts healthy pods in a loop
- [ ] Timeouts and thresholds too tight for GC pauses
- [ ] Health endpoint exposing internals publicly
- [ ] External synthetic checks (blackbox exporter) catch what internal probes cannot

### Distributed Tracing

#### Concepts
- [ ] Spans and traces
- [ ] Trace context propagation
- [ ] Baggage propagation
- [ ] Sampling strategies
- [ ] Parent-child relationships

#### Tools
- [ ] OpenTelemetry
- [ ] Jaeger
- [ ] Zipkin
- [ ] Spring Cloud Sleuth / Micrometer Tracing
- [ ] Auto vs manual instrumentation
- [ ] Grafana Tempo

#### Tracing pitfalls and anti-patterns
- [ ] Context lost across async code, thread pools and message queues
- [ ] Head sampling drops the rare slow or failing trace; tail-based sampling
- [ ] Span per method: noise and cost
- [ ] Personal data in span attributes
- [ ] Instrumenting only some services, leaving gaps in the trace

### Alerting
- [ ] Alert rules
- [ ] Thresholds and SLOs
- [ ] Error budgets
- [ ] Alert fatigue
- [ ] Runbooks
- [ ] On-call practices
- [ ] SLIs, SLOs and SLAs
- [ ] Multi-window burn-rate alerts

#### Alerting pitfalls and anti-patterns
- [ ] Alerting on causes instead of symptoms
- [ ] Alerts with no action, so pages get ignored
- [ ] Static thresholds that fire on every traffic spike

### Performance

#### Profiling
- [ ] JVM profilers (VisualVM, JProfiler, async-profiler)
- [ ] Heap dumps
- [ ] Thread dumps
- [ ] Flame graphs

#### Load Testing
- [ ] JMeter basics
- [ ] Gatling
- [ ] Performance benchmarks
- [ ] Identifying bottlenecks

#### JVM Tuning
- [ ] Garbage collectors (G1, ZGC, Shenandoah)
- [ ] Heap sizing
- [ ] GC logs analysis
- [ ] Memory leaks detection
- [ ] JVM flags

---

## Russian Curriculum (Модуль 11)

### Наблюдаемость
- [ ] Логирование
- [ ] Метрики
- [ ] Трейсинг
- [ ] Алертинг
- [ ] Дашборды

---

## Project Tasks

**E-Commerce Stage 12, 15:**
- [ ] Add structured JSON logging
- [ ] Implement correlation ID propagation
- [ ] Set up Prometheus + Grafana
- [ ] Add custom business metrics
- [ ] Integrate distributed tracing
- [ ] Create monitoring dashboards
- [ ] Run load tests with JMeter
- [ ] Profile and optimize hot paths

---

## Reading List
- [ ] Cindy Sridharan, [Distributed Systems Observability](https://www.oreilly.com/library/view/distributed-systemsobservability/9781492033431/)
- [ ] Charity Majors, [Observability: a 3-year retrospective](https://thenewstack.io/observability-a-3-year-retrospective/)
- [ ] Majors, Fong-Jones, Miranda, [Observability Engineering](https://www.oreilly.com/library/view/observability-engineering/9781492076438/)
- [ ] Google SRE Book, [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [ ] Brendan Gregg, [The USE Method](https://www.brendangregg.com/usemethod.html)
- [ ] Tom Wilkie, [The RED Method](https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services/)
- [ ] Sigelman et al., [Dapper](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)
- [ ] Rob Ewaschuk, [My Philosophy on Alerting](https://docs.google.com/document/d/199PqyG3UsyXlwieHaqbGiWVa8eMWi8zzAn0YfcApr8Q)

---

## Related
- [[Kubernetes - MOC]]
- [[Microservices Patterns - MOC]]
- [[DevOps - MOC]]
- [[System Design - MOC]]
