---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# FIN terminates TCP connections through graceful shutdown handshake

FIN stands for "Finish." It signals that a host has finished sending data and wants to close the connection.

When a host sends FIN, it's saying "I have no more data to send. Let's close this connection." The other side acknowledges with ACK, then sends its own FIN. A final ACK closes the connection completely.

This **graceful shutdown** ensures both sides are aware the connection is ending. It's different from abruptly dropping the connection, which could lose data.

Unlike the three-way handshake that opens connections, connection closure typically uses a four-way handshake (FIN, ACK, FIN, ACK) because each direction can close independently.

TCP connections have a clear lifecycle: open with SYN, exchange data, close with FIN.

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[TCP MOC]]
