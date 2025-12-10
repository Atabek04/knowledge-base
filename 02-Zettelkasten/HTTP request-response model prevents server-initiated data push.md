---
created: 2025-12-08
tags: [networking/http]
sr-due:
sr-interval:
sr-ease:
---

# HTTP request-response model prevents server-initiated data push

HTTP is built on a **request-response model** where the **client must always initiate communication**. The server cannot send data to the client unless the client asks for it first.

This creates several problems for real-time scenarios:

**1. Polling inefficiency:** The client must repeatedly ask "do you have updates?" even when there's nothing new, wasting bandwidth and server resources.

**2. Latency:** There's always a delay between when the server has new data and when the client asks for it.

**3. Connection overhead:** Each request requires establishing a connection, sending headers, and processing the request/response cycle.

For scenarios like chat applications, live stock prices, or notifications, this limitation is significant. The server must wait for clients to ask, rather than pushing updates immediately.

This is the fundamental problem that WebSocket solves by enabling server-initiated data push.

## Links

- [[Request-response communication requires new requests for each data exchange]]
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Polling repeatedly requests updates to simulate real-time communication]]
- [[Networking MOC]]
