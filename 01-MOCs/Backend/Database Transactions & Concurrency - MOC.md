---
created: 2026-06-12
tags: [moc, database, concurrency, transactions, isolation]
---

> Engine-agnostic relational concurrency control — ACID, the anomalies concurrent transactions cause, the isolation levels that forbid them, and the locking strategies that protect data. SQL-standard concepts; per-engine behavior links out.

---

## Transactions & ACID

- [[PostgreSQL transactions wrap multiple operations in an atomic unit with automatic rollback on failure|Transaction — atomic all-or-nothing unit, auto-rollback on failure]]
- [ ] ACID properties (atomicity, consistency, isolation, durability)
- [ ] Two-phase commit (2PC) — atomic commit across multiple databases

## Concurrency anomalies

- [[A dirty read happens when a transaction reads another transactions uncommitted changes|Dirty read — reads another txn's uncommitted data]]
- [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update|Non-repeatable read — a re-read row changed value mid-txn]]
- [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones|Phantom read — a re-run query gains or loses matching rows]]
- [[A lost update occurs when two transactions read a row then both write and the second write erases the first|Lost update — concurrent read-modify-write, second write erases the first]]
- [ ] Write skew / serialization anomaly — result no serial order could produce

## Isolation levels

- [[Isolation levels are defined by which read anomalies they permit|Isolation levels — each forbids one more anomaly, for a concurrency cost]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates|@Transactional defaults to READ COMMITTED — doesn't stop lost updates]]

## Locking strategies

- [[Optimistic and pessimistic locking are two strategies for preventing lost updates|Optimistic vs pessimistic — detect conflict late vs lock early]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|FOR UPDATE — locking read held to commit, closes read-write race]]
- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked|Wait policies — block (default) vs NOWAIT (error) vs SKIP LOCKED (skip)]]
- [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue|FOR UPDATE SKIP LOCKED — table becomes a competing-consumers queue]]
- [[FOR UPDATE locks rows from every joined table unless you restrict it with OF|FOR UPDATE OF — a join locks every table unless you name one]]
- [[FOR UPDATE locks rows beneath LIMIT and OFFSET in the query plan|FOR UPDATE + LIMIT — locks under the limit; OFFSET rows lock too]]
- [ ] Deadlock detection and prevention
- [ ] Advisory locks — application-defined locks not tied to rows
- [ ] MVCC — readers and writers never block via row versioning

## Engine-specific behavior

- → [[PostgreSQL - MOC]] — PG's stricter-than-standard isolation, EvalPlanQual, `SKIP LOCKED`, MVCC internals

---

## Related

- [[Databases - MOC]]
- [[PostgreSQL - MOC]]
- [[Distributed Systems - MOC]]
