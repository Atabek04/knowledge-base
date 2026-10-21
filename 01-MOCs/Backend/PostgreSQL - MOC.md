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

### Connection Model

- [[PostgreSQL spawns a dedicated OS process for each client connection|Process-per-connection — each client gets its own forked OS process]]
- [[PostgreSQL max_connections sets the server-side ceiling on simultaneous connections|max_connections — server ceiling (default 100), distinct from pool size]]
- [[Too many PostgreSQL connections cause CPU thrashing through excessive context switching|Too many connections → context-switch thrashing, not a RAM problem]]
- [ ] Connection pooling (PgBouncer)

## Roles & Access Control

- [ ] Roles: user and group are one concept, LOGIN makes a role a user
- [ ] Group roles with NOLOGIN (readonly, readwrite, ddl) granted to per-person login roles
- [ ] GRANT and REVOKE on database, schema, table; USAGE on schema is required first
- [ ] Revoking the PUBLIC defaults on the public schema and database
- [ ] Object ownership: one NOLOGIN owner role for all objects, migrations run as it
- [ ] ALTER DEFAULT PRIVILEGES: grants for tables not created yet
- [ ] Predefined roles: pg_read_all_data, pg_write_all_data, pg_monitor
- [ ] Separate roles per app service, never the superuser
- [ ] pg_hba.conf: who may connect from where, with which auth method (scram-sha-256)
- [ ] Row-level security policies
- [ ] Audit logging with pgAudit
- [ ] Short-lived credentials from Vault's database engine instead of shared passwords

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
