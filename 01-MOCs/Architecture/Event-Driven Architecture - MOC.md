> Services that communicate by publishing and reacting to events, with event sourcing as the storage model

In an ordinary call, service A asks service B to do something and waits for the answer. A knows B exists, and if B is down, A fails too.

<mark style="background: #FFF3A3A6;">In event-driven architecture, a service announces a fact that already happened ("OrderPlaced") to a broker, and any service that cares reacts to it later.</mark> The producer does not know who listens, does not wait, and keeps working when a consumer is down.

The price is that the flow is no longer visible in one place, and other services see the change a moment later, not instantly (eventual consistency).

Roadmap order: foundations, then messaging guarantees, then the four meanings of "event-driven", then the patterns that make them reliable, then operations.

---

## Foundations

- [ ] Events vs commands vs queries
- [ ] Synchronous vs asynchronous communication: temporal coupling
- [ ] Event notification: tell others something happened, expect no reply
- [ ] Event-carried state transfer: the event carries the data consumers need
- [ ] Domain events vs integration events
- [ ] Event storming: discovering events with domain experts

## Messaging and Brokers

- [ ] Message queue (point-to-point) vs publish/subscribe
- [ ] Traditional brokers (RabbitMQ, JMS) vs log-based brokers (Kafka)
- [ ] Partitions, ordering guarantees and partition keys
- [ ] Consumer groups and offsets
- [ ] Delivery semantics: at-most-once, at-least-once, exactly-once
    - [[Kafka delivers messages at-least-once by default and exactly-once with atomic offset commits|Kafka: at-least-once default, exactly-once via atomic commits]]
- [ ] Dead letter queues and retry topics
- [ ] Backpressure and consumer lag
- [ ] Log compaction: the topic as a durable table

## Event Design and Schemas

- [ ] Event granularity: thin (notification) vs fat (state) events
- [ ] Event naming and envelope (id, type, timestamp, correlation id)
- [[Distributed Systems - MOC#Data Encoding and Schema Evolution|Encoding and schema evolution: JSON, Avro, Protobuf, registry]]
- [ ] Event versioning: new field, new event type, or upcast
- [ ] Events as public contracts between teams

## Event Sourcing

- [ ] Event sourcing: the event log is the source of truth
- [ ] Event store and append-only streams
- [ ] Rebuilding state by replaying events
- [ ] Aggregates as consistency boundaries
- [ ] Snapshots to shorten replay
- [ ] Projections and read models
- [ ] Upcasting old events to the latest version
- [ ] Never edit a past event: record a correcting fact instead
- [ ] Optimistic concurrency on a stream (expected version)
- [ ] GDPR and deletion in an immutable log (crypto-shredding)
- [ ] When event sourcing is the wrong choice

## CQRS

- [ ] CQRS: separate write model and read model
- [ ] Event sourcing with CQRS
- [ ] Read-your-own-writes on eventually consistent read models
- [ ] When CQRS is worth its cost

## Reliability Patterns

- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction|Outbox: DB write and event in one transaction]]
- [ ] Dual-write problem: why "save then publish" loses events
- [ ] Inbox pattern and idempotent consumers
    - [[Idempotency key prevents duplicate processing when clients retry failed requests|Idempotency key: retries never double-process]]
- [ ] Change data capture as an event source
    - [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots|Debezium streams Postgres WAL to Kafka (LSN, slots)]]
    - [[Outbox over Debezium eliminates polling overhead while preserving business event contracts|Outbox over Debezium drops polling, keeps event contracts]]
- [ ] Poison messages and error handling strategies

## Workflows Across Services

- [ ] Choreography vs orchestration
- [ ] Saga pattern: local transactions plus compensations
- [ ] Process manager and state machines
- [ ] Eventual consistency and how users experience it
    - [[Eventual consistency lets replicas accept writes during a partition and converge afterward|Eventual consistency: replicas converge after a partition]]

## Stream Processing

- [ ] Streams vs tables duality
- [ ] Kafka Streams and Flink basics
- [ ] Event time vs processing time, watermarks
- [ ] Windows: tumbling, hopping, sliding, session
- [ ] Stream joins: stream-stream, stream-table
- [ ] Kappa vs Lambda architecture

## Operations and Testing

- [ ] Distributed tracing across async hops (correlation and causation ids)
- [ ] Observability: consumer lag, DLQ size, end-to-end latency
- [ ] Replaying and reprocessing events safely
- [ ] Contract testing for events
- [ ] Testing event-sourced aggregates (given events, when command, then events)
- [ ] Common EDA failure modes: event chains nobody can follow, hidden coupling

---

## Sources

- Martin Fowler, [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html) (2017): the four patterns
- Adam Bellemare, [Building Event-Driven Microservices](https://oreilly.com/library/view/building-event-driven-microservices/9781492057888), O'Reilly (2020, 2nd ed. from Confluent)
- Greg Young, [Versioning in an Event Sourced System](https://leanpub.com/esversioning), Leanpub
- Martin Kleppmann, Designing Data-Intensive Applications, Ch. 11 (see [[DDIA - MOC]])
- Chris Richardson, Microservices Patterns, Manning (2018): saga, outbox, event sourcing, CQRS
- Gregor Hohpe, Bobby Woolf, Enterprise Integration Patterns (2003): messaging vocabulary
- Ben Stopford, Designing Event-Driven Systems, O'Reilly/Confluent (2018)

### Read more

- [[Distributed Systems - MOC]]
- [[Microservices Patterns - MOC]]
- [[DDIA - MOC]]
