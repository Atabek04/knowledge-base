---
created: 2025-12-08
tags: [networking/patterns]
sr-due:
sr-interval:
sr-ease:
---

In persistent connection communication, the client and server establish a ==connection that stays open continuously==.

Either party can send data at any time ==without initiating a new request or establishing a new connection==.

It's like having an open phone call where both parties can speak whenever they need to. The connection remains active and ready for instant communication.

This pattern enables true real-time communication scenarios. Both client and server can push data in either direction at any moment.

The connection lifecycle is: establish → exchange bidirectional data anytime → close gracefully.

## Links

- [[Request-response communication requires new requests for each data exchange]]
- [[Implement persisten connection communication]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[Networking MOC]]
