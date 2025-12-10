---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# SYN synchronizes Initial Sequence Numbers between hosts

SYN stands for "Synchronize." Its purpose is to synchronize the Initial Sequence Numbers (ISN) between two hosts.

When Host A wants to connect to Host B, it sends a SYN packet with its chosen ISN (e.g., 5000). Host B responds with a SYN-ACK, acknowledging that ISN and providing its own ISN (e.g., 8000).

Now both sides know what sequence number to expect from the other.

This **synchronization** allows both sides to track data correctly throughout the connection. Each side knows the starting point for the other side's data stream.

Without SYN synchronization, there would be no way to verify that packets belong to the correct connection or are in the correct order.

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[TCP sequence numbers track individual bytes for ordering and completeness]]
- [[Initial Sequence Number randomization prevents TCP sequence prediction attacks]]
- [[TCP MOC]]
