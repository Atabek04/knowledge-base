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

### Collecting Requirements

#### Functional Requirements
- [ ] Define what the system does from a user perspective
- [ ] Narrow a vague prompt (e.g. "Design Instagram") to a specific slice
- [ ] Ask open-ended questions to force decisions with the interviewer
- [ ] State assumptions explicitly ("I'll assume a Users API already exists")

#### Non-Functional Requirements (NFRs)
- [ ] Performance (latency, throughput)
- [ ] Scalability (vertical, horizontal)
- [ ] Availability (uptime, SLA/SLO)
- [ ] Reliability (MTBF, MTTR)
- [ ] Durability (data persistence)
- [ ] Consistency requirements
- [ ] Security requirements
- [ ] Cost constraints

### The Basics

#### Client / Server Model
- [ ] Client (browser/mobile) sends request → Server handles logic → returns data
- [ ] In distributed systems: load balancer routes to stateless compute nodes (EC2, Fargate)
- [ ] Key decisions: where logic lives, what can be cached client-side vs server-side

#### Stateless vs Stateful Services
- [ ] **Stateless** — no session/user data between requests; easy horizontal scaling; default choice
- [ ] **Stateful** — retains in-memory session state; hard to scale; use only when latency gain justifies it (e.g. multiplayer games)
- [ ] Real-world nuance: delegate state to external DB → server is stateless, system has state

#### Access Patterns
- [ ] DB choice should be driven by how data is read/written, not by trends
- [ ] Simple key lookups → key-value store (DynamoDB, Redis)
- [ ] Complex relationships / joins → relational (PostgreSQL, MySQL)
- [ ] High write throughput / time-series → wide-column (Cassandra, HBase)
- [ ] Nested/flexible documents → document store (MongoDB, Firestore)
- [ ] Relationship traversal → graph DB (Neo4j, Amazon Neptune)

#### Database Types & CAP Theorem
- [ ] **CAP theorem** — can only guarantee 2 of 3: Consistency, Availability, Partition Tolerance
- [ ] P is always given (networks fail) → real choice is **CP vs AP**
- [ ] CP systems (CockroachDB, PostgreSQL) — consistent but may reject during partition
- [ ] AP systems (Cassandra, DynamoDB) — always available but may return stale data
- [ ] **RDBMS** — ACID, structured schema, joins, CP → banking, inventory, orders
- [ ] **Key-Value** — fast O(1) lookups, no schema, AP → caching, sessions, shopping carts
- [ ] **Document** — flexible JSON/BSON schema, can be CP or AP → content platforms, user profiles
- [ ] **Wide-Column** — sparse rows, high write throughput, AP → logging, telemetry, analytics
- [ ] **Graph** — nodes + edges for relationship traversal → social networks, fraud detection

### Capacity Planning
- [[Server capacity is bounded by whichever resource saturates first, not just RAM|Server capacity — bounded by first resource to saturate, not just RAM]]
- [ ] Traffic estimation
- [ ] Storage estimation
- [ ] Bandwidth estimation
- [ ] QPS calculations
- [ ] Read/write ratios

### Scaling Strategies

#### Database Scaling
- [[The database is the hardest tier to scale because every app server shares one writer|DB is hardest tier to scale — all servers share one writer]]
- [[A connection storm from new instances can exhaust the database connection limit|Connection storm — too many instances exhaust the DB connection limit]]
- [ ] Vertical scaling
- [ ] Read replicas
- [ ] Sharding strategies
- [ ] Consistent hashing
- [ ] Denormalization
- [ ] Hot partition problem — bad partition key choice → uneven load
- [ ] Avoiding JOINs at scale — denormalization tradeoffs in read-heavy systems

#### Application Scaling
- [ ] Stateless services
- [[Horizontal scaling multiplies stateless app servers but not the shared database|Horizontal scaling — clones stateless app servers, not the shared DB]]
- [ ] Load balancing
- [[Auto-scaling is reactive so it always trails a sudden traffic spike|Auto-scaling is reactive — always trails a sudden spike]]
- [[A newly launched instance needs warm-up before it can serve traffic|New instance needs warm-up before serving — alive is not ready]]
- [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot|Pre-warm + headroom absorb bursts reactive scaling cannot]]

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
- [[A cold cache sends every request to the database, causing a thundering herd|Cold cache sends every request to the DB — thundering herd]]
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
- [[Load shedding drops excess requests to keep the core service alive|Load shedding — drop excess to keep the core alive]]
- [ ] Backpressure — upstream flow control when consumers lag producers

### Trade-Offs

