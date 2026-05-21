---
aliases: [idempotency key, Idempotency-Key header]
created: 2026-05-21
tags: [api, rest, distributed-systems, reliability]
---

A network timeout leaves the client unable to tell if the server processed the request or not.
Without protection, every retry risks executing the operation twice — a double charge, a duplicate order.

**Idempotency key** is a client-generated UUID sent in the `Idempotency-Key` request header.
The server executes the operation on the first call, caches the result keyed by that UUID, and returns the cached result on every subsequent call with the same key — without re-executing.

```
POST /orders
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
```

**Server logic:**
1. Look up the key in the idempotency store
2. If found → return cached response immediately
3. If not found → execute, store result, return response

Cached results typically expire after 24 hours.
The key is client-generated so the server never needs to distinguish a retry from a new request — same key means same response, always.

**Why it matters:**
- Mobile clients and load balancers retry on timeout — without idempotency, retries are dangerous by default
- The pattern makes write operations **safe to retry**, which is a requirement in any distributed system
- Stripe, PayPal, and every major payment API mandate idempotency keys on write endpoints

---

**Read more:**
- [[API Design - MOC]]
