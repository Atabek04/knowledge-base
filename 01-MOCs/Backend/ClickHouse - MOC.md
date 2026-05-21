---
created: 2026-05-12
tags: [moc, clickhouse, database, olap]
---

# ClickHouse — MOC

> Fast open-source OLAP DBMS — columnar storage, vectorized execution, MergeTree family.

---

## Fundamentals

- [ ] What ClickHouse is and when to use it
- [[ClickHouse columnar storage reads only queried columns by preserving row position across files]]
- [[ClickHouse column compression reduces I/O with LZ4 by default and opt-in codecs per column]]
- [ ] Installation and deployment (binary, Docker, Kubernetes)
- [ ] Client tools (clickhouse-client, DBeaver, HTTP interface)

## SQL

- [ ] DDL — databases, tables, schema evolution
- [ ] DQL — SELECT, filtering, aggregation
- [[ClickHouse lightweight DELETE marks rows with hidden flag removed during background merge]]
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

- [[MergeTree stores each INSERT as an immutable data part merged in background]]
- [ ] On-disk layout — data directory, bin files, mark files, primary index
- [ ] Primary key vs ORDER BY key
- [ ] Partitioning strategy
- [ ] Data skipping indexes
- [ ] Engine settings and tuning

## MergeTree Family Variants

- [[ReplacingMergeTree deduplicates rows on merge using ORDER BY key and optional version column]]
- [[FINAL forces deduplication at query time but degrades performance with many unmerged parts]]
- [[argMax retrieves the value corresponding to the maximum of another column]]
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
- [[Dual-write pattern uses PostgreSQL for transactional writes and ClickHouse for analytics]]
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
