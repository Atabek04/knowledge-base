---
created: 2025-12-08
tags:
  - networking/websocket
sr-due:
sr-interval:
sr-ease:
---

# WebSocket upgrades HTTP connection to enable bidirectional communication

WebSocket cleverly **<mark style="background: #ADCCFFA6;">starts as an HTTP request</mark>** and then **<mark style="background: #ABF7F7A6;">upgrades</mark>** to the WebSocket protocol. Here's the process:

1. Client establishes TCP connection (three-way handshake)
2. Client sends a special **<mark style="background: #FFB86CA6;">HTTP Upgrade request</mark>** with headers indicating it wants to switch to WebSocket protocol
3. Server responds with **<mark style="background: #BBFABBA6;">HTTP 101 Switching Protocols</mark>** status code
4. **==The same TCP connection is now speaking WebSocket protocol==** instead of HTTP
5. Bidirectional communication begins with WebSocket frames

---

### Implementation

User will send request with `Upgrade` header
we invite our server to switch to one of listed protocols

> **Note:** The [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Connection) header with type `upgrade` 
> must _always_ be sent with the `Upgrade` header.

```
Connection: Upgrade
Upgrade: websocket
```

This upgrade process is why WebSocket can work through existing HTTP infrastructure like proxies, load balancers, and firewalls. 
They initially see it as an HTTP request, so they allow it through.

After the upgrade, the connection is no longer bound by HTTP's request-response pattern. 
Either party can send data at any time.

WebSocket URLs use `ws://` (unencrypted) or `wss://` (encrypted) schemes, distinguishing them from HTTP (`http://`, `https://`).

---

## Why not to use WebSocket directly, without HTTP Upgrade?

Read it here: 
- [[WebSocket can't start directly without HTTP upgrade]]

---

## Links

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket eliminates HTTP header overhead after initial handshake]]
- [[WebSocket MOC]]