#### Consistency vs Availability (CAP)
- [ ] Consistency — all nodes see same data; stale reads never allowed; needs distributed locking or quorum
- [ ] Availability — always responds, even if data is stale
- [ ] Choose consistency: financial transactions, user permissions, inventory counts
- [ ] Choose availability: news feeds, caches, logging/analytics
- [ ] Hybrid: same system can use AP for browsing and CP for checkout

#### Latency vs Durability
- [ ] Durability — acknowledged write survives crash; requires fsync, replication, WAL → adds 50–200ms
- [ ] Latency strategies: write-behind cache, buffer + flush, write to memory only
- [ ] Prioritize durability: payments, orders, password changes
- [ ] Prioritize latency: likes, views, logs (low-risk reversible writes)

#### Cost vs Performance
- [ ] Every performance boost has a cost (AWS bill + engineering cost)
- [ ] Cost reduction: smaller instances, fewer replicas, batching, rate limiting, shorter log retention
- [ ] Justify performance spend only when it directly impacts revenue

#### Monolith vs Microservices
- [ ] **Monolith** — single codebase; simple to develop/debug/scale as unit; default for startups
- [ ] **Microservices** — independent services per concern; independent scaling; teams don't block each other
- [ ] Microservices cost: network calls, version mismatches, distributed monitoring, auth between services
- [ ] Choose microservices when components serve distinct use cases and scale independently

#### Read vs Write Optimization
- [ ] **Read-heavy** → denormalize data, cache aggressively, read replicas, minimize joins
- [ ] **Write-heavy** → normalize, append-only, bulk writes, async pipelines
- [ ] **CQRS** (Command Query Responsibility Segregation) — split write path (normalized, durable) from read path (denormalized, fast)
- [ ] CQRS trade-off: eventual consistency between read/write models + added complexity

#### Real-Time vs Eventually Consistent
- [ ] **Strongly consistent** — every read reflects latest write; needs distributed locking + quorum; adds latency
- [ ] **Eventually consistent** — replicas catch up asynchronously; faster writes; stale reads briefly possible
- [ ] Use strong consistency: password changes, auth tokens, account state
- [ ] Use eventual consistency: likes, comments, feed updates, profile pictures

### Large File Uploads & Downloads

#### Pre-signed URLs
- [ ] Client requests a pre-signed URL from your server → server generates it using storage credentials → client uploads/downloads directly to storage (bypasses your server)
- [ ] Benefit: large files never pass through your app servers → no bandwidth bottleneck, no memory pressure
- [ ] Pre-signed URL contains: bucket, object key, expiry time, signature — storage validates on arrival
- [ ] **S3** — native support via `presignedPutObject` / `presignedGetObject`
- [ ] **MinIO** — S3-compatible API, same pre-signed URL pattern works (investigate SDK compatibility)
- [ ] **Garage** — S3-compatible; pre-signed URL support present but less documented — verify behavior under load
- [ ] Common pattern: server issues URL with short TTL (5–15 min) → client uploads → storage triggers webhook/event → server confirms

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

> Interview-day running order with time budgets: [[HelloInterview Delivery Framework structures a system design interview into six timed steps|HelloInterview framework: six timed interview steps]]

### Design Problems Practice

**Interview process:** 1) Clarify requirements (5 min) → 2) Capacity estimate (5 min) → 3) High-level design (10 min) → 4) Deep dive (15 min) → 5) Bottlenecks + trade-offs (5 min)

#### Tier 1 — Most Common (do these first)
- [ ] URL Shortener (Bitly) — hashing, redirects, analytics, scale
- [ ] Rate Limiter — token bucket, sliding window, distributed
- [ ] Key-Value Store — consistent hashing, replication, partitioning
- [ ] Unique ID Generator — snowflake, UUID, clock sync
- [ ] Web Crawler — BFS, dedup, politeness, scale

#### Tier 2 — Frequently Asked
- [ ] Twitter/X Feed — fanout on write vs read, celebrity problem
- [ ] Instagram — photo storage, CDN, feed ranking
- [ ] WhatsApp / Chat System — WebSocket, message delivery, group chat
- [ ] YouTube / Netflix — video upload, streaming, CDN, encoding
- [ ] Notification System — push, email, SMS, fan-out
- [ ] Search Autocomplete — trie, top-k, real-time suggestions

#### Tier 3 — Advanced
- [ ] Distributed Message Queue (Kafka) — partitions, consumer groups, durability
- [ ] Ride-Sharing (Uber/Lyft) — geospatial indexing, matching, surge pricing
- [ ] Google Maps — routing, tile serving, ETA
- [ ] Dropbox / Google Drive — chunked upload, sync, conflict resolution
- [ ] Distributed Cache (Redis) — eviction, replication, persistence
- [ ] Payment System — idempotency, double-charge prevention, reconciliation

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

