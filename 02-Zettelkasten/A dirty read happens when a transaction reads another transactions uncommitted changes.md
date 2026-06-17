---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, anomaly]
aliases: [dirty read]
---

When transactions run concurrently, one of them can peek at data a neighbour has written but not yet committed. If the neighbour later rolls back, that data never officially existed — yet you already read it and maybe acted on it.

That is a **dirty read**: reading "dirty" (uncommitted) data.

---

### Why "dirty" means uncommitted

A value a transaction has written but not yet committed is <mark style="background: #FFF3A3A6; font-weight: bold;">dirty</mark> — provisional, not durable, still capable of vanishing on rollback. Reading it means trusting a number that has no guarantee of ever becoming real.

```SQL
T1: UPDATE account SET balance=500 WHERE id=1;   -- not committed yet
T2: SELECT balance FROM account WHERE id=1;       -- reads 500 (dirty!)
T1: ROLLBACK;                                      -- the 500 never existed
```

Umar's transaction (`T2`) read `500` and may have approved a withdrawal on it. Ali (`T1`) then rolled back — the balance was never `500`. The decision was made on a phantom value.

---

### PostgreSQL never allows dirty reads

This is the one anomaly PostgreSQL forbids at <mark style="background: #ABF7F7A6;">every isolation level</mark>. Even if you ask for `READ UNCOMMITTED`, PostgreSQL silently upgrades it to `READ COMMITTED` — its lowest *real* level still hides uncommitted data.

So in PostgreSQL a dirty read is mostly a *definitional baseline*: it's the anomaly the weakest usable level already prevents, the floor that [[Isolation levels are defined by which read anomalies they permit|the isolation levels]] build up from.

---

### Read more

- [[Isolation levels are defined by which read anomalies they permit]]
- [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update]]
- [[A lost update occurs when two transactions read a row then both write and the second write erases the first]]
