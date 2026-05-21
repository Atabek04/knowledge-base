---
aliases: [Debezium, CDC, change data capture]
created: 2026-05-21
tags: [debezium, cdc, kafka, postgresql, data-engineering]
---

### What Debezium Does

Debezium is a Change Data Capture (CDC) tool. It connects to PostgreSQL, tails the WAL like `tail -f`, and streams every committed change to Kafka — without any changes to application code.

---

### How It Tracks Progress: LSN Offsets

Every WAL entry has a **Log Sequence Number (LSN)** — a monotonically increasing position identifier.

```
LSN 100: INSERT orders id=1
LSN 101: UPDATE items stock=9
LSN 102: INSERT orders id=2
```

After processing each batch, Debezium saves the last processed LSN to a Kafka topic (the offset store). On restart it reads that offset and tells PG: "give me everything after LSN 102." No gaps, no replays.

---

### Replication Slot: No WAL Entries Lost

PG uses a **replication slot** to guarantee WAL entries are retained until Debezium confirms it has read them. Even if Debezium is offline for hours, PG holds the WAL entries — nothing is lost.

---

### Failure and Retry

On DB connection failure, Debezium throws a retriable exception → Kafka Connect restarts the connector → resumes from last saved LSN.

Default guarantee: **at-least-once** — the same event may be published twice if Debezium crashes after publishing but before saving the offset. Consumers must be idempotent.

Exactly-once is available with Kafka Connect 3.3+ but requires extra configuration.

---

### What Debezium Events Look Like

Raw WAL changes — DB column names and types exposed directly:

```json
{ "op": "c", "after": { "id": 123, "user_id": 1, "status": "pending" } }
```

This leaks DB schema to consumers. Use the Outbox pattern on top of Debezium when clean business event contracts are needed.

---

Read more:
- [[Microservices Patterns - MOC]]
- [[PostgreSQL WAL records every change before applying to data files enabling crash recovery]]
- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction]]
- [[Kafka delivers messages at-least-once by default and exactly-once with atomic offset commits]]
