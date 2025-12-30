---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

Web browsers eliminated NPAPI (Netscape Plugin API) plugin support in the mid-2010s.
This removed the ability for websites to load native code extensions.

**Security reasons for removal**:
- Plugins could access all system resources
- No sandboxing or security boundaries
- Source of many browser vulnerabilities
- Enabled drive-by malware installation
- Inconsistent security model across plugins

**Timeline**:
- **Chrome**: Removed NPAPI in 2015
- **Firefox**: Removed all plugins except Flash by 2016, removed Flash in 2021
- **Edge**: Never supported NPAPI (built post-plugin era)
- **Safari**: Restricted then removed plugin support

This created a crisis for digital signature systems.
Many national PKI systems relied on browser plugins to access hardware tokens.

**Previous architecture** (plugin-based):
1. Website loads cryptographic plugin
2. Plugin directly accesses USB tokens
3. Signs data and returns to website

**New architecture** (WebSocket-based):
1. Native application runs on user's machine
2. Website connects via WebSocket or WebExtension
3. Native app accesses tokens and performs signatures

**Kazakhstan adapted** by creating NCALayer.
The WebSocket approach became the new standard.

**Web Crypto API** provides browser-native cryptography.
But it doesn't support hardware token access or national algorithms like GOST.

**WebExtensions** are the modern plugin system.
They're more restricted and can't directly access hardware.

**Progressive enhancement**: Older systems migrated to WebSocket middleware.
The user experience remained similar despite architectural change.

The plugin removal improved browser security significantly.
But required national PKI systems worldwide to redesign their architecture.

## Links
- [[NCALayer bridges browsers to local cryptographic hardware]]
- [[NCALayer runs WebSocket server on localhost port 13579]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[Cryptographic Standards MOC]]
