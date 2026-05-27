---
aliases: [ClickHouse DELETE, lightweight delete]
created: 2026-05-21
tags: [clickhouse, database, mergetree, delete]
---

### Why DELETE Is Not Instant in ClickHouse

Parts are immutable — rows cannot be removed in place. Instead, ClickHouse uses a hidden system column `_row_exists` to mark rows as deleted without touching the part files.

---

### How Lightweight DELETE Works

```sql
DELETE FROM orders WHERE id = 123;
```

1. CH creates a small **patch part** setting `_row_exists = 0` for matching rows
2. All subsequent queries skip rows where `_row_exists = 0` — deletion is immediately visible
3. Rows are physically removed from disk during the next background merge

The original part files are never modified.

---

### Three Deletion Mechanisms Compared

| Mechanism | How | Cost |
|---|---|---|
| `DELETE FROM` (lightweight) | Patch part with hidden flag | Low — recommended |
| `ALTER TABLE ... DELETE` | Rewrites entire affected parts | Very high — avoid |
| `DROP PARTITION` | Drops partition directory instantly | Near-zero — best for bulk time-based deletes |

---

### When to Use Each

- **Lightweight DELETE** — row-level deletes where physical removal can wait until next merge
- **DROP PARTITION** — bulk deletion of old data by time range (e.g. TTL cleanup)
- **ALTER TABLE DELETE** — avoid; same cost as a mutation, rewrites all matching parts

---

Read more:
- [[ClickHouse - MOC]]
- [[MergeTree stores each INSERT as an immutable data part merged in background]]
