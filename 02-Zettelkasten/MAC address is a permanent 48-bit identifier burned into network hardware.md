---
created: 2025-12-15
tags: [networking/datalink]
sr-due:
sr-interval:
sr-ease:
---

# MAC address is a permanent 48-bit identifier burned into network hardware

MAC (Media Access Control) address is a hardware identifier.

Format: `AA:BB:CC:DD:EE:FF` (48 bits / 6 bytes in hex)

Key properties:
- **Burned in** — physically written to network card during manufacturing
- **Permanent** — doesn't change like IP addresses
- **Not configurable** — can't be managed or reassigned

Used by Data Link Layer to identify devices on the same local network.

## Links
- [[Data Link Layer encapsulates packets into frames with MAC headers]]
- [[Switches forward frames within a LAN by reading MAC addresses]]
- [[Networking MOC]]
