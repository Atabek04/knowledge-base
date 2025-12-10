---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# Maximum Transmission Unit limits packet size on network links

The **Maximum Transmission Unit (MTU)** is the maximum size a packet can be on a network link. The typical MTU is around **1500 bytes**.

However, not all 1500 bytes are available for your actual data (payload). TCP/IP headers consume about **40 bytes** (20 bytes for TCP header + 20 bytes for IP header).

This leaves approximately **1460 bytes** available for your actual data per packet.

If you want to send **5000 bytes** of data:
- Packet 1: bytes 0-1459 (1460 bytes payload)
- Packet 2: bytes 1460-2919 (1460 bytes payload)
- Packet 3: bytes 2920-4379 (1460 bytes payload)
- Packet 4: bytes 4380-4999 (620 bytes payload)

So your 5000 bytes become 4 separate packets. TCP tracks these using sequence numbers and reassembles them in order.

Understanding MTU is important for performance optimization—if packets are too large, they might be fragmented at lower network layers, reducing efficiency.

## Links

- [[TCP packets carry data chunks with headers and payload]]
- [[TCP MOC]]
