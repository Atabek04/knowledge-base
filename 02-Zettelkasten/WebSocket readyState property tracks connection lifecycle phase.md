---
created: 2025-12-17
tags: [networking/websocket, programming/javascript]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket readyState property tracks connection lifecycle phase

The **`readyState` property** returns a **numeric value** indicating the current phase of the WebSocket connection lifecycle.

## Four possible states

- **`WebSocket.CONNECTING` (0)** — handshake in progress, can't send yet
- **`WebSocket.OPEN` (1)** — connection active, can send/receive
- **`WebSocket.CLOSING` (2)** — close handshake initiated
- **`WebSocket.CLOSED` (3)** — fully closed, resources cleaned up

## Checking state before sending

It's common practice to check `readyState` before calling `send()`:

```js
if (socket.readyState === WebSocket.OPEN) {
    socket.send('Hello server');
}
```

---

## Links

- [[WebSocket connection progresses through four lifecycle states]]
- [[WebSocket send method transmits text and binary data]]
- [[Browser WebSocket API is JS interface to create and manage connections]]
- [[WebSocket MOC]]