## Primary Course — Grokking Modern System Design

**Path:** `/Users/salahaddin/Documents/Courses/Grokking-System-Design`
**Progress:** 0 / 40 modules

Schedule:
- August 2026: modules 1–10 (foundation — DNS, Load Balancers, Databases, CDN, Cache)
- September 2026: modules 11–25 (monitoring, messaging, rate limiter, blob store, distributed search/log)
- October 2026: modules 26–40 (real system designs — YouTube, Uber, Twitter, WhatsApp, Google Docs)

After each module: draw the design from memory on paper (10 min) — no peeking.

### Module 1 — System Design Interviews
- [ ] What Is a System Design Interview?
- [ ] How to Prepare for Success
- [ ] How to Perform Well

### Module 2 — Introduction
- [ ] Introduction to Modern System Design
- [ ] Course Structure for Modern System Design

### Module 3 — Abstractions
- [ ] Why Are Abstractions Important?
- [ ] Network Abstractions: Remote Procedure Calls
- [ ] Spectrum of Consistency Models
- [ ] The Spectrum of Failure Models

### Module 4 — Non-functional System Characteristics
- [ ] Availability
- [ ] Reliability
- [ ] Scalability
- [ ] Maintainability
- [ ] Fault Tolerance

### Module 5 — Back-of-the-envelope Calculations
- [ ] Put Back-of-the-envelope Numbers in Perspective
- [ ] Examples of Resource Estimation

### Module 6 — Building Blocks
- [ ] Introduction to Building Blocks for Modern System Design

### Module 7 — Domain Name System (DNS)
- [ ] Introduction to Domain Name System
- [ ] How the Domain Name System Works

### Module 8 — Load Balancers
- [ ] Introduction to Load Balancers
- [ ] Global and Local Load Balancing
- [ ] Advanced Details of Load Balancers

### Module 9 — Databases
- [ ] Introduction to Databases
- [ ] Types of Databases
- [ ] Data Replication
- [ ] Data Partitioning
- [ ] Trade-offs in Databases

### Module 10 — Key-value Store
- [ ] System Design: The Key-value Store
- [ ] Design of a Key-value Store
- [ ] Ensure Scalability and Replication
- [ ] Versioning Data and Achieving Configurability
- [ ] Enable Fault Tolerance and Failure Detection

### Module 11 — Content Delivery Network (CDN)
- [ ] System Design: The CDN
- [ ] Introduction to a CDN
- [ ] Design of a CDN
- [ ] In-depth Investigation of CDN: Part 1
- [ ] In-depth Investigation of CDN: Part 2
- [ ] Evaluation of CDN's Design
- [ ] Quiz on CDN's Design

### Module 12 — Sequencer
- [ ] System Design: Sequencer
- [ ] Design of a Unique ID Generator
- [ ] Unique IDs with Causality

### Module 13 — Distributed Monitoring
- [ ] System Design: Distributed Monitoring
- [ ] Introduction to Distributed Monitoring
- [ ] Prerequisites of a Monitoring System

### Module 14 — Monitor Server-side Errors
- [ ] Design of a Monitoring System
- [ ] Detailed Design of a Monitoring System
- [ ] Visualize Data in a Monitoring System

### Module 15 — Monitor Client-side Errors
- [ ] Focus on Client-side Errors in a Monitoring System
- [ ] Design of a Client-side Monitoring System

### Module 16 — Distributed Cache
- [ ] System Design: The Distributed Cache
- [ ] Background of Distributed Cache
- [ ] High-level Design of a Distributed Cache
- [ ] Detailed Design of a Distributed Cache
- [ ] Evaluation of a Distributed Cache's Design
- [ ] Memcached versus Redis

### Module 17 — Distributed Messaging Queue
- [ ] System Design: The Distributed Messaging Queue
- [ ] Requirements of Design
- [ ] Considerations of Design
- [ ] Design of a Distributed Messaging Queue: Part 1
- [ ] Design of a Distributed Messaging Queue: Part 2
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 18 — Pub-sub
- [ ] System Design: The Pub-sub Abstraction
- [ ] Introduction to Pub-sub
- [ ] Design of a Pub-sub System

### Module 19 — Rate Limiter
- [ ] System Design: The Rate Limiter
- [ ] Requirements of Design
- [ ] Design of a Rate Limiter
- [ ] Rate Limiter Algorithms
- [ ] Quiz on Design

### Module 20 — Blob Store
- [ ] System Design: A Blob Store
- [ ] Requirements of Design
- [ ] Design of a Blob Store
- [ ] Design Considerations of a Blob Store
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 21 — Distributed Search
- [ ] System Design: The Distributed Search
- [ ] Requirements of Design
- [ ] Indexing in a Distributed Search
- [ ] Design of a Distributed Search
- [ ] Scaling Search and Indexing
- [ ] Evaluation of Design

