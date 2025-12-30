---
created: 2025-12-15
tags: [networking/ip]
sr-due:
sr-interval:
sr-ease:
---

# IP addresses flow hierarchically from IANA through RIRs and ISPs

IP address allocation follows a top-down hierarchy:

1. **IANA** (Internet Assigned Numbers Authority) — global authority
2. **RIRs** (Regional Internet Registries) — e.g., ARIN for North America
3. **ISPs** — receive blocks from RIRs
4. **Your router** — receives public IP from ISP

The internet itself is a hierarchical network of ISP routers.

## Links
- [[Routers have private IP for LAN and public IP for internet]]
- [[Network Layer wraps segments into packets by adding IP addresses]]
- [[Networking MOC]]
