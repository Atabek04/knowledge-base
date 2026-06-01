---
created: 2026-06-01
tags: [networking/sse]
aliases: [long-polling vs SSE]
---

REST terminates cleanly: client sends a request, server responds with full body, TCP closes.

Long-polling stretches this — the server holds the connection open until it has data, then sends and closes. The client immediately re-requests. It simulates push but with overhead at every event boundary.

**Why long-polling falls short for continuous streaming:**

1. **Re-request cost** — client must send a new HTTP request after every batch. Under high event frequency this becomes a flood of handshakes.
2. **No event framing** — the response body is a raw stream. Client can't tell where one logical event ends and the next begins without custom parsing.
3. **No built-in reconnect** — the client must detect disconnects and re-request manually; there's no standard mechanism.

---

### What SSE adds on top of plain HTTP

SSE keeps the same HTTP foundation but fixes all three gaps:

| Problem | SSE solution |
|---|---|
| Re-request overhead | Connection never closes — one persistent body for all events |
| No event framing | `key: value\n\n` protocol — browser knows exactly where each event ends |
| Manual reconnect | `EventSource` reconnects automatically; server controls delay via `retry:` field |

The `Content-Type: text/event-stream` header activates this parsing in the browser. Without it, the browser sees a plain HTTP response and `EventSource` fires nothing.

---

### Comparison at a glance

```
REST:
Client → GET /data
Server → 200 OK + full body → TCP FIN ✓

Long-polling:
Client → GET /poll → Server holds → data ready → 200 + body → TCP FIN
Client → GET /poll → ... (repeat per event)

SSE:
Client → GET /stream
Server → 200 + headers → chunk → chunk → chunk → ... (no FIN)
```

### Read more
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE uses event-stream content type to signal streaming response]]
- [[SSE event has four optional fields - data, event, id, retry]]
- [[Browser EventSource API opens SSE connection and receives events]]
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]]
- [[SSE MOC]]
