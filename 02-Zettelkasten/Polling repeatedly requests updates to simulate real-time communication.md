---
created: 2025-12-08
tags: [networking/patterns]
sr-due:
sr-interval:
sr-ease:
---

# Polling repeatedly requests updates to simulate real-time communication

Polling is a workaround for HTTP's limitation: server cannot push data first.

Client repeatedly asks "do you have updates?" at fixed intervals (e.g., `GET /messages` every 5 seconds).

**Why it's inefficient:**

1. **Wasted requests**: most polls return "no updates" but consume bandwidth
2. **Latency**: if data arrives after a poll, client waits until next interval
3. **Scalability**: 10,000 clients polling every 5s = 2,000 req/sec even with no updates
4. **Battery drain**: mobile devices waste energy on empty requests

**WebSocket eliminates polling:**

Server pushes data immediately when available. Client asks once (upgrade handshake), then receives updates instantly.

Example comparison for chat:
- **Polling**: 50 requests in 100 seconds, 45 return "no messages"
- **WebSocket**: 1 handshake + N actual messages, zero waste

## Links
- [[HTTP request-response model prevents server-initiated data push]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[Networking MOC]]
