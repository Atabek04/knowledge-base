---
created: 2025-12-15
tags: [networking/osi]
sr-due:
sr-interval:
sr-ease:
---

# Network Layer wraps segments into packets by adding IP addresses

After Transport Layer creates segments, they flow down to Network Layer (Layer 3).

Network Layer adds **source and destination IP addresses** to each segment.

This encapsulated unit is called a **packet**.

Packets can now be routed across different networks — IP addresses identify the final destination.

## Links
- [[Transport Layer breaks data into segments with TCP headers]]
- [[Data Link Layer encapsulates packets into frames with MAC headers]]
- [[OSI model describes how network communication works]]
- [[Networking MOC]]
