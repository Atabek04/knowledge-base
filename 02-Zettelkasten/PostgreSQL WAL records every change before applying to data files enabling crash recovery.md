---
aliases: [WAL, write-ahead log, PostgreSQL WAL]
created: 2026-05-21
tags: [postgresql, database, storage, transactions]
---

### What WAL Is

The Write-Ahead Log is a sequential file where PostgreSQL records every change — INSERT, UPDATE, DELETE, COMMIT, ROLLBACK — **before** applying it to the actual data files.

---

### Why Write to WAL Before the Data File

Writing to data files is **random I/O** — jump to page 47, update 3 bytes, jump to page 1203. Slow.

Writing to WAL is **sequential** — always append to the end of one file. Fast.

PG's deal: write to WAL first → tell the client "committed" → update data files in the background. Net result: same durability guarantee, far fewer slow random writes.

---

### Crash Recovery: REDO and UNDO

WAL records both the change and whether the transaction completed. On restart after a crash, PG replays the WAL:

**Change + COMMIT present → REDO**: transaction finished but data file may not reflect it yet. PG reapplies the change.

**Change + no COMMIT → UNDO**: transaction never completed. PG discards those changes.

No manual intervention needed — PG reconstructs correct state automatically from the log.

---

### LSN — Position in the WAL

Every entry in the WAL has a **Log Sequence Number (LSN)** — a monotonically increasing position identifier. External tools like Debezium use LSNs to track exactly where they are in the log and resume after failure without missing or replaying events.

---

Read more:
- [[PostgreSQL - MOC]]
- [[Databases - MOC]]
- [[PostgreSQL transactions wrap multiple operations in an atomic unit with automatic rollback on failure]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]]
