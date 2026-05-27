---
aliases: [offset pagination, LIMIT OFFSET pagination]
created: 2026-05-23
tags: [api-design, databases, pagination, performance]
---

### What it is

Offset pagination fetches a page by skipping `N` rows and returning the next `LIMIT` rows.

```sql
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 4980;
```

The client asks for page 250 by sending `?limit=20&offset=4980`.

---
### Why it degrades

The database can't jump straight to row 4981.

It must <mark style="background: #ff6b8b">read and discard all 4980 skipped rows first</mark>, then return the 20 you want.

Page 1 (`OFFSET 0`) is instant.
Page 5000 (`OFFSET 99980`) crawls — the engine walks through 99,980 rows just to throw them away.

Cost grows linearly with offset → latency that gets worse the deeper you page.

---
### The consistency trap

Offset assumes the underlying data is frozen between requests.

If a row is inserted or deleted while a user pages, the window shifts:
- A new row at the top → the last item of page 1 reappears as the first item of page 2 (**duplicate**)
- A deleted row → an item is **skipped** entirely

---
### When it's fine

- Small datasets where deep pages are rare
- UIs that need "jump to page 250" or a total page count
- Admin tables, reports — correctness over scale

The fix for high-load systems is [[Keyset pagination filters by the last seen key for stable performance at any depth|keyset pagination]].

---
Read more:
- [[Keyset pagination filters by the last seen key for stable performance at any depth]]
- [[Cursor pagination hides the paging position inside an opaque token]]
- [[API Design - MOC]]
