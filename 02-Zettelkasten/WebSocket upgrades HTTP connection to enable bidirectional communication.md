---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket upgrades HTTP connection to enable bidirectional communication

WebSocket cleverly **starts as an HTTP request** and then **upgrades** to the WebSocket protocol. Here's the process:

1. Client establishes TCP connection (three-way handshake)
2. Client sends a special **HTTP Upgrade request** with headers indicating it wants to switch to WebSocket protocol
3. Server responds with **HTTP 101 Switching Protocols** status code
4. **The same TCP connection is now speaking WebSocket protocol** instead of HTTP
5. Bidirectional communication begins with WebSocket frames

This upgrade process is why WebSocket can work through existing HTTP infrastructure like proxies, load balancers, and firewalls. They initially see it as an HTTP request, so they allow it through.

After the upgrade, the connection is no longer bound by HTTP's request-response pattern. Either party can send data at any time.

WebSocket URLs use `ws://` (unencrypted) or `wss://` (encrypted) schemes, distinguishing them from HTTP (`http://`, `https://`).

## Links

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket eliminates HTTP header overhead after initial handshake]]
- [[WebSocket MOC]]
