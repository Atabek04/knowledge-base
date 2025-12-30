---
created: 2025-12-15
tags: [networking/osi]
sr-due:
sr-interval:
sr-ease:
---

# Data Link Layer encapsulates packets into frames with MAC headers

Data Link Layer (Layer 2) wraps packets into **frames**.

Frame structure:
- **Header**: source and destination MAC addresses (+ EtherType, VLAN tags)
- **Payload**: the entire packet from Network Layer
- **Trailer**: FCS (Frame Check Sequence) for error detection

Frames are the unit of transmission on a local network segment.

## Links
- [[Network Layer wraps segments into packets by adding IP addresses]]
- [[MAC address is a permanent 48-bit identifier burned into network hardware]]
- [[Frame Check Sequence detects corrupted frames using checksum comparison]]
- [[Physical Layer encodes bits as electrical optical or radio signals]]
- [[Networking MOC]]
