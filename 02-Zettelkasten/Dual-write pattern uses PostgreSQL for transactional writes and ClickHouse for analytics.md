---
aliases: [dual-write, dual-write pattern]
created: 2026-05-21
tags: [clickhouse, postgresql, architecture, data-engineering]
---

### Why Neither Database Alone Is Enough

**PostgreSQL** handles transactional workloads — ACID guarantees, row-level locking, multi-statement `BEGIN/COMMIT`. Poor fit for aggregating billions of rows.

**ClickHouse** handles analytical workloads — columnar storage, vectorized execution, sub-second aggregations over billions of rows. No multi-statement transactions, expensive mutations.

Systems that need both operational consistency and real-time analytics require both.

---

### The Naive Approach and Its Failure

```
app → INSERT into PG  ✓
app → INSERT into CH  ✗ (network drop, crash)
```

PG has the record. CH doesn't. Analytics are silently wrong — **data drift**.

---

### The Solution: Reliable Event Delivery

The app must never write directly to CH. Instead it writes to PG, and a reliable pipeline carries changes to CH:

```
app → PG (transactional write)
        ↓
      pipeline (Outbox or CDC)
        ↓
      Kafka
        ↓
      CH consumer → INSERT
```

Two patterns implement the pipeline:

**Outbox pattern** — app writes to an `outbox` table in the same PG transaction. A process reads and forwards to Kafka. Gives full control over event shape.

**Debezium (CDC)** — reads PG's WAL directly and streams every committed change to Kafka. No app changes needed.

---

### Preventing Data Drift

- **At-least-once delivery** — Debezium/outbox may send duplicates on retry. CH's `ReplacingMergeTree` handles duplicates naturally via version column.
- **Order guaranteed** — WAL events arrive in commit order; Kafka preserves order within a partition.
- **No missed writes** — PG replication slot holds WAL entries until Debezium confirms delivery.

---

Read more:
- [[ClickHouse - MOC]]
- [[Databases - MOC]]
- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]]
- [[ReplacingMergeTree deduplicates rows on merge using ORDER BY key and optional version column]]
