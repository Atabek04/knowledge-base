---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

NCALayer is Kazakhstan's middleware that connects web browsers to local cryptographic hardware.
It solves the problem of browser-based applications needing access to hardware tokens and local key storage.

Modern browsers removed support for NPAPI plugins for security reasons.
This eliminated the ability for websites to directly access USB tokens or smart cards.

**NCALayer architecture**:
1. Native application runs on user's computer
2. Opens WebSocket server on localhost
3. Websites connect via JavaScript
4. NCALayer accesses hardware tokens and PKCS-12 files
5. Returns signature results to website

The WebSocket connection stays within the local machine.
External websites cannot bypass this — only localhost can connect to localhost.

**Security model**:
- User explicitly approves each signature operation
- PIN entry happens in NCALayer UI, not the webpage
- Private keys never leave the token or local storage
- Websites only receive signature output, never keys

The middleware handles complexity of different token types.
Websites use a simple JavaScript API regardless of hardware vendor.

**Browser compatibility** covers all major browsers.
Chrome, Firefox, Edge, Safari all support WebSocket connections.

**Installation required**: Users must install NCALayer before using e-government services.
The NCA provides installers for Windows, macOS, and Linux.

This approach became the standard solution worldwide.
Other countries implemented similar middleware for their national PKI systems.

## Links
- [[NCALayer runs WebSocket server on localhost port 13579]]
- [[NCALayer accesses hardware tokens and PKCS-12 files]]
- [[Modern browsers removed plugin support for security]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[Cryptographic Standards MOC]]
