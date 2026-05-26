# System Design — MOC

> **Phase 10** of [[00 - IT Career - MOC]]
> Design scalable, reliable systems

---

## Progress

- [ ] NFRs analysis
- [ ] Scaling patterns
- [ ] High availability
- [ ] Design exercises
- [ ] Architecture Decision Records

---

## Topics

### Non-Functional Requirements (NFRs)
- [ ] Performance (latency, throughput)
- [ ] Scalability (vertical, horizontal)
- [ ] Availability (uptime, SLA/SLO)
- [ ] Reliability (MTBF, MTTR)
- [ ] Durability (data persistence)
- [ ] Consistency requirements
- [ ] Security requirements
- [ ] Cost constraints

### Capacity Planning
- [ ] Traffic estimation
- [ ] Storage estimation
- [ ] Bandwidth estimation
- [ ] QPS calculations
- [ ] Read/write ratios

### Scaling Strategies

#### Database Scaling
- [ ] Vertical scaling
- [ ] Read replicas
- [ ] Sharding strategies
- [ ] Consistent hashing
- [ ] Denormalization
- [ ] Hot partition problem — bad partition key choice → uneven load
- [ ] Avoiding JOINs at scale — denormalization tradeoffs in read-heavy systems

#### Application Scaling
- [ ] Stateless services
- [ ] Horizontal scaling
- [ ] Load balancing
- [ ] Auto-scaling

### High Availability
- [ ] Redundancy
- [ ] Failover mechanisms
- [ ] Active-passive vs Active-active
- [ ] Multi-region deployment
- [ ] Disaster recovery
- [ ] RTO and RPO

### Caching
- [ ] Cache-aside pattern
- [ ] Write-through, write-behind
- [ ] Cache invalidation
- [ ] Cache stampede prevention
- [ ] CDN caching
- [ ] Hot key problem — single key overwhelms one shard, mitigation strategies
- [ ] TTL jitter — randomizing expiry to prevent synchronized stampede
- [ ] Multi-level caching — L1 local + L2 Redis + CDN layers

### Async Processing
- [ ] Message queues
- [ ] Task queues
- [ ] Background jobs
- [ ] Batch processing
- [ ] Fanout patterns — fan-out-on-write vs fan-out-on-read (celebrity problem)
- [ ] Event ordering guarantees — Kafka partition keys, sequence numbers
- [ ] Exactly-once semantics — offset management, idempotent consumers
- [ ] Out-of-order event handling — watermarks, sequence-based reordering

### Distributed Transactions
- [ ] Idempotency keys — why every mutation needs one, how to store them
- [ ] Saga pattern — choreography vs orchestration
- [ ] Compensation workflows — how to undo a half-completed transaction
- [ ] Distributed locking — Redis SETNX, optimistic vs pessimistic locking
- [ ] Two-phase commit (2PC) — why it's rarely used in modern systems

### Reliability & Resilience
- [ ] Circuit breakers — open/half-open/closed states, when to trip
- [ ] Bulkhead pattern — isolating failures so one service can't sink the platform
- [ ] Timeout strategies — fail fast vs wait, cascading timeout risk
- [ ] Retry storms — exponential backoff + jitter to avoid thundering herd
- [ ] Load shedding — controlled degradation under extreme load
- [ ] Backpressure — upstream flow control when consumers lag producers

### AI System Design
- [ ] RAG architecture — retrieval-augmented generation, when and why
- [ ] Vector databases — ANN search, HNSW, recall vs latency tradeoffs
- [ ] LLM cost control — prompt caching, token budgets, model routing
- [ ] Hallucination mitigation — grounding, citations, confidence thresholds
- [ ] Semantic search latency — embedding optimization, approximate vs exact search

### Geospatial Indexing
- [ ] "Find X near me" problem — why naive 2D distance scans don't scale
- [ ] Geohash — encoding 2D coordinates into a 1D string
- [ ] Shared prefix → shared geography (proximity property)
- [ ] Reusing B-tree index for spatial queries via geohash prefix
- [ ] Geohash precision levels and cell sizes
- [ ] Edge cases — boundary cells, neighbor lookup
- [ ] Alternatives — quadtree, R-tree, S2, H3

### System Design Process
1. Requirements clarification
2. Capacity estimation
3. High-level design
4. Component deep dive
5. Bottleneck identification
6. Trade-off discussion

### Design Problems Practice

#### Social Network
- [ ] User profiles and connections
- [ ] News feed generation
- [ ] Real-time notifications
- [ ] Message system

#### E-Commerce
- [ ] Product catalog
- [ ] Shopping cart
- [ ] Order processing
- [ ] Inventory management
- [ ] Payment integration

#### URL Shortener
- [ ] Hash generation
- [ ] Redirect handling
- [ ] Analytics
- [ ] Scale considerations

#### Rate Limiter
- [ ] Algorithms
- [ ] Distributed rate limiting
- [ ] Client identification

#### Ticket Booking (BookMyShow)
- [ ] Seat locking under concurrent requests
- [ ] Optimistic vs pessimistic locking tradeoffs
- [ ] Reservation expiry and cleanup

#### Real-Time Location Tracking (Uber/Swiggy)
- [ ] GPS polling intervals and WebSocket streaming
- [ ] Eventual consistency in location updates
- [ ] Geo-distributed write paths

#### Video Upload & Transcoding Pipeline (YouTube)
- [ ] Chunked upload and resumable transfers
- [ ] Distributed encoding workers
- [ ] Async pipeline with status callbacks

#### OTP Delivery Service
- [ ] Rate limiting and retry storm prevention
- [ ] Multi-provider failover strategy
- [ ] Queue buffering during traffic spikes

#### Notification Fanout at Scale (Instagram)
- [ ] Celebrity vs regular user fanout strategies
- [ ] Push notification scalability
- [ ] Backpressure when follower count is massive

---

## Russian Curriculum

### Модуль 1: NFT (Нефункциональные требования)
- [ ] Производительность
- [ ] Масштабируемость
- [ ] Доступность
- [ ] Надёжность

### Модуль 3: Масштабирование
- [ ] Вертикальное масштабирование
- [ ] Горизонтальное масштабирование
- [ ] Балансировка нагрузки
- [ ] Кэширование

### Модуль 12: Системы в жизни
- [ ] Реальные кейсы
- [ ] Типовые архитектуры
- [ ] Решение задач

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Designing Data-Intensive Applications** — Kleppmann | 🔴 Critical | ⏳ |
| **Code Complete** — McConnell | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce Stage 14-15:**
- [ ] Implement inventory sharding
- [ ] Add read replicas for product queries
- [ ] Implement caching strategy
- [ ] Load test and identify bottlenecks
- [ ] Document architecture decisions (ADRs)

---

## Related
- [[Architecture - MOC]]
- [[Distributed Systems - MOC]]
- [[Databases - MOC]]
- [[00 - IT Career - MOC]]
