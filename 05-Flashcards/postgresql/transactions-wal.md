TARGET DECK: Tech-KB::PostgreSQL::Transactions and WAL
Tags: postgresql database
**Chapter:** Transactions & Isolation
**Related:** [[PostgreSQL - MOC]]

---

START
Coding Questions
What is the PostgreSQL WAL, and why does PG write to it before updating data files?
Back:
**WAL (Write-Ahead Log)** is a sequential file where PG records every change — INSERT, UPDATE, DELETE, COMMIT, ROLLBACK — **before** applying it to data files.

**Why write first?**
- Data file writes = **random I/O** (jump to page 47, then 1203...) → slow
- WAL writes = **sequential** (always append) → fast

PG's deal: write to WAL → tell client "committed" → update data files in background.
Same durability, far fewer slow random writes.
Tags: postgresql wal storage
END

START
Coding Questions
How does PostgreSQL use the WAL to recover after a crash? What are REDO and UNDO?
Back:
On restart, PG replays the WAL and handles two cases:

**Change + COMMIT present → REDO**
Transaction finished but data file may not reflect it yet. PG reapplies the change.

**Change + no COMMIT → UNDO**
Transaction never completed. PG discards those changes.

No manual intervention — PG reconstructs correct state automatically from the log.
Tags: postgresql wal transactions
END

START
Coding Questions
What is an LSN in PostgreSQL, and what is it used for externally?
Back:
**LSN (Log Sequence Number)** — a monotonically increasing position identifier for every entry in the WAL.

```
LSN 100: INSERT orders id=1
LSN 101: UPDATE items stock=9
```

External tools like **Debezium** use LSNs to track exactly where they are in the WAL — on restart, they resume from the last saved LSN without missing or replaying events.
Tags: postgresql wal cdc
END

START
Coding Questions
What problem do PostgreSQL transactions solve, and what is the atomicity guarantee?
Back:
**Problem**: without transactions, concurrent users can read stale state and both proceed with an operation that should only succeed for one — a **data race**.

Example: two users buy the last item. Both read `stock = 1`, both proceed → `stock = -1`.

**Transaction** wraps multiple operations into one atomic unit — **all succeed or all fail**:
```sql
BEGIN;
  INSERT INTO orders ...;
  UPDATE items SET stock = stock - 1 WHERE id = 42;
COMMIT;
```
No partial state is ever visible to other queries.
Tags: postgresql transactions acid
END

START
Coding Questions
How does `SELECT ... FOR UPDATE` prevent a data race in PostgreSQL?
Back:
`FOR UPDATE` acquires a **row-level lock** before reading:

```sql
BEGIN;
  SELECT stock FROM items WHERE id = 42 FOR UPDATE; -- locks the row
  UPDATE items SET stock = stock - 1 WHERE id = 42;
COMMIT; -- lock released
```

The second buyer **waits at the lock**, then re-reads `stock = 0` after the first transaction commits — and aborts cleanly.

Lock scope: held from `SELECT FOR UPDATE` until `COMMIT` or `ROLLBACK`.
Tags: postgresql transactions locking
END

START
Coding Questions
Why can't ClickHouse replace PostgreSQL for transactional workloads?
Back:
ClickHouse supports only **single-INSERT atomicity** — there is no `BEGIN/COMMIT` across multiple statements.

Adding multi-statement transaction locks would require **global coordination** between writers — directly contradicting CH's lock-free, high-throughput insert model.

CH chose **OLAP** (analytical reads, bulk inserts) over **OLTP** (transactional consistency, row-level updates).
This is the core reason transactional workloads belong in PostgreSQL.
Tags: postgresql clickhouse transactions
END
