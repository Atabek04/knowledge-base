> Understand distributed computing fundamentals

---

## Progress

- [ ] CAP theorem
- [ ] Consistency models
- [ ] Message queues (Kafka, RabbitMQ)
- [ ] Event-driven architecture
- [ ] Service mesh basics

---

## Topics

### Fundamentals
- [ ] What makes a system distributed
- [ ] Fallacies of distributed computing
- [ ] Network partitions
- [ ] Latency and timeouts
- [ ] Clocks and ordering
- [ ] BASE vs ACID
- [ ] Idempotency keys

### CAP Theorem & PACELC
- [[CAP theorem forces a partitioned system to choose between consistency and availability|CAP: pick C or A under partition (CP vs AP, PACELC)]]
- [[Eventual consistency lets replicas accept writes during a partition and converge afterward|Eventual consistency: replicas converge after a partition]]
- [ ] Trade-off decisions

### Consistency Models
- [ ] Strong consistency
- [ ] Eventual consistency
- [ ] Causal consistency
- [ ] Read-your-writes consistency
- [ ] Linearizability vs Serializability

### Consensus
- [ ] The consensus problem
- [ ] Paxos (conceptual)
- [ ] Raft (conceptual)
- [ ] Leader election
- [ ] Split-brain problem

### Message Queues

#### Apache Kafka
- [ ] Topics, partitions, offsets
- [ ] Producers and consumers
- [ ] Consumer groups
- [ ] Replication and durability
- [ ] Producer acks, idempotent producer, batching
- [ ] Consumer rebalancing & partition assignment strategies
- [[Kafka delivers messages at-least-once by default and exactly-once with atomic offset commits|Kafka: at-least-once default, exactly-once with atomic offsets]]
- [ ] Kafka Streams basics
- [ ] Schema Registry (Avro, Protobuf)
- [ ] Dead Letter Queue (DLQ) pattern
- [ ] Compacted topics

#### RabbitMQ
- [ ] Exchanges, queues, bindings
- [ ] Exchange types (direct, fanout, topic)
- [ ] Acknowledgments
- [ ] Dead letter queues
- [ ] Message TTL

#### Apache Pulsar
- [ ] Topics, tenants, namespaces
- [ ] Pulsar vs Kafka — when each fits

### Event-Driven Architecture
- [ ] Events vs Commands vs Queries
- [ ] Event sourcing basics
- [ ] Event store
- [ ] Eventual consistency patterns
- [ ] Choreography vs Orchestration

### Service Communication
- [ ] Synchronous vs Asynchronous
- [ ] Request-Reply pattern
- [ ] Publish-Subscribe pattern
- [ ] Message formats (JSON, Protobuf, Avro)
- [ ] API versioning in distributed systems

---

## Russian Curriculum (Модуль 5)

### Распределённые системы
- [ ] CAP теорема
- [ ] Консистентность
- [ ] Консенсус
- [ ] Распределённые транзакции

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Designing Data-Intensive Applications** — Kleppmann | 🔴 Critical | ⏳ |

---

## Project Tasks

**E-Commerce Stage 6:**
- [ ] Add Kafka for order events
- [ ] Implement order notification via Kafka consumer
- [ ] Handle message delivery guarantees
- [ ] Implement dead letter handling

---

## Related
- [[Microservices Patterns - MOC]]
- [[Architecture - MOC]]
- [[Databases - MOC]]
