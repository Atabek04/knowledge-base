---
created: 2026-04-28
tags: [backend/http, backend/api]
aliases: [Content-Type cheatsheet, Content-Type values]
sr-due:
sr-interval:
sr-ease:
---

# Content-Type common values grouped by purpose

---

### API & Web

| Value | Use |
|---|---|
| `application/json` | REST API bodies |
| `application/x-www-form-urlencoded` | HTML form submit (default) |
| `multipart/form-data` | File upload + form fields mixed |
| `text/html; charset=utf-8` | HTML pages |
| `text/plain; charset=utf-8` | Plain text |

---

### Streaming & Real-Time

| Value | Use |
|---|---|
| `text/event-stream` | SSE — persistent HTTP push |
| `application/x-ndjson` | Newline-delimited JSON stream (one object per line) |
| `application/octet-stream` | Raw binary stream |
| `video/mp4` | Video stream |
| `audio/mpeg` | Audio stream (MP3) |

---

### File Downloads

| Value | Use |
|---|---|
| `application/octet-stream` | Generic download — browser won't render |
| `application/pdf` | PDF |
| `application/zip` | ZIP archive |
| `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` | Excel `.xlsx` |
| `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | Word `.docx` |

> Pair with `Content-Disposition: attachment; filename="file.pdf"` to force download.

---

### Images

| Value | Use |
|---|---|
| `image/png` | PNG |
| `image/jpeg` | JPEG |
| `image/webp` | WebP |
| `image/svg+xml` | SVG |

---

### Web Assets

| Value | Use |
|---|---|
| `text/css` | CSS |
| `text/javascript` | JS (modern standard) |
| `application/wasm` | WebAssembly |
| `font/woff2` | Web font |

---

### Data Formats

| Value | Use |
|---|---|
| `application/xml` | XML |
| `text/csv` | CSV |
| `application/graphql` | GraphQL query body |
| `application/x-protobuf` | Protocol Buffers |

---

### Key Rules

- `application/octet-stream` = safe default for unknown binary — browser downloads, never renders
- `text/event-stream` — no charset suffix, exact value required for SSE
- JSON is always UTF-8 per spec — no charset needed

## Read more
- [[Content-Type header tells receiver how to parse the HTTP body]]
- [[SSE uses text/event-stream content type to signal streaming response]]
- [[API Design - MOC]]
