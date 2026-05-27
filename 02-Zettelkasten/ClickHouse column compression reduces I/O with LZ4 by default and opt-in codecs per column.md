---
aliases: [ClickHouse compression, ClickHouse codecs]
created: 2026-05-21
tags: [clickhouse, database, compression, storage]
---

### Default Compression

ClickHouse applies **LZ4** compression to every column automatically on self-hosted deployments; ClickHouse Cloud defaults to **ZSTD(1)**.
No schema changes needed — this compression is transparent and applied on write, reversed on read.

---

### Opt-In Column Encodings

Beyond the default codec, ClickHouse offers column-level encodings that must be explicitly declared in the schema.

**Dictionary encoding via `LowCardinality`**

Wrap a column type to enable dictionary encoding:

```sql
region LowCardinality(String)
```

ClickHouse stores unique values once in a dictionary; each row stores a small integer index instead of the full string.
Effective when cardinality is below ~10,000 distinct values. Above ~100,000 it can hurt performance.

**RLE codec**

Compresses consecutive runs of identical values:

```sql
status String CODEC(RLE)
```

`[EU, EU, EU, US, US, EU]` is stored as `[EU×3, US×2, EU×1]`.
Order is fully preserved — decoding replays each run in sequence.
Best for sorted low-cardinality columns.

**Delta codec**

Stores differences between consecutive values instead of the values themselves:

```sql
event_time DateTime CODEC(Delta, LZ4)
```

Effective for monotonically increasing columns like timestamps.
Codecs can be chained — applied left-to-right on write, right-to-left on read.

---

### Compression Is Transparent at Query Time

All encodings are reversed in memory before positional row mapping across columns.
The row-position contract is never broken at query time.

---

### Combined Effect

Columnar layout + per-column compression gives ClickHouse two compounding advantages:

1. **Less data read** — skip irrelevant columns entirely
2. **Smaller data per column** — homogeneous values compress far better than mixed rows

Typical analytical data hits 5–10× compression; low-cardinality columns can reach 30×+.

---

Read more:
- [[ClickHouse - MOC]]
- [[ClickHouse columnar storage reads only queried columns by preserving row position across files]]
