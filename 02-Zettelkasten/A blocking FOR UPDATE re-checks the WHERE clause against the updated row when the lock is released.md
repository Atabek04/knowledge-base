---
created: 2026-06-12
tags: [postgresql, database, concurrency, locking, transactions]
aliases: [EvalPlanQual, EPQ, lock re-check]
---

When a `SELECT ... FOR UPDATE` tries to lock a row another transaction already holds, it blocks and waits. The interesting question is what happens *after* the holder commits and the waiter finally wakes up — because by then the row may have changed.

PostgreSQL does not blindly hand back the row that matched when the query first started. It re-examines it.

---

### Block, then re-check on wake

Under `READ COMMITTED`, a freed locking read re-fetches the **latest committed version** of the row and <mark style="background: #FFF3A3A6;">re-runs the query's `WHERE` against it</mark>. If the row no longer matches, it is dropped from the result.

Two transactions compete for the same free seat — `T1` (Ali) and `T2` (Umar). Top-to-bottom is time order:

```
T1: SELECT ... WHERE status='OPEN' LIMIT 1 FOR UPDATE;  -- locks row 7
T2: SELECT ... WHERE status='OPEN' LIMIT 1 FOR UPDATE;  -- row 7 locked → BLOCKS
T1: UPDATE slot SET status='ASSIGNED' WHERE slot_id=7;
T1: COMMIT;                                             -- T2 wakes
T2: re-checks row 7: status='ASSIGNED' ≠ 'OPEN' → dropped → returns 0 rows
```

Umar waited for row 7, then correctly got **nothing** — not a stale claim on a seat that is no longer open. This re-check is why blocking `FOR UPDATE` never double-claims.

---

### The mechanism has a name: EvalPlanQual

PostgreSQL calls this re-evaluation <mark style="background: #ABF7F7A6;">EvalPlanQual</mark> (EPQ) — it re-evaluates the plan's qualifiers against the freshly-updated row before deciding to lock and return it.

Reading the name backwards explains it: *evaluate* the *plan*'s *qual*ifiers, again, on the new row version.

---

### Only READ COMMITTED re-checks silently

This automatic re-check is a `READ COMMITTED` behavior. At [[PostgreSQL enforces stricter isolation than the SQL standard requires|higher isolation]], PostgreSQL refuses to silently swap in a newer row version:

> Under `REPEATABLE READ` or `SERIALIZABLE`, the waiter instead aborts with <mark style="background: #FFB8EBA6;">`could not serialize access due to concurrent update`</mark> and the transaction must retry.

Same safety guarantee, two different failure styles: <mark style="background: #ABF7F7A6;">re-check-and-continue at READ COMMITTED, error-and-retry above it.</mark>

---

### Read more

- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked]]
- [[PostgreSQL enforces stricter isolation than the SQL standard requires]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates]]
