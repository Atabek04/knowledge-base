> Patterns for reliable microservices

---

## Progress

- [ ] Resilience patterns
- [ ] Distributed transactions (Saga)
- [ ] Data patterns (Outbox, CQRS)
- [ ] Communication patterns
- [ ] Deployment patterns

---

## Topics

### Resilience Patterns

#### Circuit Breaker
- [ ] Closed, Open, Half-Open states
- [ ] Failure thresholds
- [ ] Timeout configuration
- [ ] Resilience4j implementation

#### Retry
- [ ] Retry strategies
- [ ] Exponential backoff
- [ ] Jitter
- [ ] Idempotency requirements
- [ ] Resilience4j Retry

#### Bulkhead
- [ ] Thread pool isolation
- [ ] Semaphore isolation
- [ ] Resource limits
- [ ] Resilience4j Bulkhead

#### Rate Limiting
- [ ] Token bucket
- [ ] Leaky bucket
- [ ] Fixed window
- [ ] Sliding window
- [ ] Resilience4j RateLimiter

#### Timeout
- [ ] Connection timeout
- [ ] Read timeout
- [ ] Overall timeout
- [ ] Timeout propagation

### Distributed Transaction Patterns

#### Saga Pattern
- [ ] Choreography Saga
- [ ] Orchestration Saga
- [ ] Compensating transactions
- [ ] Saga state management
- [ ] Error handling in sagas

#### Two-Phase Commit (2PC)
- [ ] Prepare phase
- [ ] Commit phase
- [ ] Coordinator failure
- [ ] Why it's often avoided

### Data Patterns

#### Outbox Pattern
- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction|Outbox: write event in the same transaction]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots|Debezium streams Postgres WAL to Kafka (LSN, slots)]]
- [[Outbox over Debezium eliminates polling overhead while preserving business event contracts|Outbox over Debezium drops polling, keeps event contracts]]
- [[Open-source CDC tools differ in database support, Kafka coupling, and operational overhead|CDC tools differ in DB support, Kafka coupling, ops]]

#### Inbox Pattern
- [ ] Idempotent consumers
- [ ] Message deduplication
- [ ] At-least-once + idempotency = exactly-once

#### CQRS
- [ ] Command Query Responsibility Segregation
- [ ] Separate read/write models
- [ ] Event sourcing with CQRS
- [ ] When to use CQRS

#### Event Sourcing
- [ ] Events as source of truth
- [ ] Event store
- [ ] Rebuilding state
- [ ] Snapshots

### Service Discovery
- [ ] Client-side discovery
- [ ] Server-side discovery
- [ ] Service registry (Eureka, Consul)
- [ ] Health checks

### API Gateway
- [ ] Routing
- [ ] Authentication
- [ ] Rate limiting
- [ ] Request aggregation
- [ ] Spring Cloud Gateway

### Database per Service
- [ ] Data isolation
- [ ] Joining across services
- [ ] Data consistency challenges
- [ ] Shared database anti-pattern

### Migration & Deployment Patterns
- [ ] Sidecar pattern
- [ ] Strangler Fig — incremental monolith migration
- [ ] Anti-Corruption Layer

---

## Russian Curriculum (Модуль 8)

### Паттерны надёжности
- [ ] Circuit Breaker
- [ ] Retry
- [ ] Timeout
- [ ] Bulkhead
- [ ] Saga pattern
- [ ] Outbox pattern
- [ ] CQRS

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Microservices Patterns** — Chris Richardson | 🔴 Critical | ⏳ |

---

## Project Tasks

**E-Commerce Stage 10-11:**
- [ ] Implement Payment Service
- [ ] Implement Saga for order + payment
- [ ] Add Outbox pattern for reliable messaging
- [ ] Implement Circuit Breaker with Resilience4j
- [ ] Add retry with exponential backoff
- [ ] Implement bulkhead isolation

---

## Related
- [[Distributed Systems - MOC]]
- [[Architecture - MOC]]
- [[Observability - MOC]]
