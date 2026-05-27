---
aliases: [cursor pagination, opaque cursor]
created: 2026-05-23
tags: [api-design, pagination, scalability]
---

### What it is

Cursor pagination is keyset pagination where the position is wrapped in an <mark style="background: yellow">opaque token</mark> the server hands to the client.

The client doesn't see or build the key — it just echoes the cursor back:

```
GET /products?limit=20
→ products[1..20] + next_cursor=abc123

GET /products?limit=20&cursor=abc123
→ products[21..40] + next_cursor=xyz789
```

The token typically encodes the last sort key(s) — often base64-encoded JSON like `{"id": 40, "created_at": "..."}`.

---
### Why wrap the key

The cursor is the same seek mechanism underneath, but the opacity buys flexibility:

- The client treats it as a <mark style="background: #4dd0e1">black box</mark> — it can't construct invalid positions.
- The server can change the **internal sort strategy** (add a tiebreaker column, switch keys) without breaking clients.
- It can pack extra state — direction, filters, a version flag — into one string.

This is why public APIs (Stripe, GitHub, Twitter) expose cursors rather than raw `since_id`.

---
### Keyset vs cursor

Same performance profile — both seek into an index, both scale to any depth.

The difference is the **contract**:
- [[Keyset pagination filters by the last seen key for stable performance at any depth|Keyset]] exposes the raw key (`since_id=40`) — simpler, but couples the client to your schema.
- Cursor hides it behind a token — more flexible and stable, slightly more server work to encode/decode.

---
Read more:
- [[Keyset pagination filters by the last seen key for stable performance at any depth]]
- [[Offset pagination slows at deep pages because the database scans and discards skipped rows]]
- [[API Design - MOC]]
