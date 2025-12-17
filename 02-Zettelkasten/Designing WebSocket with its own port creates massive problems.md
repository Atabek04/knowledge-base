---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# Designing WebSocket with its own port creates massive problems

WebSocket could theoretically use a dedicated port (e.g., **9000**) instead of HTTP's ports 80/443. But this would create **massive deployment problems**.

## Why dedicated ports fail

**1. Corporate firewalls block non-standard ports**
- Only ports **80**, **443**, and a few others are typically allowed
- Port 9000 would be **blocked by default**

**2. Proxies can't handle unknown ports**
- Corporate proxies only understand HTTP/HTTPS
- Even if traffic reaches port 9000, proxies don't know what to do

**3. Existing infrastructure doesn't work**
- **Load balancers** configured for HTTP wouldn't work
- **CDNs** wouldn't recognize the protocol
- **SSL/TLS certificates** are tied to domains and standard ports

## The trade-off

By reusing HTTP's infrastructure, WebSocket sacrifices protocol "purity" for **real-world deployability**. The HTTP upgrade handshake is the price paid for working through existing network infrastructure.

---

## Links

- [[WebSocket designed to reuse HTTP to be compatible and for deployment simplicity]]
- [[WebSocket can't start directly without HTTP upgrade]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
