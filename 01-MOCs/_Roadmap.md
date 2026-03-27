# IT Career — Senior Java Backend Developer

> **Goal:** Senior Java Developer → Remote Work → Family Provision
> **Study Time:** Office hours (8:00-17:30) when AI handles routine tasks
> **Resources:** Books + Documentation only (no video dependencies)

---

## Current Phase

| Phase | Status | Focus |
|-------|--------|-------|
| **Phase 1** | 🔄 Active | Core Java Mastery |
| Phase 2 | ⏳ Pending | Concurrency & Testing |
| Phase 3 | ⏳ Pending | Databases & Persistence |
| Phase 4 | ⏳ Pending | Spring Ecosystem |
| Phase 5 | ⏳ Pending | Kotlin |
| Phase 6 | ⏳ Pending | DevOps & Infrastructure |
| Phase 7 | ⏳ Pending | Architecture |
| Phase 8 | ⏳ Pending | Distributed Systems & Microservices |
| Phase 9 | ⏳ Pending | Observability & Advanced |
| Phase 10 | ⏳ Pending | System Design Practice |

---

## Learning Path MOCs

### Core Skills
- [[Java Core - MOC]] — Fundamentals, OOP, Generics, Streams, Java 17+/21+
- [[Java Concurrency - MOC]] — Multithreading, java.util.concurrent, thread safety
- [[Design Patterns - MOC]] — GoF patterns, enterprise patterns
- [[Testing - MOC]] — JUnit, Mockito, TDD, integration testing

### Data Layer
- [[Databases - MOC]] — SQL, PostgreSQL, NoSQL, Redis, transactions

### Frameworks
- [[Spring Ecosystem - MOC]] — Core, Boot, Data, Security, Web
- [[Kotlin - MOC]] — Syntax, coroutines, Spring integration

### API & Communication
- [[API Design - MOC]] — REST, gRPC, GraphQL, documentation

### Infrastructure
- [[DevOps - MOC]] — Git, Linux, Docker, Kubernetes, CI/CD

### Architecture & Scale
- [[Architecture - MOC]] — Monolith, modular monolith, microservices, DDD
- [[Distributed Systems - MOC]] — CAP, consistency, messaging, event-driven
- [[Microservices Patterns - MOC]] — Resilience, Saga, Outbox, CQRS
- [[Observability - MOC]] — Logging, metrics, tracing, OpenTelemetry

### Practice
- [[System Design - MOC]] — NFRs, scaling, high availability, design problems
- [[Technical Books - MOC]] — Reading list with priorities

---

## Project: E-Commerce Platform

Single project that evolves from CRUD monolith to full microservices.

### Domain Entities
- Users (customers, admins)
- Products (catalog, categories, inventory)
- Orders (cart, checkout, order history)
- Payments (payment processing, refunds)
- Notifications (email, SMS)
- Reviews & Ratings

### Evolution Tracker

| Stage | Description | Skills | Status |
|-------|-------------|--------|--------|
| 1 | Product catalog CRUD | Spring Boot, JPA, REST | ⏳ |
| 2 | Validation, error handling, logging | Bean Validation, SLF4J | ⏳ |
| 3 | User registration + JWT auth | Spring Security, JWT | ⏳ |
| 4 | Shopping Cart + Orders | Business logic, transactions | ⏳ |
| 5 | Product caching (Redis) | Redis, caching strategies | ⏳ |
| 6 | Async order notifications | Kafka/RabbitMQ | ⏳ |
| 7 | Containerize with Docker | Docker, Docker Compose | ⏳ |
| 8 | Split into microservices | Service decomposition | ⏳ |
| 9 | Service Discovery + API Gateway | Spring Cloud, Eureka | ⏳ |
| 10 | Payment Service + Saga | Distributed transactions | ⏳ |
| 11 | Resilience patterns | Resilience4j | ⏳ |
| 12 | Observability stack | Prometheus, Grafana, Jaeger | ⏳ |
| 13 | Kubernetes deployment | K8s, Helm charts | ⏳ |
| 14 | Inventory sharding | Database scaling | ⏳ |
| 15 | Load testing + optimization | JMeter, profiling, JVM tuning | ⏳ |

### Final Architecture
```
┌─────────────────┐
│   API Gateway   │
└────────┬────────┘
         │
    ┌────┴────┬────────┬──────────┐
    ▼         ▼        ▼          ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌──────────┐
│ User  │ │Product│ │ Order │ │ Payment  │
│Service│ │Service│ │Service│ │ Service  │
└───┬───┘ └───┬───┘ └───┬───┘ └────┬─────┘
    │         │        │           │
    ▼         ▼        ▼           ▼
  [DB]      [DB]     [DB]        [DB]
              │        │
              └───┬────┘
                  ▼
              [Kafka]
                  │
                  ▼
         ┌──────────────┐
         │ Notification │
         │   Service    │
         └──────────────┘
```

---

## Documentation Resources

### Official Docs
- [Java SE Documentation](https://docs.oracle.com/en/java/)
- [Spring Framework](https://docs.spring.io/spring-framework/reference/)
- [Spring Boot](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Kotlin](https://kotlinlang.org/docs/home.html)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Redis](https://redis.io/docs/)
- [Docker](https://docs.docker.com/)
- [Kubernetes](https://kubernetes.io/docs/)
- [Kafka](https://kafka.apache.org/documentation/)

### Roadmaps
- [roadmap.sh/java](https://roadmap.sh/java)
- [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot)
- [roadmap.sh/backend](https://roadmap.sh/backend)
- [roadmap.sh/system-design](https://roadmap.sh/system-design)

### Guides (Text-based)
- [Baeldung Java](https://www.baeldung.com/java-tutorial)
- [Baeldung Spring](https://www.baeldung.com/spring-tutorial)

---

## Related
- [[Long-Term-Vision]]
- [[2026-Yearly-Goals]]
