---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# TCP sequence numbers track individual bytes for ordering and completeness

TCP uses **byte-level sequence numbers**, not packet-level numbers. Each individual byte of data gets its own sequence number.

If you're sending 1000 bytes, they might be numbered 5000, 5001, 5002... 5999 (assuming your Initial Sequence Number is 5000).

**Ordering:** If packets arrive out of order (e.g., packet 3, 1, 2), the receiver uses sequence numbers to rearrange them back to the correct order before delivering to the application.

**Completeness detection:** If the receiver gets sequence numbers 100, 101, 103 but not 102, it knows that byte 102 is missing and can request retransmission.

**Duplicate detection:** If the same packet arrives twice, sequence numbers let TCP identify and discard the duplicate.

These three properties—ordering, completeness, and duplicate detection—are why TCP is reliable and ordered.

## Links

- [[TCP packets carry data chunks with headers and payload]]
- [[SYN synchronizes Initial Sequence Numbers between hosts]]
- [[ACK acknowledges receipt and specifies next expected sequence number]]
- [[Initial Sequence Number randomization prevents TCP sequence prediction attacks]]
- [[TCP MOC]]
