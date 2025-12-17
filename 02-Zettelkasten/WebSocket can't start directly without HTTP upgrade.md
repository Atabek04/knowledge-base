---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket can't start directly without HTTP upgrade

![[WebSocket_piggybacking.png]]

**Firewalls and proxies** only allow traffic on ports **80 (HTTP)** and **443 (HTTPS)**. They expect HTTP traffic on these ports — sending WebSocket frames directly would be blocked as **malformed traffic**.

## Why direct WebSocket fails

WebSocket uses the **same ports as HTTP/HTTPS**:
- Port **80** for `ws://` (unencrypted)
- Port **443** for `wss://` (encrypted/TLS)

If WebSocket frames were sent without HTTP upgrade:
- No HTTP method
- No HTTP headers
- Binary frame data instead

Firewalls and proxies would think: "That's **malformed traffic** or an attack — **reject it**."

## Piggybacking solution

WebSocket **piggybacks** on HTTP's established infrastructure, making it appear as normal web traffic. The initial HTTP upgrade request passes inspection, then the connection switches to WebSocket protocol.

---

## Related

- [[WebSocket piggybacking works, because initial request is valid]] — how HTTP upgrade solves this
- [[Designing WebSocket with its own port creates massive problems]] — why new ports aren't the answer
- [[WebSocket designed to reuse HTTP to be compatible and for deployment simplicity]] — design rationale
- [[Single port handles multiple TCP connections via unique socket tuples]] — how HTTP and WebSocket coexist on same port
- [[WebSocket MOC]]
