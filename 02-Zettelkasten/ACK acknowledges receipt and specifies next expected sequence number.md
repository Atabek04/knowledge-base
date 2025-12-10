---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# ACK acknowledges receipt and specifies next expected sequence number

ACK stands for "Acknowledgment." When a host sends ACK, it confirms receipt of data or a connection request.

The ACK includes a sequence number that indicates which byte the receiver is expecting next.

In the three-way handshake, when Host B sends ACK=X+1, it means: "I received your SYN with sequence X (which counts as one byte), and I'm expecting the next data to start at sequence X+1."

This is why the math is X+1: the SYN flag itself consumes one sequence number in the stream, so the next byte starts at X+1.

ACKs are critical for reliability. They confirm that data arrived safely, allowing the sender to know which bytes need retransmission if acknowledgments don't arrive.

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[TCP sequence numbers track individual bytes for ordering and completeness]]
- [[TCP MOC]]
