---
created: 2025-12-15
tags: [networking/osi]
sr-due:
sr-interval:
sr-ease:
---

# Transport Layer breaks data into segments with TCP headers

When data arrives at the Transport Layer (Layer 4), it's chunked into smaller pieces.

The chunk size is defined by **Maximum Segment Size (MSS)** from the network.

Each chunk gets encapsulated with a **TCP header** containing:
- Source and destination **port numbers**
- **Sequence numbers** for ordering

The result is called a **segment** (TCP) or **datagram** (UDP).

On receiving side, segments are reassembled in correct order using sequence numbers.

## Links
- [[Network Layer wraps segments into packets by adding IP addresses]]
- [[OSI model describes how network communication works]]
- [[Networking MOC]]
