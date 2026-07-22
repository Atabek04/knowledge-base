TARGET DECK: Tech-KB::SQL::Locking
Tags: sql concurrency locking
**Chapter:** Locking strategies
**Related:** [[Database Transactions & Concurrency - MOC]]

---

START
Coding Questions
What does SELECT ... FOR UPDATE do, and when is the lock released?
Back: A **locking read** — it takes the same row-level write lock an `UPDATE` would, but at read time ("a read taken *for* a coming *update*").
- Held until **COMMIT or ROLLBACK** — not at statement end, not when the row is updated
- Spanning read + write as one unit closes the read-then-write race
Tags: sql postgresql locking
<!--ID: 1782128730565-->
END

START
Coding Questions
Does FOR UPDATE take a row-level or table-level lock?
Back: **Row-level** — it locks only the specific rows the query returned.
- Two requests claiming different rows never collide
- Contention occurs only when two target the **same** row
Tags: sql postgresql locking
<!--ID: 1782128730568-->
END

START
Coding Questions
When a blocking FOR UPDATE wakes up after the lock holder commits (READ COMMITTED), what does it do?
Back: It runs **EvalPlanQual** — re-fetches the **latest committed** version of the row and re-runs the query's `WHERE` against it.
- If the row no longer matches, it is dropped from the result
- This re-check is why blocking FOR UPDATE never double-claims
Tags: sql postgresql locking
<!--ID: 1782128730570-->
END

START
Coding Questions
How does the EvalPlanQual re-check differ between READ COMMITTED and REPEATABLE READ?
Back:
- **READ COMMITTED** — silently re-checks the new row version and continues
- **REPEATABLE READ / SERIALIZABLE** — aborts with `could not serialize access`, transaction must retry
- Same safety guarantee, different failure style: re-check vs error-and-retry
Tags: sql postgresql locking
<!--ID: 1782128730572-->
END

START
Coding Questions
What is the difference between optimistic and pessimistic locking?
Back: They differ in **when** they handle the conflict:
- **Pessimistic** — assume a clash, **lock first** (`FOR UPDATE`); others wait
- **Optimistic** — assume no clash, take **no lock**; verify a version at write time, reject and retry if it moved
Tags: sql concurrency locking
<!--ID: 1782128730574-->
END

START
Coding Questions
When would you choose optimistic vs pessimistic locking?
Back: By how often writers actually collide:
- **High contention** → **pessimistic** — blocking up front beats constant retries
- **Low contention** → **optimistic** — skip the lock; the rare retry is cheaper than locking everyone
Tags: sql concurrency locking
<!--ID: 1782128730577-->
END

START
Coding Questions
What are the three wait policies for a locking read when it hits an already-locked row?
Back:
- **default** — **block** and wait until the lock frees
- **NOWAIT** — **error immediately** (`55P03 lock_not_available`)
- **SKIP LOCKED** — **skip** the locked row and return the rest
Tags: sql postgresql locking
<!--ID: 1782128730579-->
END

START
Coding Questions
How does SKIP LOCKED differ from NOWAIT?
Back: Both avoid waiting, but differently:
- **NOWAIT** — throws an error the moment a target row is locked
- **SKIP LOCKED** — silently omits locked rows, returning a smaller result set (no error)
- SKIP LOCKED deliberately returns an **incomplete** view
Tags: sql postgresql locking
<!--ID: 1782128730582-->
END

START
Coding Questions
What does the SELECT FOR UPDATE SKIP LOCKED idiom achieve, and what is it called?
Back: It turns a table into a **competing-consumers** work queue:
- Each worker locks the **next free** row, skipping ones being claimed
- **No blocking, no double-claim, full parallelism**
- Used for job queues, order processing, seat reservation, outbox, pool checkout
Tags: sql postgresql locking pattern
<!--ID: 1782128730584-->
END

START
Coding Questions
In a FOR UPDATE query that joins tables, which rows get locked, and how do you restrict it?
Back: By default, rows from **every** table contributing to the result are locked.
- A join silently locks the other tables too → accidental contention
- Use `FOR UPDATE OF <table>` to lock only the named table(s)
Tags: sql postgresql locking
<!--ID: 1782128730586-->
END

START
Coding Questions
What three surprises arise when combining FOR UPDATE with LIMIT and OFFSET?
Back: The lock step runs **beneath** LIMIT/OFFSET in the plan:
- **OFFSET-skipped rows still get locked** (`OFFSET 10 LIMIT 5` locks ~15)
- Without **ORDER BY**, which rows get locked is unpredictable
- Plain `LIMIT 1 FOR UPDATE` funnels all workers onto the same row → add **SKIP LOCKED** to spread them
Tags: sql postgresql locking
<!--ID: 1782128730588-->
END

START
Coding Questions
Why must you never make an external HTTP call inside a @Transactional method?
Back: A `@Transactional` method holds its **DB connection and row locks** from open until the method returns.
- An HTTP call inside makes lock duration = your write + **the other service's latency** (which you don't control)
- Slow/hung dependency → locks pile up, connections stay checked out, **pool drains**, whole service freezes
- Rule: read + call external **before** opening the transaction; wrap only local writes
Tags: sql spring transactions locking
END

START
Coding Questions
What is the correct ordering to avoid holding a lock during an external call?
Back: **read → external call (no tx) → open tx → write → commit.**
- The external latency runs on your thread with **zero DB resources held**
- The transaction opens and commits in milliseconds around the write only
Tags: sql spring transactions locking
END

START
Coding Questions
Why does splitting the external call and the write into the same bean break the @Transactional fix?
Back: **Self-invocation bypasses the Spring proxy.**
- `@Transactional` is applied by a proxy wrapping the bean; a `this.method()` call skips it → annotation silently ignored, no transaction starts
- Fix: put the write method in a **separate bean**, or use a `TransactionTemplate`
Tags: sql spring transactions locking
END

START
Coding Questions
When does a JPA @Lock(PESSIMISTIC_WRITE) release its lock, and how?
Back: **Automatically at transaction end** — `COMMIT` or `ROLLBACK`.
- No separate query, no unlock statement; the lock's lifetime *is* the transaction's
- `@Lock` only appends `FOR UPDATE` to the generated `SELECT` — that's its whole mechanism
Tags: sql spring jpa locking
END

START
Coding Questions
Why does @Lock(PESSIMISTIC_WRITE) do nothing without an open @Transactional?
Back: The lock's release point **is** the transaction boundary — with no transaction, there's nothing for it to live inside.
- No active tx → Hibernate throws, or applies `FOR UPDATE` to an auto-commit statement that releases instantly → no protection
- Corollary: a long transaction = a long-held lock; you control release by tx duration, not a call
Tags: sql spring jpa locking
END
