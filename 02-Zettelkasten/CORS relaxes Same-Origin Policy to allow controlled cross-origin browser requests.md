---
aliases: [CORS, Cross-Origin Resource Sharing]
created: 2026-05-14
tags: [web, security, http, api]
---

**Same-Origin Policy (SOP)** is a browser rule: JavaScript on `https://a.com` cannot read responses from `https://b.com`. It blocks a malicious page from silently calling your bank's API using the user's cookies.

**CORS (Cross-Origin Resource Sharing)** is the *server-controlled escape hatch*. The server explicitly tells the browser "I trust origin X to read my responses" via response headers. Browser enforces; server authorizes.

**Origin** = scheme + host + port. `https://app.com` ≠ `http://app.com` ≠ `https://app.com:8443`.

**Key point: CORS protects the user's browser, not the server.** A `curl` or backend-to-backend call ignores CORS entirely — only browsers enforce it. SOP/CORS exists because browsers automatically attach cookies/auth headers to requests; without SOP any site could ride those credentials.

**Minimal handshake (simple GET):**
```
Request:   Origin: https://app.com
Response:  Access-Control-Allow-Origin: https://app.com
```
If the response header is missing or doesn't match, browser drops the response and surfaces a CORS error to JS — the request still hit the server.

**With credentials** (cookies, `Authorization` header sent by browser):
```
Access-Control-Allow-Origin: https://app.com   (must be exact origin, not *)
Access-Control-Allow-Credentials: true
```

**Common confusion:** a CORS failure looks like a network error in the browser console but the server already executed the request. CORS is a *read* gate, not a *send* gate. For mutating requests, the [[CORS preflight uses OPTIONS request to authorize non-simple cross-origin calls]] mechanism does block the actual call until the server greenlights it.

---

**Read more:**
- [[CORS preflight uses OPTIONS request to authorize non-simple cross-origin calls]]
- [[Browser sends Origin header on cross-origin requests and on non-simple same-origin requests]]
- [[API Design - MOC]]
