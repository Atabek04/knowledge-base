---
created: 2026-05-21
tags: [moc, postgresql, database, oltp]
---

> Open-source relational DBMS — ACID transactions, row-oriented storage, OLTP workloads.

---

## Fundamentals

- [ ] Data types (arrays, JSON, UUID)
- [ ] JSONB queries and indexing
- [ ] Full-text search
- [ ] Partitioning
- [ ] Connection pooling (PgBouncer)

## Transactions & Concurrency

General relational concepts — ACID, the anomalies, isolation levels, locking strategies — live in → [[Database Transactions & Concurrency - MOC]]. Listed here only where PostgreSQL behaves *specially*.

- [[PostgreSQL enforces stricter isolation than the SQL standard requires|Stricter isolation — no dirty reads ever, RR is snapshot isolation, SERIALIZABLE is SSI]]
- [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released|EvalPlanQual — blocked FOR UPDATE re-checks WHERE on the updated row]]
- [ ] MVCC implementation — tuple versions, xmin/xmax, visibility
- [ ] SELECT FOR UPDATE SKIP LOCKED — PG locking-clause syntax and wait policies
- [ ] Advisory locks — `pg_advisory_lock`, app-defined locks
- [ ] Lock modes and table-level locks — `LOCK TABLE`, conflict matrix
- [ ] Deadlock detection — `deadlock_timeout`

## Performance & Internals

- [ ] EXPLAIN and query analysis
- [ ] Index types (B-tree, Hash, GiST, GIN)
- [ ] Index optimization
- [ ] pg_stat for monitoring
- [ ] VACUUM and maintenance

## Replication & CDC

- [[PostgreSQL WAL records every change before applying to data files enabling crash recovery|WAL records changes before data files (crash recovery)]]
- [ ] Replication basics (streaming, logical)
- [ ] Replication slots

---

## Related

- [[Database Transactions & Concurrency - MOC]]
- [[Databases - MOC]]
- [[ClickHouse - MOC]]
- [[Distributed Systems - MOC]]
