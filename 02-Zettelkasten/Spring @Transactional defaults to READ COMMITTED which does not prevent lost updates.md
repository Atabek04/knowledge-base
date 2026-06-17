---
created: 2026-06-12
tags: [spring, postgresql, database, concurrency, transactions]
aliases: [Transactional isolation, Spring transaction isolation, Transactional default isolation]
---

Many Spring developers treat `@Transactional` as a catch-all for concurrency: wrap the method, and races are handled. It is not. The annotation gives you a transaction boundary — start, commit, rollback — but says nothing about row locking, and its default isolation lets lost updates through.

This is the gap that surprises people who have only ever used the annotation and never written explicit SQL locks.

---

### @Transactional gives a transaction, not a lock

`@Transactional` ensures the wrapped work is **atomic** — all of it commits or none of it does. That solves *partial failure*, not *concurrent access*.

Two threads can each run the same `@Transactional` method, each in its own valid transaction, and still both read a row, both decide from it, and both write — a textbook [[A lost update occurs when two transactions read a row then both write and the second write erases the first|lost update]]. Atomicity never promised they would take turns.

---

### The default isolation is READ COMMITTED

`@Transactional` without an explicit `isolation` uses <mark style="background: #FFF3A3A6; font-weight: bold;">`Isolation.DEFAULT`</mark> — defer to the database default. For PostgreSQL that is `READ COMMITTED`.

```java
@Transactional   // isolation = DEFAULT → PostgreSQL READ COMMITTED
public void checkIn(...) { ... }
```

[[Isolation levels are defined by which read anomalies they permit|`READ COMMITTED`]] guarantees one thing: you never read another transaction's **uncommitted** data (no dirty reads). It deliberately does **not** stop two transactions from reading the same committed row and racing to overwrite it.

So the annotation is doing exactly what it promises — and a lost update slips right through.

---

### Closing the gap

You have to ask for protection explicitly:

- **Row lock** — add a [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|locking read (`FOR UPDATE`)]] to the query (`@Lock(PESSIMISTIC_WRITE)` in Spring Data JPA).
- **Higher isolation** — set `@Transactional(isolation = Isolation.REPEATABLE_READ)` or `SERIALIZABLE`, then be ready to <mark style="background: #FFB8EBA6;">catch the serialization error and retry</mark>.

<mark style="background: #ABF7F7A6;">`@Transactional` chooses *when* to commit; isolation and locking choose *how concurrent writers interact*. They are separate decisions.</mark>

---

### Read more

- [[Isolation levels are defined by which read anomalies they permit]]
- [[A lost update occurs when two transactions read a row then both write and the second write erases the first]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
