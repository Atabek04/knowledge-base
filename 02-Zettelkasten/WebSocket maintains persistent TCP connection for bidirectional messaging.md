---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket maintains persistent TCP connection for bidirectional messaging

After the upgrade handshake, the TCP connection stays open continuously.

Both client and server can send data at any time without request/response pairing.

Key characteristics:
- **Persistent**: connection remains open until explicitly closed
- **Bidirectional**: either party can send data independently
- **Full-duplex**: both can send and receive simultaneously
- **No polling**: server pushes updates when available

Use cases:
- **Chat**: messages arrive instantly without polling
- **Live notifications**: alerts push the moment they occur
- **Collaborative editing**: changes sync in real-time
- **Live dashboards**: stock prices, analytics update automatically
- **Multiplayer games**: state propagates with minimal latency

WebSocket preserves TCP's reliability — data arrives in order and complete.

## Links
- [[Persistent connections enable continuous bidirectional data flow]]
- [[Polling repeatedly requests updates to simulate real-time communication]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[TCP provides reliable ordered error-checked data delivery over networks]]
- [[WebSocket MOC]]
