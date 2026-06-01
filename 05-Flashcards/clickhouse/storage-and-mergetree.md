TARGET DECK: Tech-KB::ClickHouse::Storage and MergeTree
Tags: clickhouse database
**Chapter:** Fundamentals + MergeTree Engine
**Related:** [[ClickHouse - MOC]]

---

START
Coding Questions
How does ClickHouse store table data on disk, and how does it differ from PostgreSQL?
Back:
- ClickHouse **stores each column in a separate binary file** (`region.bin`, `price.bin`, etc.)
- A query on 2 columns reads only those 2 files — all others skipped
- PostgreSQL stores each row as a full tuple — a query on 2 of 20 columns still reads all 20
- **Column count has almost no effect** on CH query I/O when only a few columns are selected
Tags: clickhouse storage columnar
<!--ID: 1780311508603-->
END

START
Coding Questions
How does ClickHouse preserve row identity when each column is stored in a separate file?
Back:
**Ordinal position** — every column file stores values in the same row order.

```
region.bin: [EU, US, EU, AS]
price.bin:  [100, 200, 300, 400]
```

Row 2 is always `region=EU, price=300` across all files.
No join, no pointer, no row ID — **position is the key**.
Tags: clickhouse storage columnar
<!--ID: 1780311508624-->
END

START
Coding Questions
Walk through what ClickHouse does at the file layer to execute: `SELECT price WHERE region = 'EU'`
Back:
1. Reads `region.bin` → finds positions `[0, 2]` where value = `EU`
2. Reads **only those positions** from `price.bin`
3. Never opens any other `.bin` file

All column encodings are decompressed in memory first; the positional contract holds at query time.
Tags: clickhouse storage columnar
<!--ID: 1780311508645-->
END

START
Coding Questions
What is the default compression codec in ClickHouse, and how do you enable dictionary encoding?
Back:
- **Default**: `LZ4` (self-hosted) or `ZSTD(1)` (ClickHouse Cloud) — automatic, no schema changes
- **Dictionary encoding**: opt-in via `LowCardinality` type:
```sql
region LowCardinality(String)
```
Stores unique values once; rows store small integer indices.
Effective below ~10,000 distinct values; can hurt above ~100,000.
Tags: clickhouse compression storage
<!--ID: 1780311508666-->
END

START
Coding Questions
What does the ClickHouse RLE codec do, and what column type is it best for?
Back:
**RLE (Run-Length Encoding)** compresses consecutive runs of identical values:

`[EU, EU, EU, US, US, EU]` → stored as `[EU×3, US×2, EU×1]`

- Declare: `status String CODEC(RLE)`
- Order is fully preserved — decoding replays runs in sequence
- Best for **sorted low-cardinality columns** (status, region, category)
Tags: clickhouse compression storage
<!--ID: 1780311508687-->
END

START
Coding Questions
What does the ClickHouse Delta codec do, and how can codecs be chained?
Back:
**Delta codec** stores differences between consecutive values instead of the values themselves.

```sql
event_time DateTime CODEC(Delta, LZ4)
```

- Best for **monotonically increasing columns** like timestamps
- Codecs chain **left-to-right on write, right-to-left on read**
- Example: `CODEC(Delta, LZ4)` → delta-encode first, then LZ4-compress
Tags: clickhouse compression storage
<!--ID: 1780311508708-->
END

START
Coding Questions
What is a MergeTree data part, and what is created on every INSERT?
Back:
A **data part** is a self-contained directory of `.bin` files created for each INSERT batch.

```
table/
  part_1/  ← first INSERT
    id.bin, email.bin, version.bin
  part_2/  ← second INSERT
    id.bin, email.bin, version.bin
```

- Row positions are **local to a part**, not global across the table
- Parts are **immutable** — never modified after being written
Tags: clickhouse mergetree storage
<!--ID: 1780311508728-->
END

START
Coding Questions
Why are MergeTree data parts immutable? What three properties does immutability enable?
Back:
Parts are **never modified after being written**. This enables:

- **High insert throughput** — multiple writers create independent parts with no locking
- **Consistent read snapshots** — a SELECT sees the exact parts that existed when it started
- **Simple replication** — immutable files can be copied without synchronization
Tags: clickhouse mergetree storage
<!--ID: 1780311508750-->
END

START
Coding Questions
Why does MergeTree run background merges, and what is the trade-off of having many small parts?
Back:
Each INSERT creates a new part → many parts → more `.bin` files to open per query → **slower reads**.

Background merge **continuously consolidates small parts into larger ones**:
- Fewer parts → fewer files opened → faster queries
- This is where the "**Merge**" in MergeTree comes from

Trade-off: merge is async — parts accumulate between merges.
Tags: clickhouse mergetree storage
<!--ID: 1780311508773-->
END

