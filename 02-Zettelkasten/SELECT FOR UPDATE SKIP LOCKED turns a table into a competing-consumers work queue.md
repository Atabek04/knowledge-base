---
created: 2026-06-12
tags: [database, sql, postgresql, concurrency, locking, patterns]
aliases: [competing consumers, SELECT FOR UPDATE SKIP LOCKED, job queue pattern, skip locked queue]
---

You have a table of pending work — jobs, orders, free seats — and many workers pulling from it at once. Each worker must claim a **different** row, with no two grabbing the same one, and without workers stalling in line behind each other. Combining a locking read with the `SKIP LOCKED` wait policy gives exactly this, turning an ordinary table into a concurrent queue.

This is the **competing-consumers** idiom: many consumers competing for items from one shared source, each taking a distinct item.

---

### Why plain FOR UPDATE is not enough

A plain blocking [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|`FOR UPDATE`]] is *safe* — no double-claim — but it **serializes** the workers. Each one that targets a locked row waits for the holder to commit, then [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released|re-checks and often finds the row gone]]. Ten workers degrade into a single-file line, each waiting its turn just to discover the row was taken.

You don't want them to wait for *that* row — you want them to grab the *next free* one.

---

### The idiom

```sql
SELECT id FROM job
WHERE status = 'PENDING'
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 1;
-- then UPDATE status='RUNNING' (or process) and COMMIT
```

The [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked|`SKIP LOCKED` wait policy]] makes each worker <mark style="background: #ABF7F7A6;">step over the rows other workers are mid-claiming</mark> and lock the next un-locked match instead. `LIMIT 1` takes one; `ORDER BY` keeps the pull order fair.

Result: <mark style="background: #FFF3A3A6;">no blocking, no double-claim, full parallelism</mark>. Ten workers grab ten different rows simultaneously.

---

### Where the same idiom shows up

The shape — interchangeable rows, many claimers, grab-the-next-free — recurs everywhere:

- **Background job queue** — workers pulling tasks to run.
- **Payment / order processing** — one consumer per order, no double-charge.
- **Ticket or seat reservation** — concert, airline, or the ЦОН exam-seat check-in.
- **Outbox pattern** — publishers each claiming distinct unsent events.
- **Resource pool checkout** — threads leasing one free connection or license each.

<mark style="background: #FFB8EBA6;">Reach for it whenever "next available, exactly once, no waiting" describes the need.</mark>

---

### Read more

- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked]]
- [[FOR UPDATE locks rows beneath LIMIT and OFFSET in the query plan]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[A blocking FOR UPDATE re-checks the WHERE clause against the updated row when the lock is released]]
