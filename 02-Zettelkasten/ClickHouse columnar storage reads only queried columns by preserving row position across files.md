---
aliases: [ClickHouse columnar storage, columnar storage]
created: 2026-05-21
tags: [clickhouse, database, olap, storage]
---

### ClickHouse Columnar Storage

ClickHouse stores each column in a separate binary file on disk.
A query touching only `price` and `region` reads just those two files — all other columns are skipped entirely.

---

### How Row Identity Is Preserved

Row identity is maintained by **ordinal position** — every column file stores values in the same row order.

```
region.bin:  [EU,  US,  EU,  AS]
price.bin:   [100, 200, 300, 400]
```

Row 2 is always `region=EU, price=300` across every column file.
No join, no pointer, no row ID needed — position is the key.

---

### Filtering Across Columns

To execute `WHERE region = 'EU'`, ClickHouse:

1. Reads `region.bin` → finds positions `[0, 2]` where value = `EU`
2. Reads only those positions from `price.bin`
3. Never opens any other `.bin` file

---

### Why This Beats Row-Oriented Storage

In PostgreSQL each row is stored as a single tuple containing all columns.
A query on 2 of 20 columns still reads all 20 — every unused column wastes I/O.

ClickHouse inverts this: column count has almost no effect on query cost when only a few columns are selected.

---

Read more:
- [[ClickHouse - MOC]]
- [[ClickHouse column compression reduces I/O with LZ4 by default and opt-in codecs per column]]
