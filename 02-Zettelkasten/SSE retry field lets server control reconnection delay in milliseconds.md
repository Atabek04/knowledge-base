---
created: 2026-04-28
tags: [networking/sse]
---

Browser default reconnect delay is 3000 ms. `retry:` overrides it.

```
retry: 1000
data: fast reconnect stream\n\n
```

After this event, the browser will wait 1 second before reconnecting on any disconnect.

`retry:` persists — it doesn't need to be sent on every event, just once to change the delay.

Use cases:
- **Lower** for real-time feeds where gaps matter
- **Higher** for expensive streams to reduce server load on flapping clients

### Read more
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]]
- [[SSE event has four optional fields - data, event, id, retry]]
- [[SSE MOC]]