### Module 22 — Distributed Logging
- [ ] System Design: Distributed Logging
- [ ] Introduction to Distributed Logging
- [ ] Design of a Distributed Logging Service

### Module 23 — Distributed Task Scheduler
- [ ] System Design: The Distributed Task Scheduler
- [ ] Requirements of Design
- [ ] Design of a Distributed Task Scheduler
- [ ] Design Considerations
- [ ] Evaluation of Design

### Module 24 — Sharded Counters
- [ ] System Design: The Sharded Counters
- [ ] High-level Design of Sharded Counters
- [ ] Detailed Design of Sharded Counters
- [ ] Quiz on Design

### Module 25 — Concluding Building Blocks
- [ ] Wrapping Up the Building Blocks Discussion
- [ ] The RESHADED Approach for System Design

### Module 26 — Design YouTube
- [ ] System Design: YouTube
- [ ] Requirements of Design
- [ ] Design of YouTube
- [ ] Evaluation of Design
- [ ] The Reality Is More Complicated
- [ ] Quiz on Design

### Module 27 — Design Quora
- [ ] System Design: Quora
- [ ] Requirements of Design
- [ ] Initial Design of Quora
- [ ] Final Design of Quora
- [ ] Evaluation of Design

### Module 28 — Design Google Maps
- [ ] System Design: Google Maps
- [ ] Requirements of Design
- [ ] Design of Google Maps
- [ ] Challenges of Design
- [ ] Detailed Design of Google Maps
- [ ] Evaluation of Design

### Module 29 — Design Proximity Service (Yelp)
- [ ] System Design: Yelp
- [ ] Requirements of Design
- [ ] Design of Yelp
- [ ] Design Considerations
- [ ] Quiz on Design

### Module 30 — Design Uber
- [ ] System Design: Uber
- [ ] Requirements of Design
- [ ] High-level Design of Uber
- [ ] Detailed Design of Uber
- [ ] Payment Service and Fraud Detection
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 31 — Design Twitter
- [ ] System Design: Twitter
- [ ] Requirements of Design
- [ ] High-level Design of Twitter
- [ ] Detailed Design of Twitter
- [ ] Client-side Load Balancer for Twitter
- [ ] Quiz on Design

### Module 32 — Design Newsfeed System
- [ ] System Design: Newsfeed System
- [ ] Requirements of Design
- [ ] Design of a Newsfeed System
- [ ] Evaluation of Design

### Module 33 — Design Instagram
- [ ] System Design: Instagram
- [ ] Requirements of Design
- [ ] Design of Instagram
- [ ] Detailed Design of Instagram
- [ ] Quiz on Design

### Module 34 — Design URL Shortener (TinyURL)
- [ ] System Design: TinyURL
- [ ] Requirements of Design
- [ ] Design and Deployment of TinyURL
- [ ] Encoder for TinyURL
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 35 — Design Web Crawler
- [ ] System Design: Web Crawler
- [ ] Requirements of Design
- [ ] Design of a Web Crawler
- [ ] Design Improvements
- [ ] Evaluation of Design

### Module 36 — Design WhatsApp
- [ ] System Design: WhatsApp
- [ ] Requirements of Design
- [ ] High-level Design of WhatsApp
- [ ] Detailed Design of WhatsApp
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 37 — Design Typeahead Suggestion
- [ ] System Design: Typeahead Suggestion System
- [ ] Requirements of Design
- [ ] High-level Design
- [ ] Data Structure for Storing Prefixes
- [ ] Detailed Design
- [ ] Evaluation of Design
- [ ] Quiz on Design

### Module 38 — Design Google Docs
- [ ] System Design: Google Docs
- [ ] Requirements of Design
- [ ] Design of Google Docs
- [ ] Concurrency in Collaborative Editing
- [ ] Evaluation of Design

### Module 39 — Spectacular Failures
- [ ] Introduction to Distributed System Failures
- [ ] Facebook, WhatsApp, Instagram, Oculus Outage
- [ ] AWS Kinesis Outage Affecting Many Organizations
- [ ] AWS Wide Spread Outage

### Module 40 — Concluding Remarks
- [ ] Conclusions

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

Sequencing + time budget + end-state (design 8 systems in 45 min): [[Interview-Prep-Master-Plan]]

---

## Related
- [[Interview-Prep-Master-Plan]]
- [[Architecture - MOC]]
- [[Distributed Systems - MOC]]
- [[Databases - MOC]]
- [[AWS - MOC]]
