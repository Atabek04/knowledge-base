---
aliases: [Outbox pattern, transactional outbox]
created: 2026-05-21
tags: [microservices, patterns, messaging, kafka]
---

### The Problem It Solves

Writing to a database and then publishing an event to Kafka are two separate operations. If the app crashes between them, the event is lost — the DB has the change but the downstream system never hears about it.

---

### How It Works

Write the event to an `outbox` table **inside the same business transaction**:

```sql
BEGIN;
  INSERT INTO orders (id, user_id, item_id) VALUES (123, 1, 42);
  INSERT INTO outbox (payload) VALUES ('{"event":"OrderPlaced","orderId":123}');
COMMIT; -- both rows committed atomically, or neither
```

A separate **publisher process** reads the outbox and forwards to Kafka. On success it marks the row as processed. On failure it retries with exponential backoff.

---

### Delivery Guarantee

The business change and the outbox row are atomic — they either both persist or both disappear. The publisher retries until Kafka confirms receipt. Result: **at-least-once delivery** — no events lost, occasional duplicates on retry.

Consumers must be idempotent (or use `ReplacingMergeTree` in ClickHouse) to handle duplicates safely.

---

### Two Publisher Implementations

**Polling publisher** — queries `WHERE processed = false` on a schedule. Simple but adds DB load and introduces latency proportional to poll interval.

**Transaction log tailing (Debezium)** — reads the outbox table changes directly from the WAL. Instant notification, zero polling overhead. See [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]].

---

### Outbox vs Pure CDC

| | Outbox | Debezium (pure CDC) |
|---|---|---|
| Event shape | Full control — business events | Raw DB column changes |
| App changes needed | Yes — write to outbox table | No |
| Schema leakage | None | Exposes DB internals to consumers |
| Multi-app DBs | Only your app's events | Captures all writers |

Choose Outbox when event semantics and clean contracts matter. Choose pure CDC for legacy systems or minimal intrusion.

---

Read more:
- [[Microservices Patterns - MOC]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]]
- [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics]]
- [[Kafka delivers messages at-least-once by default and exactly-once with atomic offset commits]]
