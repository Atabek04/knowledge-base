---
created: 2025-12-17
tags: [networking/websocket, programming/javascript]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket has four event handlers

The Browser WebSocket API provides four **event handlers** to manage different stages of the connection lifecycle:

## `onopen` — connection established

Fires when the **HTTP upgrade completes successfully** and the connection enters `OPEN` state.

**Common actions:** Send authentication, subscribe to channels, update UI

```js
socket.onopen = (event) => {
    socket.send(JSON.stringify({
        type: 'auth',
        token: 'user-token-123'
    }));
    statusElement.textContent = 'Connected';
};
```

---

## `onmessage` — data received

Fires when data arrives from the server.

**Data types:** String, Blob, or ArrayBuffer (depends on `binaryType` setting)

```js
socket.binaryType = 'arraybuffer'; // or 'blob'

socket.onmessage = (event) => {
    if (typeof event.data === 'string') {
        // Text message
        console.log('Text:', event.data);
    } else {
        // Binary message
        console.log('Binary:', new Uint8Array(event.data));
    }
};
```

---

## `onerror` — error occurred

Fires when an error occurs during communication.

```js
socket.onerror = (error) => {
    console.error('Error:', error);
};
```

---

## `onclose` — connection closed

Fires when the connection is closed.

**Event properties:**
- `code` — close status code (e.g., 1000, 1006)
- `reason` — text description
- `wasClean` — boolean, true if graceful close (both sides sent close frames)

```js
socket.onclose = (event) => {
    if (event.code === 1000) {
        console.log('Normal closure');
    } else if (event.code === 1006) {
        console.log('Abnormal - connection lost');
    }
};
```

---

## Links

- [[Browser WebSocket API is JS interface to create and manage connections]]
- [[WebSocket send method transmits text and binary data]]
- [[WebSocket close status codes indicate termination reason]]
- [[WebSocket MOC]]
