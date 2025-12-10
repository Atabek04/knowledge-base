---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket eliminates HTTP header overhead after initial handshake

With **HTTP Keep-Alive**, even though the TCP connection is reused, **each message pair still includes HTTP headers**. Headers contain metadata like Content-Type, Content-Length, authorization tokens, cookies, and more.

For a typical HTTP request/response, headers can be several hundred bytes or more.

With **WebSocket**, after the initial upgrade handshake:
- The connection switches to WebSocket protocol
- Messages use lightweight **WebSocket frames** instead of HTTP messages
- The frame overhead is minimal—just a few bytes of framing information

This is a significant efficiency improvement for protocols that exchange many small messages (chat, real-time updates, gaming).

**Example:** If you're sending 100 chat messages per second with polling:
- HTTP: 100 requests × 200+ bytes headers per request = 20KB+ of header overhead
- WebSocket: 100 frames × 2-10 bytes framing = minimal overhead

Over a streaming application's lifetime, the reduction in header overhead compounds significantly, saving bandwidth and reducing latency.

## Links

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
