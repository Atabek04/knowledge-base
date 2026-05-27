---
created: 2026-05-21
tags: [moc, postgresql, database, oltp]
---

# PostgreSQL — MOC

> Open-source relational DBMS — ACID transactions, row-oriented storage, OLTP workloads.

---

## Fundamentals

- [ ] Data types (arrays, JSON, UUID)
- [ ] JSONB queries and indexing
- [ ] Full-text search
- [ ] Partitioning
- [ ] Connection pooling (PgBouncer)

## Transactions & Isolation

- [[PostgreSQL transactions wrap multiple operations in an atomic unit with automatic rollback on failure]]
- [[PostgreSQL WAL records every change before applying to data files enabling crash recovery]]
- [ ] ACID properties
- [ ] Isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)
- [ ] Dirty reads, non-repeatable reads, phantom reads
- [ ] Locking (row-level, table-level)
- [ ] Deadlock detection and prevention
- [ ] Optimistic vs pessimistic locking
- [ ] Two-phase commit (2PC)

## Performance & Internals

- [ ] EXPLAIN and query analysis
- [ ] Index types (B-tree, Hash, GiST, GIN)
- [ ] Index optimization
- [ ] pg_stat for monitoring
- [ ] VACUUM and maintenance

## Replication & CDC

- [[PostgreSQL WAL records every change before applying to data files enabling crash recovery]]
- [ ] Replication basics (streaming, logical)
- [ ] Replication slots

---

## Related

- [[Databases - MOC]]
- [[ClickHouse - MOC]]
- [[Distributed Systems - MOC]]
