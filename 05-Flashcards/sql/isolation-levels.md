TARGET DECK: Tech-KB::SQL::Isolation Levels
Tags: sql concurrency
**Chapter:** Isolation levels
**Related:** [[Database Transactions & Concurrency - MOC]]

---

START
Coding Questions
What defines a transaction isolation level?
Back: An **isolation level** is defined by **which read anomalies it still permits** — not by how it's implemented.
- Each level is a promise: "these anomalies can't happen to you; those still can"
- Higher level = fewer anomalies allowed, more cost
Tags: sql concurrency isolation
END

START
Coding Questions
What are the four SQL isolation levels (weakest to strongest), and which anomaly does each newly eliminate?
Back:
- **READ UNCOMMITTED** — allows all (dirty, non-repeatable, phantom)
- **READ COMMITTED** — stops **dirty reads**
- **REPEATABLE READ** — also stops **non-repeatable reads**
- **SERIALIZABLE** — also stops **phantoms** (and serialization anomalies)
Tags: sql concurrency isolation
END

START
Coding Questions
What is the trade-off when you raise the isolation level?
Back: Cleaner reads bought with more cost:
- **Higher** — more blocking, snapshot bookkeeping, serialization errors to catch and retry
- **Lower** — less contention, but anomalies leak into application code
- `READ COMMITTED` is the common default: cheap, kills dirty reads
Tags: sql concurrency isolation
END

START
Coding Questions
What isolation level does Spring @Transactional use by default, and why doesn't it stop lost updates?
Back: Default `Isolation.DEFAULT` → the DB default = **READ COMMITTED** in PostgreSQL.
- Stops dirty reads only
- Does **not** stop two transactions reading the same committed row and racing to overwrite
- `@Transactional` gives a transaction boundary, not a row lock
Tags: sql spring concurrency isolation
END

START
Coding Questions
How is PostgreSQL stricter than the SQL isolation standard?
Back: It gives stronger guarantees than the spec's minimum (built on MVCC snapshots):
- **No dirty reads at any level** — `READ UNCOMMITTED` behaves like `READ COMMITTED`
- **REPEATABLE READ blocks phantoms too** — a level earlier than the spec requires
- Only three distinct behaviors really exist
Tags: sql postgresql concurrency isolation
END

START
Coding Questions
What is PostgreSQL's REPEATABLE READ implemented as, and what are the consequences?
Back: **Snapshot isolation** — one snapshot taken at the transaction's first statement, read for the whole transaction.
- Non-repeatable reads **and** phantoms both vanish
- A lost update aborts the loser with `could not serialize access due to concurrent update`
Tags: sql postgresql concurrency isolation
END

START
Coding Questions
What does PostgreSQL SERIALIZABLE add on top of snapshot isolation?
Back: **Serializable Snapshot Isolation (SSI)** — also catches the **serialization anomaly** (e.g. write skew).
- A committed result no one-at-a-time ordering could produce
- Monitors read/write dependencies and aborts a transaction in a dangerous cycle
Tags: sql postgresql concurrency isolation
END
