---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

After the WebSocket upgrade handshake completes, the **TCP connection stays open continuously** and both client and server can **send data at any time** without request/response pairing.

Key characteristics:
- **Persistent:** The connection remains open until explicitly closed by either side
- **Bidirectional:** Either party can send data independently
- **Full-duplex:** Both parties can send and receive simultaneously
- **Real-time:** No need for the client to poll or wait for a response

This enables true real-time communication scenarios: chat applications, live notifications, collaborative editing, live dashboards, gaming, stock market feeds, etc.

The connection is established once with the upgrade handshake, then either side can push updates whenever data is available. Compare this to HTTP where each update requires the client to ask first.

WebSocket preserves TCP's reliability guarantees—data is guaranteed to arrive in order and complete.

## Links

- [[Persistent connections enable continuous bidirectional data flow]]
- [[TCP provides reliable ordered error-checked data delivery over networks]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
