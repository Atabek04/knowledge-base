---
aliases: [CORS preflight, OPTIONS preflight, simple vs non-simple request]
created: 2026-05-14
tags: [web, security, http, cors]
---

For "non-simple" cross-origin requests the browser sends an extra **OPTIONS** request *before* the real one. The real request only fires if the preflight response approves it.

**Simple request** (no preflight needed — must match ALL):
- Method: `GET`, `HEAD`, or `POST`
- Headers: only CORS-safelisted (`Accept`, `Accept-Language`, `Content-Language`, `Content-Type`)
- `Content-Type` is one of: `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`

**Non-simple** (preflight required) — anything else: `PUT`, `DELETE`, `PATCH`, custom headers like `Authorization`, or `Content-Type: application/json`.

**Preflight exchange:**
```
OPTIONS /api/reports HTTP/1.1
Origin: https://app.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: authorization, content-type

HTTP/1.1 204
Access-Control-Allow-Origin: https://app.com
Access-Control-Allow-Methods: POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 3600
```

`Access-Control-Max-Age` caches the preflight result so the browser doesn't OPTIONS every call.

**Why this matters in practice:** `application/json` POST is the *most common* trigger. A backend that allows GET cross-origin but rejects the OPTIONS preflight (or returns wrong allowed origin) will silently break every JSON POST while GETs keep working — exactly the symptom in the report-service Swagger 403 incident, where the prod hostname was missing from `allowedOrigins` and only the JSON POST tripped CORS because GET sent no `Origin` header.

**Spring gotcha:** `DefaultCorsProcessor` rejects with `403 "Invalid CORS request"` *before* security filters run. JWT errors won't show up — fix CORS first, then debug auth.

---

**Read more:**
- [[CORS relaxes Same-Origin Policy to allow controlled cross-origin browser requests]]
- [[Browser sends Origin header on cross-origin requests and on non-simple same-origin requests]]
- [[API Design - MOC]]
