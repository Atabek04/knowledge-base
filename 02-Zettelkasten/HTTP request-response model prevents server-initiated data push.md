---
created: 2025-12-08
tags: [networking/http]
sr-due:
sr-interval:
sr-ease:
---

HTTP is built on a **request-response model** where the **client must always initiate communication**.

The server cannot send data to the client unless the client asks for it first.

This is a ==fundamental architectural constraint==, not a bug.

HTTP was designed for document retrieval: client requests a page, server responds. This works well for traditional web browsing.

But for real-time scenarios (chat, live prices, notifications), the server often has new data before the client knows to ask for it.

The server must wait for clients to ask, rather than pushing updates immediately.

This limitation led to workarounds like **polling**, and eventually to protocols like **WebSocket** that enable true server push.

## Links

- [[Request-response communication requires new requests for each data exchange]]
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Polling repeatedly requests updates to simulate real-time communication]]
- [[Bandwidth is the max capacity of data in network connection]]
- [[Networking MOC]]
