---
aliases: [Outbox + Debezium hybrid, hybrid CDC outbox, OutboxEventRouter]
tags: [architecture, microservices, cdc, debezium, kafka, outbox]
---

### Outbox over Debezium eliminates polling overhead while preserving business event contracts

Pure Outbox gives you event shape control but requires a polling publisher that burns DB resources.
Pure CDC gives you log-based delivery but leaks raw DB columns to consumers.

The hybrid fixes both: write a shaped business event to the outbox table, let [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots|Debezium]] tail the WAL instead of polling.

---

#### How the Hybrid Works

```
App writes:
  BEGIN;
    INSERT INTO orders (id, status) VALUES (123, 'placed');
    INSERT INTO outbox (aggregate_type, aggregate_id, type, payload)
      VALUES ('Order', 123, 'OrderPlaced', '{"orderId":123,"userId":1}');
  COMMIT;

Debezium:
  tails WAL → sees outbox INSERT → publishes to Kafka
  no polling, no extra DB queries, sub-second latency
```

The outbox table is never read by application code after insert — Debezium owns it entirely.

---

#### Debezium OutboxEventRouter

Debezium ships a built-in SMT (Single Message Transform) called `OutboxEventRouter`.

It intercepts raw WAL events from the outbox table and rewrites them into clean domain events before publishing to Kafka:

- routes to topic per `aggregate_type` (e.g. `outbox.event.Order`)
- sets Kafka message key to `aggregate_id`
- strips internal outbox columns (`id`, `created_at`, `processed`) from the event payload

Result: consumers receive clean `OrderPlaced` events, not raw `INSERT INTO outbox` noise.

---

#### Why Hybrid Dominates Industry

| | Polling Outbox | Pure CDC | **Outbox + Debezium** |
|---|---|---|---|
| Event shape control | ✅ | ❌ leaks DB schema | ✅ |
| No polling overhead | ❌ | ✅ | ✅ |
| Transactional atomicity | ✅ | ❌ (reads any write) | ✅ |
| App code changes needed | Yes | No | Yes (outbox insert) |
| Schema evolution safety | ✅ | ❌ | ✅ |

The hybrid is the dominant production pattern. Netflix, Uber, and Shopify all use variants of it.

---

#### Industry Adoption

**Netflix** — CDC-based outbox for billions of events/day, requires ordering and zero loss even on DB failover.

**Uber** — Outbox in trip management to guarantee ride status events propagate reliably across services.

**Shopify** — polling outbox for low-criticality events (simplicity), CDC for core DB propagation to data platform.

The trend in 2025: teams start with polling outbox (simple), migrate the publisher to Debezium once polling latency or DB load becomes a problem. The outbox table stays unchanged.

---

#### When to Use Which

```
New system, clean contracts, already have Kafka  → Outbox + Debezium (hybrid)
Legacy system, can't touch app code              → Pure CDC
Simple app, low throughput, no Kafka             → Polling Outbox
Batch sync to data warehouse                     → Airbyte or Flink CDC
```

---

#### Migration Path

Polling outbox → Debezium outbox is a non-breaking migration:
1. Deploy Debezium connector pointing at `outbox` table
2. Disable the polling publisher
3. Outbox table schema unchanged, consumers unchanged

---

### Read more

- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction]]
- [[Debezium streams PostgreSQL WAL changes to Kafka using LSN offsets and replication slots]]
- [[Open-source CDC tools differ in database support, Kafka coupling, and operational overhead]]
