---
created: 2025-12-17
tags: [networking/websocket, programming/javascript]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket send method transmits text and binary data

The **`send()` method** transmits data to the server across the WebSocket connection.

## Sending text and JSON

```js
socket.send('Hello server');

// Usually send JSON:
socket.send(JSON.stringify({
    type: 'message',
    text: 'Hello',
    room: 'general'
}));
```

## Sending binary data

WebSocket supports multiple **binary formats**:

```js
// ArrayBuffer
const buffer = new ArrayBuffer(8);
socket.send(buffer);

// Blob
const blob = new Blob(['binary data']);
socket.send(blob);

// TypedArray (Uint8Array, Int16Array, etc.)
const bytes = new Uint8Array([1, 2, 3, 4]);
socket.send(bytes);
```

## Important constraint

**Only call `send()` when connection is in `OPEN` state.**

Attempting to send before the connection is ready (e.g., during `CONNECTING` state) will fail.

---

## Links

- [[WebSocket has four event handlers]]
- [[Browser WebSocket API is JS interface to create and manage connections]]
- [[WebSocket connection progresses through four lifecycle states]]
- [[WebSocket MOC]]
