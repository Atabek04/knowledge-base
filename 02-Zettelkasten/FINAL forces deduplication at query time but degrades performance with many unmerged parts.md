---
aliases: [FINAL, FINAL keyword]
created: 2026-05-21
tags: [clickhouse, database, mergetree, deduplication, performance]
---

### What FINAL Does

`FINAL` forces ClickHouse to deduplicate rows at query time instead of waiting for background merge.

```sql
SELECT * FROM users FINAL WHERE id = 5;
```

CH reads all parts, holds all versions of each `ORDER BY` key in memory, picks the winner, discards the rest — then returns results.
This is the same job as background merge, but **synchronous**: your query waits until it's done.

---

### Performance Cost

Because `FINAL` must reconcile all parts before returning results, its cost scales with the number of unmerged parts.

Benchmarks show 21–550% query slowdown (average ~280%) and 20–200× higher memory usage compared to queries without `FINAL`.

Performance improves significantly as parts consolidate — with a single merged part the gap narrows considerably.

---

### When to Avoid It

Avoid `FINAL` on tables receiving active inserts — many small parts → worst-case dedup cost.

Prefer `argMax` for predictable latency regardless of merge state.

---

### When FINAL Is Acceptable

On historical partitions that are fully merged (one part per partition), `FINAL` performance approaches that of `argMax`.

---

Read more:
- [[ClickHouse - MOC]]
- [[ReplacingMergeTree deduplicates rows on merge using ORDER BY key and optional version column]]
- [[argMax retrieves the value corresponding to the maximum of another column]]
