---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket connection progresses through four lifecycle states

A WebSocket connection progresses through **four distinct states** from creation to closure.

## State 0: CONNECTING

- **Initial state** after `new WebSocket()` is called
- **HTTP upgrade handshake** in progress
- **Cannot send messages** — connection not ready
- Browser is negotiating protocol switch with server

## State 1: OPEN

- **Handshake complete**, connection established
- **Can send and receive messages** freely
- **Normal operational state** — bidirectional communication active
- Application logic executes here

## State 2: CLOSING

- **Close handshake initiated** by either client or server
- **Waiting for close frame** from the other side
- **Cannot send new messages** (close process is in progress)
- Existing in-flight messages may still be processed

## State 3: CLOSED

- **Connection fully closed**
- **No communication possible**
- **Resources cleaned up** by the browser
- Both sides have completed the close handshake or connection dropped

---

## Links

- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket readyState property tracks connection lifecycle phase]]
- [[WebSocket close handshake is for graceful shutdown]]
- [[WebSocket has four event handlers]]
- [[WebSocket MOC]]
