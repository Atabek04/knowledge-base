---
created: 2026-04-28
tags: [networking/sse]
---

The browser stores the last received `id` internally. On reconnect it sends it back:

```
Last-Event-ID: 42
```

The server reads this header and replays only events after position 42 — the client misses nothing.

Without `id`, reconnect starts the stream from scratch.

Server example:
```
id: 1
data: first event\n\n

id: 2
data: second event\n\n
```

IDs are arbitrary strings — sequential integers are conventional but not required.

### Read more
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]]
- [[SSE event has four optional fields - data, event, id, retry]]
- [[SSE MOC]]
