---
aliases: [MergeTree data parts, data parts, MergeTree]
created: 2026-05-21
tags: [clickhouse, database, mergetree, storage]
---

### What Happens on INSERT

Every INSERT batch in ClickHouse creates a new self-contained directory called a **data part**.

```
table/
  part_1/   ← first INSERT batch
    id.bin
    email.bin
    version.bin
  part_2/   ← second INSERT batch
    id.bin
    email.bin
    version.bin
```

Each part has its own `.bin` files. Row positions are local to a part — not global across the table.

---

### Why Parts Are Immutable

Parts are never modified after being written. This enables:

- **High insert throughput** — multiple writers create independent parts with no locking or coordination
- **Consistent read snapshots** — a SELECT sees the exact set of parts that existed when it started; no mid-query surprises
- **Simple replication** — immutable files can be copied without synchronization

---

### Background Merge

Many small parts → more files to scan per query → slower reads.

CH runs a background process that continuously merges small parts into larger ones.
This is where the "Merge" in MergeTree comes from.

Fewer parts after merge → fewer `.bin` files opened per query → faster reads.

---

### The UPDATE Problem

Because parts are immutable, `UPDATE email WHERE id = 5` cannot edit `email.bin` in place.

CH must read the entire affected part, apply the change, and write a brand new part — a **mutation**.
Even a single-row change rewrites millions of rows. This is why mutations are expensive and should be avoided.

---

Read more:
- [[ClickHouse - MOC]]
- [[ClickHouse columnar storage reads only queried columns by preserving row position across files]]
- [[ReplacingMergeTree deduplicates rows on merge using ORDER BY key and optional version column]]
