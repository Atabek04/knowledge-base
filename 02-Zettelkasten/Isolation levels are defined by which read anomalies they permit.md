---
created: 2026-06-12
tags: [database, sql, concurrency, transactions, isolation]
aliases: [isolation levels, transaction isolation levels, isolation level]
---

When transactions run at the same time, a database can let them see more of each other's in-flight work (faster, but anomalies leak in) or wall them off (cleaner, but more locking and aborts). An **isolation level** is the knob that picks where on that spectrum a transaction sits.

The SQL standard defines each level not by *how* it's implemented but by **which read anomalies it still allows** — so the level is really a promise: "these anomalies cannot happen to you; those still can."

---

### The four standard levels

Ordered weakest to strongest, each forbids one more anomaly than the last:

| Level | Dirty read | Non-repeatable | Phantom |
|---|---|---|---|
| READ UNCOMMITTED | allowed | allowed | allowed |
| READ COMMITTED | — | allowed | allowed |
| REPEATABLE READ | — | — | allowed |
| SERIALIZABLE | — | — | — |

The column anomalies each have their own note: [[A dirty read happens when a transaction reads another transactions uncommitted changes|dirty read]], [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update|non-repeatable read]], [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones|phantom read]]. Reading down a column tells you the lowest level that stops that anomaly.

---

### The trade-off the knob controls

Each step up buys cleaner reads at a price: <mark style="background: #FFB8EBA6;">more blocking, more snapshot bookkeeping, and serialization errors you must catch and retry</mark>. Each step down runs with less contention but leaks anomalies you then have to defend against in application code.

`READ COMMITTED` is the most common default — strong enough to kill dirty reads, loose enough to stay cheap. It is also the level [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates|Spring's `@Transactional` inherits by default]].

---

### Engines are often stricter than the table

This table is the *standard minimum* — a level may forbid **more** than required, just never less. [[PostgreSQL enforces stricter isolation than the SQL standard requires|PostgreSQL, for example, is stricter]]: it never allows dirty reads at any level and blocks phantoms one level earlier than the spec demands. Always check the specific engine's guarantees against this baseline.

---

### Read more

- [[A dirty read happens when a transaction reads another transactions uncommitted changes]]
- [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update]]
- [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones]]
- [[PostgreSQL enforces stricter isolation than the SQL standard requires]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates]]
