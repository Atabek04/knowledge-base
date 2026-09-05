---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, anomaly]
aliases: [phantom read]
---

You run a query that returns a *set* of rows matching some condition. Later in the same transaction you run it again — and extra rows have appeared, or some vanished. A concurrent transaction inserted or deleted rows matching your `WHERE`. The newcomers are **phantoms**.

---

### The row set changes, not one row's value

```SQL
T1: SELECT count(*) FROM slot WHERE status='OPEN';   -- 5 rows
T2: INSERT INTO slot (status) VALUES ('OPEN'); COMMIT;
T1: SELECT count(*) FROM slot WHERE status='OPEN';   -- 6 rows  ← a phantom appeared
```

Ali's transaction (`T1`) asked the same question twice and got `5` then `6`. No row Ali already read changed value — instead the *membership* of the result set changed because Umar (`T2`) inserted a new matching row.

---

### Why "phantom"

The extra rows <mark style="background: #FFF3A3A6;">appear and disappear like ghosts</mark> between two identical queries — present the second time though absent the first, with nothing you did to summon them. That ghostly entrance into a predicate's result set is the phantom.

This is the boundary with a [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update|non-repeatable read]]: that one is an existing row changing *value*; a phantom is the *set of qualifying rows* changing size.

---

### PostgreSQL prevents phantoms early

The [[Isolation levels are defined by which read anomalies they permit|SQL standard]] only requires phantoms to be gone at `SERIALIZABLE`. PostgreSQL is stricter: because [[PostgreSQL enforces stricter isolation than the SQL standard requires|`REPEATABLE READ` uses snapshot isolation]], the whole transaction reads one frozen snapshot, so <mark style="background: #ABF7F7A6;">no phantoms appear at `REPEATABLE READ` either</mark> — earlier than the spec demands.

---

### Read more

- [[A non-repeatable read happens when a row you re-read has changed because another transaction committed an update]]
- [[A dirty read happens when a transaction reads another transactions uncommitted changes]]
- [[Isolation levels are defined by which read anomalies they permit]]
- [[PostgreSQL enforces stricter isolation than the SQL standard requires]]
