---
created: 2025-12-17
tags: [networking/websocket, programming/javascript]
sr-due:
sr-interval:
sr-ease:
---

# Browser WebSocket API is JS interface to create and manage connections

The **Browser WebSocket API** is a JavaScript interface built into modern browsers for creating and managing **WebSocket connections** on the client side.

## Creating connections

Create a new WebSocket connection using the `new WebSocket()` constructor:

```js
const socket = new WebSocket('ws://example.com/chat');
// or secure:
const socket = new WebSocket('wss://example.com/chat');
```

**Connection schemes:**
- `ws://` — unencrypted (port 80)
- `wss://` — encrypted with TLS (port 443)

The connection will automatically start the HTTP upgrade handshake. Once successful, the connection enters the **OPEN** state and bidirectional communication begins.

---

## Links

- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket has four event handlers]]
- [[WebSocket connection progresses through four lifecycle states]]
- [[WebSocket MOC]]
