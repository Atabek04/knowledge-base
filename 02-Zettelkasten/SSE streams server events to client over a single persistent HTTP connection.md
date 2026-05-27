---
created: 2026-04-28
tags: [networking/sse]
aliases: [SSE, Server-Sent Events]
sr-due:
sr-interval:
sr-ease:
---

# SSE streams server events to client over a single persistent HTTP connection

SSE (Server-Sent Events) is a standard for pushing data from server to client over a plain HTTP connection that stays open indefinitely.

The client makes a single GET request. The server responds with headers and keeps the response body open, writing text chunks over time.

Each chunk is an **event** — a small block of plain text the browser parses and delivers to JavaScript.

Key characteristics:
- **Unidirectional**: server → client only
- **Plain HTTP**: no protocol upgrade, no new port
- **Persistent**: one connection lives for the session
- **Text-based**: events are UTF-8 plain text

This is fundamentally different from normal HTTP where the server sends a full response and closes the connection immediately.

---

### Why it matters for AI agents

LLMs generate tokens one at a time. SSE lets the server forward each token to the browser the moment it's generated — users see output appear word by word instead of waiting for the full response.

## Read more
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE uses text/event-stream content type to signal streaming response]]
- [[SSE MOC]]
