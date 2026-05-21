---
created: 2026-05-14
aliases: [curl]
tags: [linux, cli-tools, curl, http, networking, api]
---

`curl` (**c**lient **URL**) sends and receives data over HTTP, HTTPS, FTP, SCP, and many other protocols. The CLI equivalent of Postman — scriptable, pipeable, no GUI overhead. Default workflow tool for testing REST APIs.

## Why use curl over Postman?

Faster: paste, edit, hit enter. Composable with `jq`, `grep`, shell variables. Reproducible — share a one-liner instead of a Postman export. Works over SSH on servers with no GUI.

---

What is the simplest curl command?

`curl https://api.example.com` performs a GET and prints the body to stdout.

---

What does `-X` do?

Sets the HTTP **method**: `curl -X POST`, `-X PUT`, `-X DELETE`. With `-d` curl auto-sets POST, so `-X` is only needed for non-default methods.

---

What does `-d` do?

Sends a request **body**. `-d '{"k":"v"}'` for inline, `-d @file.json` to read from file. Auto-sets `Content-Type: application/x-www-form-urlencoded` — override with `-H`.

---

What does `-H` do?

Adds a request **header**. Repeat for multiple: `-H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"`.

---

What does `-i` vs `-v` show?

`-i` includes response **headers** in output. `-v` (verbose) prints the full request/response trace including TLS handshake — best debug flag.

## Essential flags

| Flag | Purpose |
|------|---------|
| `-X METHOD` | HTTP method |
| `-d DATA` | request body (`@file` to read) |
| `-H "K: V"` | request header |
| `-i` | include response headers |
| `-I` | HEAD request only |
| `-v` | verbose (full request + TLS) |
| `-s` | silent (no progress bar) |
| `-S` | show errors even when silent |
| `-o file` | write body to file |
| `-O` | save with remote filename |
| `-L` | follow redirects |
| `-k` | skip TLS verification (testing only) |
| `-u user:pass` | basic auth |
| `-b "k=v"` | send cookies |
| `-c file` | save cookies to file |
| `--data-urlencode "k=v"` | URL-encode value |
| `-w "%{http_code}"` | print response metadata |
| `-f` | fail silently on HTTP errors (CI-friendly) |
| `--max-time N` | total timeout in seconds |
| `--retry N` | retry failed requests |

## Common patterns

```bash
# GET
curl https://api.github.com/users/torvalds

# GET with headers + pretty JSON
curl -s -H "Accept: application/json" https://api.example.com/users | jq

# POST JSON
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "role": "admin"}'

# POST from file
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d @payload.json

# Bearer auth
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/me

# Basic auth
curl -u admin:secret https://api.example.com/admin

# Upload file (multipart)
curl -X POST https://api.example.com/upload \
  -F "file=@photo.jpg" \
  -F "title=vacation"

# Download file
curl -L -O https://example.com/archive.tar.gz

# Only headers
curl -I https://example.com

# Debug full request
curl -v https://api.example.com

# Save cookies, reuse later
curl -c cookies.txt -d "user=a&pass=b" https://example.com/login
curl -b cookies.txt https://example.com/dashboard

# Check status code only
curl -s -o /dev/null -w "%{http_code}\n" https://example.com

# CI-friendly: fail on 4xx/5xx, retry
curl -fsSL --retry 3 --max-time 30 https://example.com/script.sh | sh
```

## Read more

- [[jq parses, filters, and transforms JSON data on the command line]]
- [[Heredoc passes multi-line text as stdin using cat and EOF marker]]
- [[Linux MOC]]
- [[Networking MOC]]
