---
aliases: [argMax]
created: 2026-05-21
tags: [clickhouse, database, aggregate-functions, sql]
---

### Syntax

```sql
argMax(arg, val)
```

Returns the value of `arg` from the row where `val` is maximum.
Always exactly two arguments: *what you want* and *what to maximize by*.

---

### Practical Example: Latest Row per User

```sql
SELECT
    id,
    argMax(email, version) AS latest_email
FROM users
GROUP BY id;
```

For each `id`, CH finds the row with the highest `version` and returns its `email`.
This gives the latest version of every row without `FINAL`.

---

### How It Works at the File Layer

CH reads `id.bin` and `version.bin` together (position-aligned).
For each unique `id`, it tracks which position holds the highest `version` value.
It then reads only those winning positions from `email.bin`.

No full-part reconciliation — CH never materializes all duplicate rows at once.

---

### Why Prefer It Over FINAL

`argMax` performance is consistent regardless of how many unmerged parts exist.
`FINAL` degrades as unmerged part count grows (21–550% slowdown under active inserts).

Use `argMax` + `GROUP BY` on tables receiving continuous inserts.
Use `FINAL` only on fully merged historical partitions.

---

### Non-Determinism Warning

If multiple rows share the same maximum `val`, the returned `arg` is non-deterministic.
Always use a strictly increasing column (timestamp, auto-increment version) to avoid ties.

---

Read more:
- [[ClickHouse - MOC]]
- [[ReplacingMergeTree deduplicates rows on merge using ORDER BY key and optional version column]]
- [[FINAL forces deduplication at query time but degrades performance with many unmerged parts]]
