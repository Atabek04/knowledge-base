---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket close status codes indicate termination reason

**Close status codes** are numeric values included in the close frame to indicate **why the connection is being terminated**.

## Normal closure codes

- **1000** — Normal closure (task complete, browser closed)
- **1001** — Going away (server shutdown, browser navigating away)

## Error and exception codes

- **1002** — Protocol error (malformed frame received)
- **1003** — Unsupported data (e.g., binary when only text expected)
- **1006** — Abnormal closure (connection lost without close frame exchange)
- **1007** — Invalid frame payload data (e.g., non-UTF-8 in text frame)
- **1008** — Policy violation (generic policy-based rejection)
- **1009** — Message too big (payload exceeded size limit)
- **1011** — Server error (unexpected internal condition)

## Using status codes

When the **`onclose` event** fires, the event object includes:
- `code` — the numeric status code
- `reason` — optional text description
- `wasClean` — boolean indicating graceful vs. abrupt closure

```js
socket.onclose = (event) => {
    if (event.code === 1000) {
        console.log('Normal closure');
    } else if (event.code === 1006) {
        console.log('Abnormal closure - reconnecting');
    }
};
```

---

## Links

- [[WebSocket close handshake is for graceful shutdown]]
- [[WebSocket has four event handlers]]
- [[WebSocket MOC]]
