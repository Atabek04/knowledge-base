---
created: 2026-04-28
tags: [backend/http, backend/api]
aliases: [Content-Type]
sr-due:
sr-interval:
sr-ease:
---

# Content-Type header tells receiver how to parse the HTTP body

Without `Content-Type`, the receiver gets raw bytes with no instruction on format. It would have to guess — or reject the request.

`Content-Type` solves this: sender declares the format, receiver parses accordingly.

```
Content-Type: application/json
Content-Type: text/event-stream
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary
```

---

### Structure

```
Content-Type: <type>/<subtype>[; parameter=value]
```

- **type** — broad category (`text`, `application`, `image`, `video`, `multipart`)
- **subtype** — specific format (`json`, `html`, `plain`, `octet-stream`)
- **parameter** — optional modifiers: `charset=utf-8`, `boundary=...`

---

### Where it appears

- **Request** — tells the server how to parse the body (POST, PUT, PATCH)
- **Response** — tells the browser/client how to handle the body

GET requests have no body → `Content-Type` is irrelevant on GET.

---

### charset

Always add `; charset=utf-8` for text types — without it, some clients default to ISO-8859-1 and misread non-ASCII characters.

```
Content-Type: text/html; charset=utf-8
Content-Type: application/json   ← JSON is always UTF-8 per spec, no need
```

## Read more
- [[Content-Type common values grouped by purpose]]
- [[API Design - MOC]]
