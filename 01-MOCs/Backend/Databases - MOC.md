# Databases — MOC

> **Phase 3** of [[00 - IT Career - MOC]]
> Master data persistence and database design

---

## Progress

- [ ] SQL fundamentals
- [ ] Advanced SQL
- [ ] PostgreSQL deep dive
- [ ] Transactions & isolation
- [ ] JPA / Hibernate
- [ ] Redis (caching)
- [ ] MongoDB basics

---

## Topics

### SQL Fundamentals
- [ ] SELECT, INSERT, UPDATE, DELETE
- [ ] WHERE, ORDER BY, LIMIT, OFFSET
- [ ] JOINs (INNER, LEFT, RIGHT, FULL, CROSS)
- [ ] GROUP BY, HAVING
- [ ] Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- [ ] Subqueries
- [ ] UNION, INTERSECT, EXCEPT

### Advanced SQL
- [ ] Window functions (ROW_NUMBER, RANK, LAG, LEAD)
- [ ] CTEs (Common Table Expressions)
- [ ] Recursive queries
- [ ] EXPLAIN and query analysis
- [ ] Index types (B-tree, Hash, GiST, GIN)
- [ ] Index optimization
- [ ] Query optimization techniques
- [ ] Stored procedures and functions

### PostgreSQL Deep Dive
- [ ] Data types (arrays, JSON, UUID)
- [ ] JSONB queries and indexing
- [ ] Full-text search
- [ ] Partitioning
- [ ] Replication basics
- [ ] pg_stat for monitoring
- [ ] VACUUM and maintenance
- [ ] Connection pooling (PgBouncer)

### Transactions & Isolation
- [ ] ACID properties
- [ ] Isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)
- [ ] Dirty reads, non-repeatable reads, phantom reads
- [ ] Locking (row-level, table-level)
- [ ] Deadlock detection and prevention
- [ ] Optimistic vs pessimistic locking
- [ ] Two-phase commit (2PC)

### JPA / Hibernate
- [ ] Entity mapping (@Entity, @Table, @Column)
- [ ] Primary keys (@Id, @GeneratedValue)
- [ ] Relationships (@OneToOne, @OneToMany, @ManyToOne, @ManyToMany)
- [ ] Fetch types (LAZY vs EAGER)
- [ ] Cascading operations
- [ ] JPQL and Criteria API
- [ ] N+1 problem and solutions
- [ ] Caching (first-level, second-level)
- [ ] Entity lifecycle and states

### Connection Pooling
- [ ] HikariCP configuration
- [ ] Pool sizing
- [ ] Connection validation
- [ ] Leak detection

### Redis
- [ ] Data structures (Strings, Lists, Sets, Sorted Sets, Hashes)
- [ ] Commands and operations
- [ ] TTL and expiration
- [ ] Pub/Sub
- [ ] Transactions (MULTI/EXEC)
- [ ] Caching strategies (write-through, write-behind, cache-aside)
- [ ] Cache invalidation
- [ ] Spring Data Redis

### MongoDB Basics
- [ ] Documents and collections
- [ ] CRUD operations
- [ ] Query operators
- [ ] Indexing
- [ ] Aggregation pipeline
- [ ] When to use NoSQL vs SQL

---

## Russian Curriculum (Модуль 7)

### Хранение данных
- [ ] Реляционные базы данных
- [ ] NoSQL базы данных
- [ ] Шардирование
- [ ] Репликация
- [ ] Консистентность данных

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Java Persistence with Hibernate** — Manning | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce Stage 3-5:**
- [ ] Design normalized schema for products, orders, users
- [ ] Implement JPA entities with proper relationships
- [ ] Add indexes for common queries
- [ ] Implement product caching with Redis
- [ ] Use @Cacheable with Spring Cache abstraction
- [ ] Handle cache invalidation on product updates

---

## Related
- [[ClickHouse - MOC]] — OLAP DBMS
- [[Spring Ecosystem - MOC]]
- [[Architecture - MOC]]
- [[00 - IT Career - MOC]]
