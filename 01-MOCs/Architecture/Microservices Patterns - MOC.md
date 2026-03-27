# Microservices Patterns — MOC

> **Phase 8** of [[00 - IT Career - MOC]]
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
- [ ] Transactional outbox
- [ ] Polling publisher
- [ ] Transaction log tailing
- [ ] Debezium (CDC)

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
- [[00 - IT Career - MOC]]
