---
created: 2025-12-15
tags: [networking/datalink]
sr-due:
sr-interval:
sr-ease:
---

# Switches forward frames within a LAN by reading MAC addresses

A switch is a Layer 2 (Data Link) device.

How it works:
- Reads MAC addresses from frame headers
- Maintains a MAC address table (which port → which MAC)
- Forwards frames only to the correct destination port

**Switch ≠ Router:**
- Switch forwards within the same network (using MAC)
- Router forwards between different networks (using IP)

## Links
- [[MAC address is a permanent 48-bit identifier burned into network hardware]]
- [[Data Link Layer encapsulates packets into frames with MAC headers]]
- [[Home router combines router switch and wireless access point]]
- [[Networking MOC]]
