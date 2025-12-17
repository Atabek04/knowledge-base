---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket close handshake is for graceful shutdown

The **close handshake** is a two-sided protocol exchange that ensures both client and server agree to close the connection and cleanly shut down resources.

## Why the handshake matters

- **Allows final messages** to be delivered before connection closes
- **Provides closure reason** via status codes
- **Prevents data loss** from abrupt disconnection

Without a handshake, simply closing the TCP connection could lose in-flight data.

## Close handshake process

1. **Initiator sends Close frame** (opcode `0x8`)
   - Optional status code (e.g., 1000)
   - Optional reason text

2. **Receiver sends Close frame back**
   - Acknowledges the close request

3. **Both sides close TCP connection**
   - Resources cleaned up
   - Connection enters CLOSED state

---

## Links

- [[Either side can initiate TCP connection termination with FIN]]
- [[WebSocket close status codes indicate termination reason]]
- [[WebSocket connection progresses through four lifecycle states]]
- [[WebSocket has four event handlers]]
- [[WebSocket MOC]]
