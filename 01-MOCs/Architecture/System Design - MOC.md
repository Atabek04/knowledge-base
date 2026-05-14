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
