---
created: 2025-12-11
tags: [topic/networking, topic/http]
sr-due:
sr-interval:
sr-ease:
---

In HTTP/1.1, Keep-Alive is enabled by default.

When the client receives a response, the TCP connection doesn't close immediately.
Instead, it remains open for potential reuse by subsequent requests.

After a timeout period (typically 60–120 seconds of inactivity), the server closes the connection.

This avoids the overhead of repeated TCP handshakes for multiple requests to the same server.

## Links
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[Networking MOC]]
