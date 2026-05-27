---
aliases: [Java Kotlin Roadmap, Senior Dev Roadmap, IT Career Roadmap]
tags: [MOC, roadmap, java, kotlin, career]
---

# Senior Java/Kotlin Developer Roadmap

> **Goal:** Senior Java Developer → Remote Work → Family Provision
> **Study Time:** Office hours (08:00–17:30) when AI handles routine tasks
> **Resources:** Books + Documentation only (no video dependencies)

Career roadmap based on real job market requirements (2025–2026). Each bullet = future atomic note.

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

## Project: E-Commerce Platform

Single project that evolves from CRUD monolith to full microservices.

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

---

## Documentation Resources

- [Java SE Documentation](https://docs.oracle.com/en/java/)
- [Spring Framework](https://docs.spring.io/spring-framework/reference/)
- [Spring Boot](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Kotlin](https://kotlinlang.org/docs/home.html)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Redis](https://redis.io/docs/)
- [Docker](https://docs.docker.com/)
- [Kubernetes](https://kubernetes.io/docs/)
- [Kafka](https://kafka.apache.org/documentation/)
- [roadmap.sh/java](https://roadmap.sh/java) · [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot) · [roadmap.sh/backend](https://roadmap.sh/backend)
- [Baeldung Java](https://www.baeldung.com/java-tutorial) · [Baeldung Spring](https://www.baeldung.com/spring-tutorial)

---

## Java Core (Deep Mastery)

### Collections & Data Structures
- Java Collections framework internals (ArrayList, LinkedList, HashMap, TreeMap)
- Generics and type erasure
- Streams API and functional operations
- Optional — correct usage and anti-patterns
- Comparator and Comparable

### JVM Internals
- JVM memory model (heap, stack, metaspace, off-heap)
- Garbage collection algorithms (G1, ZGC, Shenandoah)
- GC tuning and JVM flags
- JIT compilation and HotSpot optimization
- Class loading mechanism

### Java Modern Features
- Records (Java 16+)
- Sealed classes (Java 17+)
- Pattern matching for instanceof and switch
- Text blocks
- Virtual threads — Project Loom (Java 21)
- Structured concurrency (Java 21)

---

## Concurrency & Multithreading

### Fundamentals
- Thread lifecycle and states
- `synchronized` keyword and intrinsic locks
- `volatile` — visibility guarantee, not atomicity
- Memory visibility and happens-before relationship
- Deadlock, livelock, starvation — detection and prevention

### Java Concurrency API
- `ExecutorService` and thread pools
- `ForkJoinPool` and work-stealing algorithm
- `CompletableFuture` — async pipelines and composition
- `CountDownLatch`, `CyclicBarrier`, `Semaphore`, `Phaser`
- `ConcurrentHashMap`, `CopyOnWriteArrayList`, `BlockingQueue`
- `ReentrantLock`, `ReadWriteLock`, `StampedLock`
- Atomic classes (`AtomicInteger`, `AtomicReference`, `LongAdder`)

### Advanced Concurrency
- Lock-free data structures and CAS operations
- `ThreadLocal` — use cases and memory leak risks
- Virtual threads vs platform threads (Project Loom)
- Reactive programming with Project Reactor / WebFlux

---

## Kotlin

### Language Fundamentals
- Null safety — `?.`, `!!`, `?:`, safe casts
- Data classes, sealed classes, value classes
- Extension functions and properties
- Higher-order functions and lambdas
- Operator overloading
- Delegation (`by` keyword)
- Kotlin DSL construction

### Coroutines
- `suspend` functions — what they compile to
- `CoroutineScope`, `CoroutineContext`, `Job`
- Builders: `launch`, `async`, `runBlocking`
- Dispatchers — `IO`, `Default`, `Main`, `Unconfined`
- Structured concurrency in Kotlin
- `Flow` — cold streams, operators, collection
- `StateFlow` and `SharedFlow`
- Exception handling in coroutines
- Coroutines vs virtual threads — when to use each

### Kotlin + Build
- Gradle with Kotlin DSL
- Kotlin interop with Java — nullability annotations, platform types

---

## Spring Ecosystem

### Spring Core
- IoC container — bean lifecycle, scopes
- Dependency injection — constructor vs field vs setter
- `@Configuration` and `@Bean` factories
- Profiles and conditional beans
- Spring AOP — aspects, pointcuts, advice types

### Spring Boot
- Auto-configuration mechanism
- Actuator — health, metrics, custom endpoints
- `@ConfigurationProperties` — type-safe config binding
- Embedded server configuration (Tomcat, Netty)
- Spring Boot with virtual threads (3.2+)

### Spring Data
- JPA and Hibernate — entity lifecycle, lazy vs eager loading
- N+1 problem — detection and solutions
- Spring Data repositories — custom queries, projections
- Transactions — propagation, isolation levels, `@Transactional` pitfalls
- Flyway and Liquibase — schema migration management

### Spring Security
- Authentication vs authorization
- OAuth2 / OIDC — resource server, authorization server
- JWT — validation, claims, refresh token flow
- Method-level security (`@PreAuthorize`, `@Secured`)
- mTLS for service-to-service auth

### Spring WebFlux (Reactive)
- Reactive Streams spec — Publisher, Subscriber, Subscription
- `Mono` and `Flux` — operators and composition
- Non-blocking I/O — when it helps and when it doesn't
- WebClient vs RestTemplate vs RestClient (Spring 6)
- Backpressure handling

---

## API Design & Protocols

### REST
- REST constraints and Richardson Maturity Model
- API versioning strategies
- Idempotency — design and implementation
- Rate limiting — token bucket, sliding window
- HATEOAS
- OpenAPI 3 / Swagger — documentation standards

### gRPC
- Protocol Buffers — schema definition, field numbering
- Service types — unary, server streaming, client streaming, bidirectional
- gRPC vs REST — when to choose each
- gRPC with Spring Boot — `grpc-spring-boot-starter`
- Deadlines, retries, and interceptors in gRPC
- gRPC health checks and reflection

### GraphQL
- Schema-first vs code-first approach
- Queries, mutations, subscriptions
- DataLoader — N+1 problem in GraphQL
- Spring for GraphQL

---

## Messaging & Event-Driven Architecture

### Apache Kafka
- Core concepts — topics, partitions, offsets, consumer groups
- Producers — acknowledgment levels, idempotency, batching
- Consumers — rebalancing, partition assignment strategies
- Exactly-once semantics (EOS) — transactions
- Dead letter queue (DLQ) pattern
- Schema Registry with Avro / Protobuf
- Kafka Streams — stateful stream processing
- Compacted topics — use cases

### Messaging Patterns
- At-least-once vs at-most-once vs exactly-once delivery
- Outbox pattern — guaranteed message delivery
- CQRS — Command Query Responsibility Segregation
- Event Sourcing — event store, projections, snapshots
- Saga pattern — choreography vs orchestration
- Change Data Capture (CDC) with Debezium

### Other Message Brokers
- RabbitMQ — exchanges, queues, routing keys, bindings
- AWS SQS / SNS — queue vs pub-sub
- Apache Pulsar — topics, tenants, namespaces

---

## Design Patterns

### SOLID Principles
- Single Responsibility — one reason to change
- Open/Closed — extend without modifying
- Liskov Substitution — subtypes must be substitutable
- Interface Segregation — lean interfaces
- Dependency Inversion — depend on abstractions

### GoF Creational Patterns
- Singleton — thread-safe implementations
- Factory Method — defer instantiation to subclasses
- Abstract Factory — families of related objects
- Builder — complex object construction
- Prototype — cloning objects

### GoF Structural Patterns
- Adapter — incompatible interfaces
- Decorator — dynamic behavior extension
- Proxy — controlled access (lazy init, logging, auth)
- Facade — simplified interface to subsystem
- Composite — tree structures

### GoF Behavioral Patterns
- Strategy — interchangeable algorithms
- Observer — event notification
- Template Method — skeleton algorithm in base class
- Command — encapsulate operations as objects
- Chain of Responsibility — handler pipeline
- State — behavior by state machine

---

## Architecture & Microservices

### Architectural Patterns
- Layered architecture — controller → service → repository
- Hexagonal architecture (Ports & Adapters)
- Clean Architecture — dependency rule
- Domain-Driven Design (DDD) — entities, aggregates, value objects, repositories, bounded contexts, ubiquitous language

### Microservice Patterns
- API Gateway — routing, auth, rate limiting
- Service discovery — client-side vs server-side (Eureka, Consul)
- Circuit Breaker — Resilience4j (closed, open, half-open states)
- Bulkhead — isolate failures
- Retry with exponential backoff and jitter
- Sidecar pattern
- Strangler Fig — monolith migration strategy
- Anti-Corruption Layer

### Distributed Systems Fundamentals
- CAP theorem — consistency, availability, partition tolerance
- BASE vs ACID
- Eventual consistency
- Distributed transactions — 2PC, Saga
- Idempotency keys
- Distributed tracing — trace ID, span ID propagation

---

## Databases

### SQL & PostgreSQL
- EXPLAIN ANALYZE — reading query plans
- Index types — B-tree, Hash, GIN, GiST, partial indexes
- Query optimization — covering indexes, index-only scans
- Window functions
- CTEs — recursive and non-recursive
- Locking — row-level, table-level, advisory locks
- MVCC — how PostgreSQL handles concurrent reads/writes
- Connection pooling — PgBouncer

### NoSQL
- Redis — data structures, TTL, pub/sub, Lua scripts, Redis Cluster
- MongoDB — documents, indexes, aggregation pipeline
- Cassandra — partition key, clustering key, consistency levels, read repair
- DynamoDB — partition key design, GSI, LSI, DynamoDB Streams

---

## Testing

### Unit Testing
- JUnit 5 — `@Test`, `@ParameterizedTest`, `@ExtendWith`, lifecycle methods
- Mockito — `@Mock`, `@InjectMocks`, `verify`, `ArgumentCaptor`
- AssertJ — fluent assertions, custom assertions
- TDD workflow — red-green-refactor

### Integration Testing
- `@SpringBootTest` — full context vs slice tests
- `@WebMvcTest`, `@DataJpaTest`, `@JsonTest` — slice testing
- Testcontainers — PostgreSQL, Kafka, Redis in tests
- `MockMvc` — HTTP layer testing without server
- `WebTestClient` — reactive HTTP testing

### Contract Testing
- Consumer-Driven Contract Testing — concept
- Pact — consumer test, pact file, provider verification
- Spring Cloud Contract — Groovy/YAML DSL, stub generation

### Performance Testing
- Gatling — simulation scripts, scenarios, feeders
- JMeter — test plans, thread groups, assertions
- Profiling with JFR (Java Flight Recorder) and JMC
- Heap dump analysis

### Test Design
- AAA pattern — Arrange, Act, Assert
- Test pyramid — unit vs integration vs E2E ratio
- Test doubles — mock vs stub vs spy vs fake vs dummy
- Property-based testing — jqwik

---

## Observability

### Logging
- SLF4J + Logback / Log4j2 — structured logging
- MDC — correlation ID propagation across threads
- Log levels — correct usage in production
- ELK stack — Elasticsearch, Logstash, Kibana

### Metrics
- Micrometer — meter types (counter, gauge, timer, distribution summary)
- Prometheus — scraping, PromQL, alerting rules
- Grafana — dashboards, panels, alerting
- SLOs and error budgets

### Distributed Tracing
- OpenTelemetry — traces, spans, baggage, context propagation
- Jaeger / Zipkin — trace visualization
- Auto-instrumentation vs manual instrumentation

---

## Cloud & Infrastructure

### AWS Core Services
- Compute — EC2, ECS, Fargate, Lambda
- Storage — S3, EBS, EFS
- Database — RDS, Aurora, DynamoDB, ElastiCache
- Networking — VPC, subnets, security groups, ALB/NLB
- Messaging — SQS, SNS, EventBridge
- Secrets Manager, Parameter Store

### Docker & Kubernetes
- Docker — image layers, multi-stage builds, best practices
- Docker Compose — local development
- Kubernetes — Pod, Deployment, Service, Ingress, ConfigMap, Secret
- Kubernetes — resource requests/limits, HPA, rolling updates
- Helm — charts, values, templating
- Kubectl — essential commands

### Infrastructure as Code
- Terraform — providers, resources, state, modules
- CI/CD pipelines — GitHub Actions, GitLab CI

### Deployment Strategies
- Blue-green deployment
- Canary deployment
- Feature flags — LaunchDarkly, Unleash
- Rolling updates

---

## Security

### Authentication & Authorization
- OAuth2 flows — authorization code, client credentials, device flow
- OIDC — ID token, UserInfo endpoint
- JWT — structure, validation, refresh token rotation
- RBAC vs ABAC
- Session management — stateful vs stateless

### Application Security
- OWASP Top 10 — injection, broken auth, XSS, IDOR, etc.
- Input validation and sanitization
- SQL injection prevention — parameterized queries
- Secret management — never in code or env vars in prod
- HashiCorp Vault — secret engines, dynamic secrets

---

## Soft Skills & Leadership

- Mentoring junior and mid developers
- Architecture Decision Records (ADR)
- Code review — giving and receiving feedback
- Technical documentation — C4 diagrams, Confluence
- Agile / Scrum — ceremonies, estimation, backlog refinement
- Decomposing complex systems — RFC process
- Stakeholder communication — translating tech to business

---

## Read more

- [[Java MOC]]
- [[Kotlin MOC]]
