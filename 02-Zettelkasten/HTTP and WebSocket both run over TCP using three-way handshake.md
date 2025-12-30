---
created: 2025-12-08
tags: [networking/protocols]
sr-due:
sr-interval:
sr-ease:
---
Both HTTP and WebSocket run on top of TCP, and both use the **same TCP three-way handshake** to establish the initial connection.

The key difference isn't about the TCP connection itself, but about the **protocol** and **communication pattern** that runs **over that TCP connection**.

Think of TCP as a **highway**, and HTTP/WebSocket as the **rules for how traffic moves on that highway**. Both use the same highway, but follow different rules:

**HTTP over TCP:**
- Uses TCP for connection establishment and reliability
- Follows request-response protocol pattern
- Includes HTTP headers in each exchange
- Server cannot initiate communication

**WebSocket over TCP:**
- Uses TCP for connection establishment and reliability
- Follows the upgrade process (starts as HTTP, switches to WebSocket protocol)
- Uses WebSocket frames instead of HTTP messages
- Both parties can initiate communication at any time

The TCP three-way handshake is identical in both cases. The difference emerges after the connection is established—different protocols govern how data flows.

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[Networking MOC]]
