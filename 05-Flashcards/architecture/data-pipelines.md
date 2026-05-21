TARGET DECK: Tech-KB::Architecture::Data Pipelines
Tags: architecture data-engineering
**Chapter:** Data Patterns
**Related:** [[Microservices Patterns - MOC]]

---

START
Coding Questions
Why does the dual-write pattern use both PostgreSQL and ClickHouse instead of one database?
Back:
Neither database covers both workloads:

| | PostgreSQL | ClickHouse |
|---|---|---|
| Transactions | ✅ ACID, BEGIN/COMMIT | ❌ single-INSERT only |
| Row updates | ✅ instant | ❌ expensive mutation |
| Analytical queries | ❌ slow on billions of rows | ✅ sub-second aggregations |

Systems needing operational consistency **and** real-time analytics require both.
Tags: dual-write architecture clickhouse postgresql
END

START
Coding Questions
What is data drift in dual-write, and what causes it?
Back:
**Data drift** = PG and CH hold different versions of the same data — analytics are silently wrong.

**Cause**: naive dual-write writes to both directly:
```
app → INSERT into PG  ✓
app → INSERT into CH  ✗  (crash/network drop)
```

PG has the record. CH doesn't. No error is raised — the inconsistency is invisible.
Tags: dual-write architecture data-engineering
END

START
Coding Questions
What is the reliable architecture for dual-write from PostgreSQL to ClickHouse?
Back:
Never write to CH directly. Use a pipeline:

```
app → PG (transactional write)
        ↓
   Outbox or Debezium (CDC)
        ↓
      Kafka
        ↓
  CH consumer → INSERT
```

- **Outbox**: app writes event to `outbox` table in same PG transaction → publisher reads and forwards
- **Debezium**: tails PG WAL directly → streams every committed change

Both guarantee at-least-once delivery. CH's `ReplacingMergeTree` handles duplicates.
Tags: dual-write architecture data-engineering
END

START
Coding Questions
How does the Outbox pattern guarantee that a database write and a Kafka event are never split?
Back:
The event is written to an `outbox` table **inside the same business transaction**:

```sql
BEGIN;
  INSERT INTO orders (id, ...) VALUES (123, ...);
  INSERT INTO outbox (payload) VALUES ('{"event":"OrderPlaced","orderId":123}');
COMMIT; -- both committed atomically, or neither
```

A **publisher process** reads the outbox and forwards to Kafka. On failure it retries.
Result: **at-least-once** — no lost events, occasional duplicates on retry.
Tags: outbox-pattern messaging architecture
END

START
Coding Questions
What are the two publisher implementations for the Outbox pattern, and what is the trade-off?
Back:
**Polling publisher**
- Queries `WHERE processed = false` on a schedule
- Simple, but adds DB load and introduces latency proportional to poll interval

**Transaction log tailing (Debezium)**
- Reads outbox table changes directly from the WAL
- Instant notification, zero polling overhead
- More infrastructure (Kafka Connect, replication slot)

Choose polling for simplicity at low scale; choose log tailing for low latency and high throughput.
Tags: outbox-pattern messaging architecture
END

START
Coding Questions
When should you choose Outbox pattern over pure Debezium CDC?
Back:
| | Outbox | Debezium (pure CDC) |
|---|---|---|
| Event shape | Full control — business events | Raw DB column changes |
| App changes | Yes — write to outbox table | No |
| Schema leakage | None | Exposes DB internals |
| Multi-app DBs | Only your app's events | Captures all writers |

**Choose Outbox** when:
- Clean event contracts matter (microservices, external consumers)
- You don't want DB schema leaking to consumers

**Choose pure CDC** when:
- Legacy system — can't change app code
- Need to capture changes from multiple apps on the same DB
Tags: outbox-pattern cdc architecture
END

START
Coding Questions
How does Debezium track its position in the PostgreSQL WAL, and what happens on restart?
Back:
Every WAL entry has an **LSN (Log Sequence Number)** — a monotonically increasing position.

After each batch, Debezium saves the **last processed LSN** to a Kafka topic (offset store).

On restart:
1. Reads last saved LSN from Kafka
2. Tells PG: "give me everything after LSN X"
3. Resumes without gaps

PG's **replication slot** guarantees WAL entries are retained until Debezium confirms it has read them — even during long outages.
Tags: debezium cdc postgresql wal
END

START
Coding Questions
What delivery guarantee does Debezium provide by default, and why can the same event appear twice?
Back:
Default: **at-least-once** delivery.

**Duplicate scenario**:
1. Debezium reads WAL event, publishes to Kafka ✓
2. Debezium crashes **before saving offset**
3. Restarts → sees last saved LSN = before that event
4. Publishes the **same event again**

**Solution**: consumers must be idempotent.
In ClickHouse, `ReplacingMergeTree` handles duplicate inserts naturally via version column.

Exactly-once available with Kafka Connect 3.3+ but rarely needed if consumer is idempotent.
Tags: debezium kafka delivery-guarantees
END

START
Coding Questions
What is a Kafka offset, and how does it cause duplicate processing in at-least-once delivery?
Back:
**Offset** = sequential position number of each message within a Kafka partition. Consumers save their last processed offset to know where to resume.

**At-least-once duplicate scenario**:
1. Consumer processes message at offset 50 ✓
2. Consumer crashes **before saving offset 50**
3. Restarts — last saved offset = 49
4. Processes offset 50 again → **duplicate**

**Fix**: idempotent consumers (e.g. `ReplacingMergeTree` in ClickHouse discards duplicates on merge).
Tags: kafka messaging distributed-systems
END

START
Coding Questions
What is the difference between at-least-once and exactly-once delivery in Kafka?
Back:
**At-least-once** (default):
- No messages lost
- Same message may be processed more than once on failure
- Requires **idempotent consumers** to handle duplicates

**Exactly-once**:
- Kafka atomically commits "message processed + offset saved" — no duplicate window
- Requires Kafka Connect distributed mode + version 3.3+

**Practical rule**: use at-least-once + idempotent consumers. Exactly-once adds complexity and is rarely necessary.

> At-least-once prioritises **no data loss** over **no duplicates** — a lost message is usually worse than a discarded duplicate.
Tags: kafka messaging distributed-systems delivery-guarantees
END
