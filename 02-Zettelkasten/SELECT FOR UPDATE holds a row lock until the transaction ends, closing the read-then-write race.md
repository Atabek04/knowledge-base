---
created: 2026-06-12
tags: [postgresql, database, concurrency, locking, transactions]
aliases: [FOR UPDATE, locking read, SELECT FOR UPDATE]
---

When two requests read the same row, decide based on what they read, then write — they can both act on stale data. A booking handler that runs `SELECT` a free seat, then `UPDATE` it to taken, has a window between the read and the write where a second request reads the *same* still-free seat. Both claim it. One physical resource, two owners.

This is the **read-then-write race** — the anomaly it produces is a [[A lost update occurs when two transactions read a row then both write and the second write erases the first|lost update]], and wrapping the code in a plain transaction won't stop it because [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates|@Transactional defaults to READ COMMITTED]]. `SELECT ... FOR UPDATE` is PostgreSQL's row-level fix.

---

### The name tells you what it does

`SELECT ... FOR UPDATE` is a <mark style="background: #FFF3A3A6;">locking read</mark> — a read taken *for* a coming *update*.

A plain `SELECT` just reads. Adding `FOR UPDATE` signals write-intent: "I'm reading these rows because I'm about to change them, so lock them now as if I already had." It acquires the **same row lock a real `UPDATE` would**, but at read time — before you've written anything.

That closes the gap. The lock exists from the instant you read the row, so no one can slip a stale read in between your read and your write.

---

### The lock is row-level, not table-level

`FOR UPDATE` locks <mark style="background: #ABF7F7A6;">only the specific rows the query returned</mark> — not the table, not neighbouring rows.

Two requests claiming two *different* free seats in the same window never collide: different rows, independent locks. Contention happens only when two requests target the *same* row.

---

### The lock is held until the transaction ends

The lock is released on <mark style="background: #FFF3A3A6;">`COMMIT` or `ROLLBACK`</mark> — not when the row is updated, not at the end of the `SELECT` statement.

This is the crucial part. If the lock dropped right after the `SELECT`, a competitor could read the still-unchanged row during the gap before your `UPDATE` — the race returns. Holding it for the whole transaction means your read and your write are protected as one unit:

```sql
BEGIN;
SELECT slot_id FROM slot
WHERE unit_code = 'A' AND exam_type = 'B' AND start_ts = '10:00' AND status = 'OPEN'
LIMIT 1
FOR UPDATE;                                  -- lock the row now

UPDATE slot SET status = 'ASSIGNED' WHERE slot_id = 7;
COMMIT;                                       -- lock releases here
```

A second transaction's `FOR UPDATE` on the same row <mark style="background: #FFB8EBA6;">blocks until your `COMMIT`</mark>, then [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released|re-checks the now-updated row]] and sees `status = 'ASSIGNED'` — so it no longer qualifies and moves on. No double-claim.

---

### Read more

- [[A lost update occurs when two transactions read a row then both write and the second write erases the first]]
- [[Optimistic and pessimistic locking are two strategies for preventing lost updates]]
- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked]]
- [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue]]
- [[FOR UPDATE locks rows from every joined table unless you restrict it with OF]]
- [[FOR UPDATE locks rows beneath LIMIT and OFFSET in the query plan]]
- [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates]]
- [[PostgreSQL transactions wrap multiple operations in an atomic unit with automatic rollback on failure]]
- [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions]]
