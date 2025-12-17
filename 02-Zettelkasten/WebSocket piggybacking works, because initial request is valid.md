---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket piggybacking works, because initial request is valid

Firewalls and proxies **allow WebSocket** because the initial upgrade request is a **valid HTTP request**:

```
GET /chat HTTP/1.1          ← Valid HTTP method and version
Host: server.example.com    ← Valid HTTP header
Upgrade: websocket          ← Valid HTTP header (RFC 2616 allows this)
Connection: Upgrade         ← Valid HTTP header
```

## How proxies handle the upgrade

1. Proxy receives upgrade request — inspects as normal HTTP
2. Proxy sees valid HTTP with `Upgrade` header
3. Server responds with **101 Switching Protocols**
4. Proxy switches to **transparent pass-through mode**

```
Upgrade request → Proxy inspects (HTTP mode) → Server
101 response    ← Proxy inspects             ← Server

[Proxy switches to pass-through mode]

Frame 1 → Proxy forwards bytes → Server (no inspection)
Frame 2 → Proxy forwards bytes → Server (no inspection)
```

## After the upgrade

The proxy no longer understands the traffic (binary WebSocket frames), but it doesn't matter — the connection was already validated, so it just **forwards bytes in both directions** without inspection.

---

## Links

- [[HTTP proxies operate in three modes for different traffic types]]
- [[WebSocket frames are binary data chunks, not HTTP requests]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
