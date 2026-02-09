---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

NCALayer operates a WebSocket server on localhost port 13579.
Websites connect to this local server to request digital signature operations.

**The WebSocket URL**: `wss://127.0.0.1:13579`
The `wss://` scheme indicates secure WebSocket over TLS.

**TLS certificate** is self-signed by NCALayer installation.
Browsers show warnings which users must accept during initial setup.

The certificate ensures encrypted communication even on localhost.
This prevents other local processes from eavesdropping on signature requests.

**Port 13579** is the standardized port for NCALayer.
All Kazakhstan e-government websites expect to find the service there.

The server only listens on localhost (127.0.0.1).
Remote connections from other machines are impossible.

**JavaScript API** connects from the browser:
```javascript
const ws = new WebSocket('wss://127.0.0.1:13579');
ws.onopen = function() {
    // Send signature request
    ws.send(JSON.stringify({
        method: 'signXml',
        args: [xmlData]
    }));
};
```

**Connection failure** indicates NCALayer isn't running.
Websites detect this and prompt users to install or start NCALayer.

The WebSocket protocol enables bidirectional communication.
NCALayer can request additional information or show PIN prompts.

**Multiple browser tabs** can connect simultaneously.
The server handles concurrent signature requests from different sessions.

The standardized port eliminates configuration complexity.
Developers don't need to discover or configure service endpoints.

## Links
- [[NCALayer bridges browsers to local cryptographic hardware]]
- [[NCALayer accesses hardware tokens and PKCS-12 files]]
- [[Modern browsers removed plugin support for security]]
- [[Kazakhstan NCALayer uses CMS for legal digital signatures]]
- [[Cryptographic Standards MOC]]
