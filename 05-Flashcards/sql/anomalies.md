TARGET DECK: Tech-KB::SQL::Anomalies
Tags: sql concurrency
**Chapter:** Concurrency anomalies
**Related:** [[Database Transactions & Concurrency - MOC]]

---

START
Coding Questions
What is a dirty read?
Back: A **dirty read** is reading another transaction's **uncommitted** ("dirty") changes — data that can still vanish on rollback.
- You act on a value that was never durably real
- If the writer rolls back, your decision rested on a value that never existed
Tags: sql concurrency anomaly
END

START
Coding Questions
What read-then-write pattern always produces a lost update?
Back: Two transactions both **read → decide → write** the same row concurrently.
- Both read the same value
- Both write based on it
- **Last writer wins** — the later COMMIT overwrites the earlier, silently erasing it
Tags: sql concurrency anomaly
END

START
Coding Questions
What is a lost update?
Back: A **lost update** is when one committed write is silently overwritten by another transaction that read the row *before* the first write existed.
- The earlier update "is lost" — clobbered with no error, no warning
- With no locking, the default is **last writer wins**
Tags: sql concurrency anomaly
END

START
Coding Questions
How does a lost update differ from a data race?
Back: Same shape of bug, different layer:
- **Data race** — threads + memory, defined by a language memory model (Go, JMM, C++)
- **Lost update** — transactions + a table row, defined by SQL isolation levels
- Both are kinds of **race condition** — but don't call a clobbered SQL row a "data race"
Tags: sql concurrency anomaly
END

START
Coding Questions
What is a non-repeatable read?
Back: A **non-repeatable read** — re-reading the same row inside one transaction returns a different value, because another transaction committed an `UPDATE`/`DELETE` to it in between.
- The read could not be *repeated* with the same result mid-transaction
Tags: sql concurrency anomaly
END

START
Coding Questions
What is a phantom read?
Back: A **phantom read** — re-running a query returns a different **set** of rows, because another transaction `INSERT`ed or `DELETE`d rows matching the `WHERE`.
- New rows "appear like ghosts" between two identical queries
Tags: sql concurrency anomaly
END

START
Coding Questions
How does a non-repeatable read differ from a phantom read?
Back: The distinction is *what* changed:
- **Non-repeatable read** — an existing row you already read changed **value** (UPDATE/DELETE)
- **Phantom read** — the **set of rows** matching your predicate grew or shrank (INSERT/DELETE)
- Non-repeatable = a held row's value; phantom = which rows qualify
Tags: sql concurrency anomaly
END
