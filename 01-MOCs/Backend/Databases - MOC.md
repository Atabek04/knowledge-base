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
- [[Primary key uniquely identifies each row and anchors referential integrity across tables|Primary key identifies rows and anchors referential integrity]]
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
- [ ] Covering indexes and index-only scans
- [ ] Stored procedures and functions

### PostgreSQL Deep Dive
→ [[PostgreSQL - MOC]]

### Transactions & Isolation
→ [[Database Transactions & Concurrency - MOC]] — anomalies, isolation levels, locking strategies (engine-agnostic)

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
- [[Connection pooling reuses connections at application level to reduce overhead|Connection pooling — borrow, use, return to avoid handshake overhead]]
- [[HikariCP maximumPoolSize caps the total number of live database connections|maximumPoolSize — hard ceiling on live DB connections]]
- [[HikariCP minimumIdle sets the floor for idle connections held in reserve|minimumIdle — floor for idle connections (default = fixed pool)]]
- [[HikariCP connectionTimeout is the max wait before throwing an exception|connectionTimeout — fail-fast threshold when pool is exhausted]]
- [[HikariCP maxLifetime recycles connections before the database closes them|maxLifetime — recycle connections before the DB times them out]]
- [[HikariCP idleTimeout evicts connections that sit idle beyond the threshold|idleTimeout — shrinks elastic pool back to minimumIdle after a spike]]
- [[HikariCP keepaliveTime pings idle connections to prevent server-side timeout|keepaliveTime — pings idle connections so firewalls don't drop them]]
- [[HikariCP leakDetectionThreshold warns when a connection is held too long|leakDetectionThreshold — logs stack trace when a connection is leaked]]

### Schema Migration
- [[Flyway clean drops and re-applies migrations while repair only realigns checksums|Flyway clean (drop + re-apply) vs repair (realign checksums)]]
- [ ] Liquibase — changelog-based migrations
- [ ] Migration best practices (forward-only, idempotent)

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

### Cassandra
- [ ] Partition key and clustering key design
- [ ] Consistency levels and read repair
- [ ] Wide-column data modeling

### DynamoDB
- [ ] Partition key design and hot partitions
- [ ] GSI vs LSI
- [ ] DynamoDB Streams

---

## Data Modeling

### Normalization

*Each fact in exactly one place — removing redundancy to kill anomalies.*

- [[Normalization eliminates redundancy to prevent insert update and delete anomalies|Normalization kills insert/update/delete anomalies]]
- [[First normal form requires atomic column values with no repeating groups|1NF: atomic values, no repeating groups]]
- [[Second normal form removes partial dependencies on part of a composite key|2NF: no partial dependency on a composite key]]
- [[Third normal form removes transitive dependencies between non-key columns|3NF: no transitive non-key dependency]]
- [[Boyce-Codd normal form requires every determinant to be a candidate key|BCNF: every determinant is a candidate key]]
- [[Denormalization trades write integrity for read performance by reintroducing redundancy|Denormalization trades integrity for read speed]]
- [[Fourth and fifth normal forms remove multivalued and join dependencies|4NF/5NF: multivalued and join dependencies]]

### Database Types & Selection

*Match a store's data model and guarantees to the requirements.*

- [[Relational databases enforce a fixed schema and ACID while NoSQL relaxes them for scale|Relational (schema + ACID) vs NoSQL (relaxed for scale)]]
- [[A document database stores self-describing records queried by their nested content|Document store: self-describing records (MongoDB)]]
- [[A key-value store maps opaque keys to values for the fastest possible lookups|Key-value store: fastest lookups (Redis, DynamoDB)]]
- [[A column-family store groups columns into families for wide sparse write-heavy tables|Column-family store: wide sparse tables (Cassandra)]]
- [[A graph database makes relationships first-class for traversal-heavy queries|Graph database: relationships first-class (Neo4j)]]
- [[Choosing a database means matching its model and guarantees to non-functional requirements|Choose a database by matching its model to NFRs]]
- [[CAP theorem forces a partitioned system to choose between consistency and availability|CAP: consistency vs availability under partition]] → [[Distributed Systems - MOC]]

### Requirements Artifacts for Data

*Documenting what the data means and who touches it.*

- [[A data dictionary is the authoritative catalog defining every data element and its rules|Data dictionary: authoritative catalog of data elements]]
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles|CRUD matrix: entity × operation grid reveals gaps]]

### Data Governance

*Who owns the data, what "one truth" means, and how its lifecycle ends.*

- [[A data owner is accountable for a data domain while a data steward maintains its quality|Data owner vs data steward]]
- [[Master data management enforces one trusted record for entities shared across systems|MDM: one golden record across systems]]
- [[Data quality is measured along completeness accuracy consistency and timeliness|Data quality: completeness, accuracy, consistency, timeliness]]
- [[Data governance documents the retention archival and deletion rules for each class of data|Data governance: retention, archival, deletion rules]]
- [[Process mining reconstructs the real process from event logs to compare against the documented one|Process mining: actual vs documented process from logs]]

### Schema Migrations

*Versioning schema changes safely in production without downtime or data loss.*

- [[Database migrations version schema changes while backups recover data loss — they are never substitutes]] — when to use migrations vs backups, expand/contract pattern, auto-gen vs handwritten, fix-forward rollback

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
- [[Database Transactions & Concurrency - MOC]] — ACID, anomalies, isolation, locking
- [[PostgreSQL - MOC]] — OLTP RDBMS
- [[ClickHouse - MOC]] — OLAP DBMS
- [[Spring Ecosystem - MOC]]
- [[Architecture - MOC]]
- [[DDIA - MOC]] — reading index for Designing Data-Intensive Applications
