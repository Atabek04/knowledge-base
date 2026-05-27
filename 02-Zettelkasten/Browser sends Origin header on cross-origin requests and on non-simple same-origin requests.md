---
aliases: [Origin header, when browser sends Origin]
created: 2026-05-14
tags: [web, http, cors, security]
---

The `Origin` header tells the server which page initiated the request. The browser's rules for *when* to attach it are subtle and explain a class of "works on GET, fails on POST" bugs.

**Always sent:**
- Any cross-origin request (GET, POST, PUT, DELETE, ...)
- Any same-origin **non-simple** request (POST with `application/json`, `PUT`, `DELETE`, custom headers)
- Any preflight `OPTIONS`

**Often omitted:**
- Same-origin **simple GET / HEAD** — no `Origin` header at all in most browsers (Chrome, Firefox)

**Why this surprises people:** if `Origin` is absent, server-side CORS filters skip the check entirely → request passes. If `Origin` is present but doesn't match the allow-list → request is rejected with `403 "Invalid CORS request"` (Spring) or browser-side block.

**Concrete bug pattern:** Swagger UI hosted at `https://api.example.com/swagger-ui` calling `https://api.example.com/v1/...`:
- `GET /v1/types` → no `Origin` header → server processes → 200
- `POST /v1/generate` (JSON body) → `Origin: https://api.example.com` sent (non-simple) → server compares to allow-list → if its own host isn't listed → 403

**Why behind a reverse proxy / ingress this gets worse:** Spring's `isSameOrigin` compares `Origin` to the *request URL it sees*, which is the internal `http://pod-ip:8080`. So even genuinely same-origin POSTs look cross-origin to the backend. Fix: `server.forward-headers-strategy=framework` so Spring reconstructs the public URL from `X-Forwarded-*`.

**Distinction from `Referer`:** `Origin` is just scheme+host+port (no path), sent on writes for privacy. `Referer` includes the full URL and is suppressed under stricter referrer policies.

---

**Read more:**
- [[CORS relaxes Same-Origin Policy to allow controlled cross-origin browser requests]]
- [[CORS preflight uses OPTIONS request to authorize non-simple cross-origin calls]]
- [[API Design - MOC]]
