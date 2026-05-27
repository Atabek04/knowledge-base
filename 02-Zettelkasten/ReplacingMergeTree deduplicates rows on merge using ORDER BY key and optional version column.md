---
aliases: [ReplacingMergeTree]
created: 2026-05-21
tags: [clickhouse, database, mergetree, deduplication]
---

### The Problem It Solves

ClickHouse can't update rows in place — parts are immutable.
The pattern instead: insert a new row with the updated values, let CH discard the old version later.

ReplacingMergeTree is the engine that handles this "keep latest version" logic.

---

### What Defines a Duplicate

Rows with identical `ORDER BY` column values are considered the same logical row.

```sql
CREATE TABLE users (
    id      UInt64,
    email   String,
    version UInt64
) ENGINE = ReplacingMergeTree(version)
ORDER BY id;
```

`ORDER BY id` → two rows with the same `id` are duplicates, regardless of other column values.

---

### How Merge Picks the Winner

During background merge, CH sorts the part by the `ORDER BY` key — duplicates become adjacent.
It then scans through and keeps one row per unique key, discarding the rest.

**With version column** (e.g. `ReplacingMergeTree(version)`): keeps the row with the highest version value.

**Without version column** (`ReplacingMergeTree()`): keeps the row from the most recently created data part. CH tracks each part's creation timestamp as internal metadata — no user-visible column or log. This is unreliable under concurrent inserts since part ordering isn't guaranteed when batches arrive simultaneously. Always prefer an explicit version column.

---

### Eventual Consistency Warning

Deduplication only happens during merge. Merges run in the background at unpredictable times.

Between inserts and the next merge, both old and new rows exist simultaneously on disk.
A plain `SELECT` will return duplicates during this window.

---

Read more:
- [[ClickHouse - MOC]]
- [[MergeTree stores each INSERT as an immutable data part merged in background]]
- [[FINAL forces deduplication at query time but degrades performance with many unmerged parts]]
- [[argMax retrieves the value corresponding to the maximum of another column]]
