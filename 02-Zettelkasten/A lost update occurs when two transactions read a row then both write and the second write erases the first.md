---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, anomaly]
aliases: [lost update, lost update anomaly]
---

When two transactions touch the same row concurrently, the database has to decide whose change wins. Without locking the answer is simply **last writer wins** — whichever `UPDATE` commits last overwrites the other. A **lost update** is that failure mode: one change silently disappears, clobbered by a transaction that never saw it.

It is the anomaly behind double-booking, double-spending, and inventory going negative.

---

### What makes the update "lost"

The pattern is always **read → decide → write**, run by two transactions at once — call them `T1` (Ali) and `T2` (Umar), each withdrawing from the same account. Top-to-bottom is time order:

```SQL
T1: SELECT balance FROM account WHERE id=1;        -- reads 100
T2: SELECT balance FROM account WHERE id=1;        -- reads 100 (same, stale)
T1: UPDATE account SET balance=100-30 WHERE id=1;  -- writes 70
T2: UPDATE account SET balance=100-50 WHERE id=1;  -- writes 50
```

Both read `100`. Ali's withdrawal of 30 should leave 70, then Umar's 50 should leave 20. Instead Umar's write (based on the stale `100`) lands last and stores `50`. <mark style="background: #FFB8EBA6;">Ali's update is lost</mark> — overwritten as if it never happened.

The name is literal: an update that did commit gets *lost* because a second writer clobbered it with a value computed from data read *before* the first update existed.

#### Related but distinct: data race

You might reach for the term "data race" here — close, but it names a different layer. A <mark style="background: #FFF3A3A6;">data race</mark> is the threads-and-memory version: two threads hit the same memory location unsynchronized, at least one writing, defined by a language memory model (Go, the JMM, C++). A <mark style="background: #FFF3A3A6;">lost update</mark> is the transaction-and-row version, defined by SQL isolation levels.

Both are kinds of <mark style="background: #ABF7F7A6;">race condition</mark> — same shape of bug, different layer. Don't call a clobbered SQL row a "data race"; the rows are a lost update, the two app threads racing in memory would be the data race.

---

### Why a plain transaction does not stop it

Both transactions are individually valid — each read a *committed* value and wrote correctly from it. Nothing was dirty, nothing was rolled back.

The default [[Isolation levels are defined by which read anomalies they permit|isolation level, `READ COMMITTED`]], only guarantees you never read *uncommitted* data. It says nothing about two readers racing to write. So wrapping the code in a transaction alone — including Spring's [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates|@Transactional, whose default isolation is READ COMMITTED]] — does **not** prevent a lost update.

---

### How to prevent it

There are [[Optimistic and pessimistic locking are two strategies for preventing lost updates|two strategy families]], differing in *when* they handle the conflict:

- **Pessimistic** — take a [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|locking read with `FOR UPDATE`]] so the second reader blocks until the first commits, then sees the fresh value.
- **Optimistic** — let both read freely but reject the stale writer at write time using a version check, like [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions|the ETag version-compare on the web side]].

<mark style="background: #ABF7F7A6;">Pessimistic locks up front; optimistic detects the conflict at the end and retries.</mark> A third option is simply raising the [[Isolation levels are defined by which read anomalies they permit|isolation level]] to `REPEATABLE READ`, which aborts the losing writer.

---

### Read more

- [[Optimistic and pessimistic locking are two strategies for preventing lost updates]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[Isolation levels are defined by which read anomalies they permit]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates]]
- [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions]]
