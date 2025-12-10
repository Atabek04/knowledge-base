---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket protocol enables real-time applications through persistent connections

WebSocket is a protocol that enables **real-time, bidirectional communication** between client and server over a single TCP connection.

Real-world use cases that WebSocket enables:

**Chat applications:** Users see messages instantly without waiting for polls. The server pushes incoming messages to all connected clients.

**Live notifications:** Applications push alerts, updates, and notifications the moment they occur.

**Collaborative tools:** Multiple users editing the same document see changes in real-time as they type.

**Live dashboards:** Stock prices, analytics, monitoring dashboards update automatically without the client refreshing.

**Multiplayer games:** Game state updates propagate instantly to all players with minimal latency.

**Live streaming:** Viewer count, comments, and interactive features work in real-time.

The key advantage: **no polling required**. The server can push updates immediately when they occur, and clients can respond instantly without waiting for a polling interval.

This makes applications feel responsive and alive, delivering the real-time experience users expect from modern applications.

## Links

- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket eliminates polling by enabling server push]]
- [[WebSocket MOC]]
