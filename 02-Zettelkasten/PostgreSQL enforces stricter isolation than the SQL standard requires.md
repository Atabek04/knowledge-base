---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, isolation]
aliases: [PostgreSQL isolation, PostgreSQL repeatable read]
---

The SQL standard defines [[Isolation levels are defined by which read anomalies they permit|isolation levels as a minimum]] — a level must forbid *at least* its listed anomalies, but may forbid more. PostgreSQL takes that freedom: at every level it gives stronger guarantees than the standard requires, because it builds isolation on **MVCC snapshots** rather than read locks.

Knowing where PostgreSQL is stricter than the table matters — code written to the standard's worst case is often defending against anomalies PostgreSQL already prevents.

---

### Only three levels really exist

PostgreSQL accepts all four level names but provides three distinct behaviors. <mark style="background: #FFF3A3A6; font-weight: bold;">`READ UNCOMMITTED` behaves exactly like `READ COMMITTED`</mark> — dirty reads are impossible at *any* level, since a transaction only ever sees committed row versions.

---

### REPEATABLE READ is snapshot isolation

This is the big divergence. PostgreSQL's `REPEATABLE READ` takes <mark style="background: #ABF7F7A6;">one snapshot at the transaction's first statement and reads from it for the whole transaction</mark>. Consequences:

- Non-repeatable reads vanish (the snapshot never moves).
- **Phantoms also vanish** — a full level earlier than the standard, which only requires that at `SERIALIZABLE`.
- A [[A lost update occurs when two transactions read a row then both write and the second write erases the first|lost update]] is caught: the loser aborts with `could not serialize access due to concurrent update` and must retry.

---

### SERIALIZABLE adds Serializable Snapshot Isolation

On top of snapshot isolation, `SERIALIZABLE` uses <mark style="background: #FFF3A3A6; font-weight: bold;">SSI</mark> to also catch the **serialization anomaly** — concurrent transactions committing a result no one-at-a-time ordering could produce (such as write skew). It monitors read/write dependencies and aborts a transaction in any dangerous cycle.

---

### Read more

- [[Isolation levels are defined by which read anomalies they permit]]
- [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones]]
- [[A lost update occurs when two transactions read a row then both write and the second write erases the first]]
- [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released]]
