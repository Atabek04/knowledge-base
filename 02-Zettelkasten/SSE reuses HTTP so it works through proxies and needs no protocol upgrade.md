---
created: 2026-04-28
tags: [networking/sse]
---

SSE is a plain HTTP response — no `Upgrade` header, no protocol switch, no special port.

HTTP proxies, load balancers, and CDNs see it as a normal long-running request and pass it through without special configuration.

WebSocket requires an `Upgrade: websocket` handshake. Some corporate proxies block or mishandle this, causing connection failures.

SSE over HTTPS (TLS) also means the stream is encrypted with zero extra setup — same as any HTTPS request.

### Read more
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]]
- [[SSE streams server events to client over a single persistent HTTP connection]]
- [[SSE MOC]]
