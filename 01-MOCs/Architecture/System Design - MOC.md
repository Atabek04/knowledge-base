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

### Async Processing
- [ ] Message queues
- [ ] Task queues
- [ ] Background jobs
- [ ] Batch processing

### System Design Process
1. Requirements clarification
2. Capacity estimation
3. High-level design
4. Component deep dive
5. Bottleneck identification
6. Trade-off discussion

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

## Primary Course

**Grokking Modern System Design** — `/Users/salahaddin/Documents/Courses/Grokking-System-Design` → see [[Grokking-System-Design - Tracker]]

Schedule:
- August 2026: modules 1–10 (foundation — DNS, Load Balancers, Databases, CDN, Cache)
- September 2026: modules 11–25 (monitoring, messaging, rate limiter, blob store, distributed search/log)
- October 2026: modules 26–40 (real system designs — YouTube, Uber, Twitter, WhatsApp, Google Docs)

After each module: draw the design from memory on paper (10 min) — no peeking.

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

## Course Trackers

Module-by-module progress (moved from Ribaat vault):

- [[Grokking-System-Design - Tracker]] — `06-Planning/Trackers/` · Grokking Modern System Design, 40 modules

Sequencing + time budget + end-state (design 8 systems in 45 min): [[Interview-Prep-Master-Plan]]

---

## Related
- [[Interview-Prep-Master-Plan]]
- [[Architecture - MOC]]
- [[Distributed Systems - MOC]]
- [[Databases - MOC]]
- [[00 - IT Career - MOC]]
