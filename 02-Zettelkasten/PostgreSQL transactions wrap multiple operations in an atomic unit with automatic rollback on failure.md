---
aliases: [PostgreSQL transactions, BEGIN COMMIT, database transaction]
created: 2026-05-21
tags: [postgresql, database, transactions, acid]
---

### The Problem Transactions Solve

Without transactions, two concurrent users can read stale state and both proceed with an operation that should only succeed for one — a data race.

Example: two users buy the last item in stock simultaneously. Both read `stock = 1`, both proceed. Result: `stock = -1`.

---

### How Transactions Fix This

A transaction wraps multiple operations into a single atomic unit — **all succeed or all fail**, with no partial state visible to other queries.

```sql
BEGIN;
  INSERT INTO orders (user_id, item_id) VALUES (1, 42);
  UPDATE items SET stock = stock - 1 WHERE id = 42;
COMMIT; -- both writes visible at once
```

If anything fails between `BEGIN` and `COMMIT`, issue `ROLLBACK` — PG reverses all changes as if they never happened.

---

### Row-Level Locking

To prevent the concurrent stock race, acquire a lock before reading:

```sql
BEGIN;
  SELECT stock FROM items WHERE id = 42 FOR UPDATE; -- locks the row
  -- other transactions wait here
  UPDATE items SET stock = stock - 1 WHERE id = 42;
COMMIT; -- lock released
```

The second buyer waits at the lock, then re-reads `stock = 0` after the first transaction commits — and aborts cleanly.

---

### Automatic Crash Recovery

If the server crashes mid-transaction, PG uses the [[PostgreSQL WAL records every change before applying to data files enabling crash recovery|WAL]] to detect the incomplete transaction on restart and rolls it back automatically. No manual cleanup required.

---

### ClickHouse Has No Equivalent

ClickHouse supports only single-INSERT atomicity. There is no `BEGIN/COMMIT` across multiple statements. This is the core reason transactional workloads belong in PostgreSQL, not ClickHouse.

---

Read more:
- [[PostgreSQL - MOC]]
- [[Databases - MOC]]
- [[PostgreSQL WAL records every change before applying to data files enabling crash recovery]]
- [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics]]
