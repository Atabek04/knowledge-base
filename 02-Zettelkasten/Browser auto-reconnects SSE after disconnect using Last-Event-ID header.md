---
created: 2026-04-28
tags: [networking/sse]
---

When an SSE connection drops, the browser automatically reopens it after a delay (default 3 s).

On reconnect it adds:
```
Last-Event-ID: <last received id>
```

The server uses this to resume from the right position, not the beginning.

This is built into the `EventSource` spec — no manual reconnect logic needed on the client.

WebSocket has no equivalent: reconnection must be coded manually.

### Read more
- [[SSE id field marks event position so client can resume after reconnect]]
- [[SSE retry field lets server control reconnection delay in milliseconds]]
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]]
- [[SSE MOC]]
