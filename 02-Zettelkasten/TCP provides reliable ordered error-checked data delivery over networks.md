---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# TCP provides reliable ordered error-checked data delivery over networks

TCP (Transmission Control Protocol) is a transport layer protocol that guarantees three critical properties: reliability, ordering, and error-checking.

**Reliability** means data you send is guaranteed to arrive. TCP retransmits lost packets automatically.

**Ordering** means data arrives in the same sequence you sent it. If packets arrive out of order, TCP reorders them before delivering to your application.

**Error-checking** means TCP detects and recovers from corrupted data.

WebSocket and HTTP both operate on top of TCP, leveraging these guarantees. Understanding TCP is essential for understanding how higher-level protocols work.

TCP establishes connections using a three-way handshake and maintains them until explicitly closed.

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[TCP MOC]]
