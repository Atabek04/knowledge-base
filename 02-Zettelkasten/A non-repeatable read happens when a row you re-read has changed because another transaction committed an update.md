---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, anomaly]
aliases: [non-repeatable read]
---

Inside a single transaction you read a row, do some work, then read the *same row again* — and the value is different. A concurrent transaction updated and committed it in between. Your read was not **repeatable**: the same query gave two answers within one transaction.

---

### Same query, same row, two different values

```SQL
T1: SELECT balance FROM account WHERE id=1;   -- reads 100
T2: UPDATE account SET balance=300 WHERE id=1; COMMIT;
T1: SELECT balance FROM account WHERE id=1;   -- reads 300  ← not repeatable
```

Ali's transaction (`T1`) never changed the row, yet saw `100` then `300`. The name is literal: the read could not be <mark style="background: #FFF3A3A6;">repeated</mark> with the same result inside one transaction, because Umar (`T2`) committed an update to that existing row in the gap.

---

### Non-repeatable read vs phantom read

These two get confused constantly. The difference is **what changed**:

- **Non-repeatable read** — an existing row you already read had its *value changed* (an `UPDATE`/`DELETE` to a row in your result).
- A [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones|phantom read]] — the *set of rows* matching your `WHERE` grew or shrank (an `INSERT`/`DELETE` adding or removing matching rows).

<mark style="background: #ABF7F7A6;">Non-repeatable = a row you held changed value. Phantom = which rows qualify changed.</mark>

---

### Prevented from REPEATABLE READ upward

`READ COMMITTED` allows non-repeatable reads — each statement sees a fresh snapshot. From [[Isolation levels are defined by which read anomalies they permit|`REPEATABLE READ` upward]] the whole transaction reads from one frozen snapshot, so a re-read always returns the original value regardless of what others commit.

---

### Read more

- [[A phantom read happens when a re-run query returns new rows because another transaction inserted matching ones]]
- [[A dirty read happens when a transaction reads another transactions uncommitted changes]]
- [[Isolation levels are defined by which read anomalies they permit]]
