---
created: 2026-06-12
tags: [database, sql, postgresql, concurrency, locking]
aliases: [FOR UPDATE LIMIT, LIMIT locking]
---

`SELECT ... LIMIT 1 FOR UPDATE` looks like "lock one row." But in the query plan the locking step runs **beneath** `LIMIT` and `OFFSET` — rows are locked as they are produced, and only then does `LIMIT` cut the result. That ordering produces three surprises worth knowing before you build anything on it.

---

### OFFSET-skipped rows still get locked

Locking happens *before* `OFFSET` discards rows, so:

```sql
SELECT ... FROM job OFFSET 10 LIMIT 5 FOR UPDATE;   -- locks ~15 rows, returns 5
```

<mark style="background: #FFB8EBA6;">The 10 rows you paged past are locked too</mark>, even though they never appear in your result. Paging with `FOR UPDATE` quietly locks everything up to your window, not just the window.

---

### Without ORDER BY, which rows lock is unpredictable

`LIMIT` without `ORDER BY` lets the planner return *any* matching rows, and the plan can change with different `LIMIT`/`OFFSET` values. So *which* rows get locked is non-deterministic. <mark style="background: #ABF7F7A6;">Always add `ORDER BY` to make the locked set predictable</mark> (and the queue pull order fair).

---

### Plain LIMIT funnels concurrent readers onto the same row

Because the lock step sits under `LIMIT`, a blocking `LIMIT 1 FOR UPDATE` pulls the first matching row, tries to lock it, and **blocks there** if another session holds it — it does *not* move on to the free rows behind it. Ten workers all pile onto row 1.

This is exactly why the [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue|queue idiom needs `SKIP LOCKED`]]: skipped rows don't count toward the `LIMIT`, so each worker walks past the busy rows and locks the next *free* one. <mark style="background: #FFF3A3A6; font-weight: bold;">`LIMIT` alone funnels; `LIMIT` + `SKIP LOCKED` spreads.</mark>

---

### Read more

- [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue]]
- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked]]
- [[FOR UPDATE locks rows from every joined table unless you restrict it with OF]]