START
Coding Questions
Why is UPDATE expensive in ClickHouse, and what is a mutation?
Back:
Parts are **immutable** — `UPDATE email WHERE id = 5` cannot edit `email.bin` in place.

CH must:
1. Read the entire affected part
2. Apply the change
3. Write a **brand new part** with all rows rewritten

This is a **mutation** — even a single-row change rewrites millions of rows.
Mutations are expensive and should be avoided.
Tags: clickhouse mergetree mutations
<!--ID: 1780311508796-->
END

START
Coding Questions
What problem does ReplacingMergeTree solve, and how does it define a duplicate row?
Back:
**Problem**: CH can't update rows in place. Instead, insert a new row with updated values and discard the old one later.

**ReplacingMergeTree** handles "keep latest version" automatically.

**Duplicate** = rows with identical `ORDER BY` column values:
```sql
ENGINE = ReplacingMergeTree(version)
ORDER BY id;
```
`ORDER BY id` → same `id` = duplicate, regardless of other columns.
Tags: clickhouse mergetree deduplication
<!--ID: 1780311508818-->
END

START
Coding Questions
How does ReplacingMergeTree pick the winner row during merge — with and without a version column?
Back:
During merge, CH sorts by `ORDER BY` key → duplicates become adjacent → keeps one per key.

- **With version** `ReplacingMergeTree(version)`: keeps the row with the **highest version value**
- **Without version** `ReplacingMergeTree()`: keeps the row from the **most recently created data part** (internal timestamp metadata — unreliable under concurrent inserts)

Always prefer an explicit version column.
Tags: clickhouse mergetree deduplication
<!--ID: 1780311508841-->
END

START
Coding Questions
Why does a plain SELECT on a ReplacingMergeTree table return duplicates, and when are they removed?
Back:
Deduplication only happens **during background merge** — which runs at unpredictable times.

Between inserts and the next merge, both old and new versions exist on disk.
A plain `SELECT` returns all rows including **duplicates during this window**.

Solutions at query time:
- `SELECT ... FINAL` — deduplicates synchronously (expensive)
- `argMax(col, version)` + `GROUP BY` — picks latest version (preferred)
Tags: clickhouse mergetree deduplication
<!--ID: 1780311508862-->
END

START
Coding Questions
What does FINAL do in ClickHouse, and what is its performance cost?
Back:
`FINAL` **forces deduplication at query time** instead of waiting for background merge.

```sql
SELECT * FROM users FINAL WHERE id = 5;
```

CH reads all parts, holds all versions in memory, picks the winner per `ORDER BY` key.

**Cost**: 21–550% query slowdown (avg ~280%), 20–200× higher memory usage.
Cost scales with **number of unmerged parts** — worst on tables with active inserts.
Tags: clickhouse mergetree deduplication performance
<!--ID: 1780311508885-->
END

START
Coding Questions
When should you use FINAL vs argMax for deduplication in ClickHouse?
Back:
**Use `argMax`** (preferred for active tables):
```sql
SELECT id, argMax(email, version) FROM users GROUP BY id;
```
- Consistent latency regardless of unmerged part count

**Use `FINAL`** only when:
- Table is historical and **fully merged** (one part per partition)
- At that point FINAL performance approaches argMax

Never use FINAL on tables receiving continuous inserts.
Tags: clickhouse mergetree deduplication performance
<!--ID: 1780311508908-->
END

START
Coding Questions
What does `argMax(arg, val)` return, and how do you use it to get the latest row per user?
Back:
`argMax(arg, val)` returns the value of `arg` from the row where `val` is **maximum**.

```sql
SELECT
    id,
    argMax(email, version) AS latest_email
FROM users
GROUP BY id;
```

- Always exactly **two arguments**: *what you want* and *what to maximize by*
- Must pair with `GROUP BY` on the unique key
- If multiple rows tie on `val`, result is **non-deterministic** — use a strictly increasing version
Tags: clickhouse sql aggregate-functions
<!--ID: 1780311508930-->
END

START
Coding Questions
How does lightweight DELETE work in ClickHouse, and how does it differ from ALTER TABLE DELETE?
Back:
**Lightweight DELETE** (`DELETE FROM`):
1. Creates a patch part setting hidden `_row_exists = 0` on matching rows
2. Queries immediately skip flagged rows
3. Physical removal happens during next background merge
→ **Low cost** — recommended for row-level deletes

**ALTER TABLE ... DELETE**:
- Rewrites entire affected parts (same cost as a mutation)
→ **Very high cost** — avoid

**DROP PARTITION**:
- Drops partition directory instantly
→ **Near-zero cost** — best for bulk time-based deletes
Tags: clickhouse mergetree delete mutations
<!--ID: 1780311508953-->
END
