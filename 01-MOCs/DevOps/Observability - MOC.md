# Observability — MOC

> **Phase 9** of [[00 - IT Career - MOC]]
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
- [ ] Logs — what happened
- [ ] Metrics — aggregated measurements
- [ ] Traces — request flow across services

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

### Distributed Tracing

#### Concepts
- [ ] Spans and traces
- [ ] Trace context propagation
- [ ] Sampling strategies
- [ ] Parent-child relationships

#### Tools
- [ ] OpenTelemetry
- [ ] Jaeger
- [ ] Zipkin
- [ ] Spring Cloud Sleuth / Micrometer Tracing

### Alerting
- [ ] Alert rules
- [ ] Thresholds and SLOs
- [ ] Alert fatigue
- [ ] Runbooks
- [ ] On-call practices

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

## Related
- [[Microservices Patterns - MOC]]
- [[DevOps - MOC]]
- [[System Design - MOC]]
- [[00 - IT Career - MOC]]
