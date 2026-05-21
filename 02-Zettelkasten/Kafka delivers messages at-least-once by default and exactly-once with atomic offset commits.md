---
aliases: [Kafka delivery guarantees, at-least-once, exactly-once, Kafka offsets]
created: 2026-05-21
tags: [kafka, messaging, distributed-systems]
---

### Kafka Offsets

Every message in a Kafka topic has a sequential **offset** — its position within a partition. Consumers track which offset they have processed. On restart, a consumer reads its last saved offset and resumes from there.

---

### At-Least-Once Delivery (Default)

The failure scenario:

1. Consumer reads message at offset 50, processes it ✓
2. Consumer crashes **before saving offset 50**
3. Restarts — last saved offset is 49
4. Processes offset 50 again → **duplicate**

No messages are lost, but the same message may be processed more than once.

**Solution**: make consumers idempotent. In ClickHouse, `ReplacingMergeTree` handles duplicate inserts naturally via the version column.

---

### Exactly-Once Delivery

Kafka atomically commits "message processed + offset saved" as one transaction — no window for the failure scenario above.

Requires:
- Kafka Connect in distributed mode
- Kafka Connect version 3.3+
- Explicit configuration

Rarely needed if the consumer is already idempotent. Most teams use at-least-once + idempotent consumers.

---

### At-Least-Once Is Not a Bug

"At-least-once" is a deliberate design — it prioritises **no data loss** over **no duplicates**. A lost message is usually worse than a duplicate that an idempotent consumer silently discards.

---

Read more:
- [[Distributed Systems - MOC]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]]
- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction]]
