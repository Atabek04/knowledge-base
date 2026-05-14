TARGET DECK: Tech-KB::Software Engineering::CORS
Tags: web security cors http
**Chapter:** CORS & Same-Origin Policy
**Related:** [[API Design - MOC]]

---

START
Coding Questions
What problem does CORS solve?
Back: The **Same-Origin Policy** blocks JavaScript on `a.com` from reading responses from `b.com` — protects users from malicious sites riding their cookies.
**CORS** is the server-controlled escape hatch: server sends `Access-Control-Allow-Origin` to authorize specific origins.
- Browser enforces, server authorizes
- Protects the **user's browser**, not the server
- `curl` / backend-to-backend ignore CORS
Tags: web security cors
END

START
Coding Questions
What defines an "origin" in CORS?
Back: **scheme + host + port** — all three must match.
- `https://app.com` ≠ `http://app.com` (different scheme)
- `https://app.com` ≠ `https://api.app.com` (different host)
- `https://app.com` ≠ `https://app.com:8443` (different port)
Tags: web security cors
END

START
Coding Questions
When does the browser send a CORS preflight (OPTIONS)?
Back: For **non-simple** cross-origin requests. A request is **simple** only if ALL hold:
- Method is `GET`, `HEAD`, or `POST`
- Headers are CORS-safelisted only
- `Content-Type` ∈ {`application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`}
Anything else (PUT/DELETE/PATCH, custom headers, `Authorization`, `Content-Type: application/json`) → preflight required.
Tags: web cors http
END

START
Coding Questions
Why does a same-origin GET often work while same-origin POST fails CORS?
Back: Browsers **omit** the `Origin` header on simple same-origin GETs but **always send** it on non-simple requests (e.g., POST with `application/json`).
- No `Origin` → server's CORS filter skips check → 200
- `Origin` present but not in allow-list → 403 "Invalid CORS request"
Common Swagger-UI symptom when the API's own host isn't in `allowedOrigins`.
Tags: web cors debugging
END

START
Coding Questions
Why use `Access-Control-Allow-Credentials: true` and what is its constraint?
Back: Tells the browser it's safe to expose responses to JS when the request carried cookies or `Authorization`.
**Constraint:** `Access-Control-Allow-Origin` cannot be `*` — must be the exact origin string. Same for `Allow-Methods` / `Allow-Headers`.
Tags: web cors security
END

START
Coding Questions
Spring returns `403 "Invalid CORS request"` for a JWT-protected endpoint. Where to look first?
Back: CORS, **not** auth. Spring's `DefaultCorsProcessor` rejects before security filters run, so JWT errors won't appear.
1. Verify request `Origin` matches `allowedOrigins`
2. Behind ingress, set `server.forward-headers-strategy=framework` so `isSameOrigin` works on the public URL
3. For credentialed requests, ensure `allowCredentials=true` + exact origin (no `*`)
Tags: spring cors debugging
END

START
Coding Questions
Difference between `Origin` and `Referer` headers?
Back:
- **Origin**: scheme + host + port only (no path). Sent on cross-origin requests and non-simple writes. Privacy-preserving.
- **Referer**: full URL including path/query. Subject to referrer policy stripping.
CORS decisions key on `Origin`, never `Referer`.
Tags: web http headers
END
