---
created: 2026-05-12
tags: [moc, clickhouse, database, olap]
---

# ClickHouse — MOC

> Fast open-source OLAP DBMS — columnar storage, vectorized execution, MergeTree family.

---

## Fundamentals

- [ ] What ClickHouse is and when to use it
- [ ] Why ClickHouse is fast (columnar storage, vectorized execution, compression)
- [ ] Installation and deployment (binary, Docker, Kubernetes)
- [ ] Client tools (clickhouse-client, DBeaver, HTTP interface)

## SQL

- [ ] DDL — databases, tables, schema evolution
- [ ] DQL — SELECT, filtering, aggregation
- [ ] DML — INSERT, ALTER, mutations vs OLTP UPDATE/DELETE
- [ ] Views — normal, materialized, parameterized
- [ ] Joins and unions — types, performance trade-offs

## Data Types

- [ ] Numeric types
- [ ] String types (String, FixedString)
- [ ] Date and DateTime
- [ ] Arrays and Tuples
- [ ] Nested type
- [ ] LowCardinality for low-cardinality columns
- [ ] Geo types
- [ ] Map type

## MergeTree Engine

- [ ] MergeTree concept — why it's called that, part merges
- [ ] On-disk layout — data directory, bin files, mark files, primary index
- [ ] Primary key vs ORDER BY key
- [ ] Partitioning strategy
- [ ] Data skipping indexes
- [ ] Engine settings and tuning

## MergeTree Family Variants

- [ ] ReplacingMergeTree — dedup by sort key
- [ ] SummingMergeTree — pre-aggregated sums
- [ ] AggregatingMergeTree — arbitrary aggregate states
- [ ] CollapsingMergeTree — sign-based row collapsing
- [ ] VersionedCollapsingMergeTree — versioned variant
- [ ] Choosing the right engine

## Special Table Engines

- [ ] File, URL — external data
- [ ] Memory, Buffer — in-memory and write buffering
- [ ] Merge, Set — query helpers
- [ ] Dictionaries — external lookup data
- [ ] Log family (TinyLog, Log, StripeLog) — small datasets

## Distributed ClickHouse

- [ ] Multi-node setup
- [ ] Replication (ReplicatedMergeTree, ZooKeeper/Keeper)
- [ ] Sharding with Distributed engine
- [ ] Replicated + sharded combined

## Integrations

- [ ] MySQL / PostgreSQL — table engines and federated queries
- [ ] MongoDB
- [ ] Apache Kafka — streaming ingest
- [ ] S3 and object storage

## Administration

- [ ] User management, roles, RBAC
- [ ] Settings profiles and quotas
- [ ] Server configuration
- [ ] System tables for introspection
- [ ] Backups and restore
- [ ] clickhouse-local and clickhouse-benchmark

---

## Related

- [[Databases - MOC]]
