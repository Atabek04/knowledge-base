---
created: 2025-12-08
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---
A **packet** is a **chunk of data** that gets transmitted over the network. 

When you send data across the internet, it doesn't travel as one continuous stream—it's broken into smaller pieces called packets.

Think of it like shipping a 1000-page book. 
Instead of one massive shipment, you break it into smaller boxes (packets), maybe 10 boxes with 100 pages each. 
Each travels independently through the postal system and gets reassembled at the destination.

Each packet contains:
- **Header information**: Source address, destination address, sequence number, checksums, etc.
- **Payload**: The actual data (a portion of your file, message, etc.)

The size of packets is limited by the **Maximum Transmission Unit (MTU)**, which is the maximum size a packet can be on a network (typically around 1500 bytes).

The network layer automatically breaks large data into appropriately-sized packets, and TCP tracks them using sequence numbers.

## Links

- [[TCP sequence numbers track individual bytes for ordering and completeness]]
- [[TCP stream abstraction hides packetization from applications]]
- [[Maximum Transmission Unit limits packet size on network links]]
- [[TCP MOC]]
