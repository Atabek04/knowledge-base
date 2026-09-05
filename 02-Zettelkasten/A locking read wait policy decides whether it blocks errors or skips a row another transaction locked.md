---
created: 2026-06-12
tags: [database, sql, postgresql, concurrency, locking]
aliases: [wait policy, lock wait policy, NOWAIT, SKIP LOCKED]
---

A [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|locking read]] often reaches a row that another transaction has *already* locked. What should it do — wait, give up, or move on? SQL lets you choose with a **wait policy** appended to the locking clause.

The default is to wait, but two keywords override it. Picking the right one is the difference between a system that queues, one that fails fast, and one that flows around contention.

---

### Default — block and wait

With no keyword, a locking read that hits a locked row <mark style="background: #FFF3A3A6;">blocks until the lock is released</mark>, then proceeds (re-checking the row first — see [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released|EvalPlanQual]]).

Right when you *must* process that specific row and waiting is acceptable — transferring money to account #42, not "some account."

---

### NOWAIT — fail fast with an error

```sql
SELECT ... FOR UPDATE NOWAIT;
```

Instead of waiting, it <mark style="background: #FFB8EBA6;">raises an error immediately</mark> (`55P03 lock_not_available`) the moment a target row is locked. The name says it: **no wait** — don't queue, surface the conflict now.

Right for interactive "someone else is editing this record" UX, where blocking the user is worse than telling them to retry.

---

### SKIP LOCKED — step over locked rows

```sql
SELECT ... FOR UPDATE SKIP LOCKED;
```

It <mark style="background: #ABF7F7A6;">silently omits any row it cannot lock immediately</mark> and returns only the rows it *could* lock. No wait, no error — just a smaller result set. The name says it: **skip** what's **locked**, keep going.

Right when the rows are interchangeable and you only need *some* free one, not a specific row — the basis of the [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue|competing-consumers queue]].

---

### Choosing

| Policy | Locked row → | Use when |
|---|---|---|
| default (block) | wait for it | you need *that* row, waiting is fine |
| `NOWAIT` | error now | a human is waiting; fail fast beats blocking |
| `SKIP LOCKED` | skip it | rows are interchangeable; grab any free one |

<mark style="background: #FFF3A3A6;">One deliberate trade-off:</mark> `SKIP LOCKED` returns an *intentionally incomplete* view — it hides rows that exist but are busy. That's a bug for reporting and a feature for queues.

---

### Read more

- [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released]]
