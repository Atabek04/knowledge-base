---
aliases: [keyset pagination, seek method, since_id pagination]
created: 2026-05-23
tags: [api-design, databases, pagination, performance, scalability]
---

### What it is

Keyset pagination (the "seek method") fetches the next page by <mark style="background: yellow">filtering on the last value seen</mark> instead of counting an offset.

Instead of "skip 4980 rows", it says "give me rows *after* this one".

```sql
SELECT * FROM products
WHERE id > 4980
ORDER BY id
LIMIT 20;
```

The client sends `?limit=20&since_id=4980` — the id of the last item it received.

---
### Why it stays fast

`WHERE id > 4980` lets the database <mark style="background: #4dd0e1">seek directly into the index</mark> and read 20 rows.

No skipped rows to scan and discard.

Page 1 and page 5000 cost the same → <mark style="background: yellow">constant, predictable latency</mark> regardless of depth.

This is why high-load systems use it.

---
### Requirements

- Order by a column that is **unique and indexed** (usually the primary key, a timestamp, or a composite).
- For non-unique sort columns, add a tiebreaker: `ORDER BY created_at, id` and compare on the pair, or duplicates/gaps appear at page boundaries.

---
### The tradeoff

You lose random access.

You can only go **next** (and **previous** with reversed comparison) — there is no "jump to page 250" and no cheap total page count.

That's an acceptable price for feeds, infinite scroll, and exports where users move sequentially.

It directly solves the deep-scan problem of [[Offset pagination slows at deep pages because the database scans and discards skipped rows|offset pagination]].

---
Read more:
- [[Offset pagination slows at deep pages because the database scans and discards skipped rows]]
- [[Cursor pagination hides the paging position inside an opaque token]]
- [[API Design - MOC]]
