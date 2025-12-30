---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

A trust store is a database of root CA certificates that the system implicitly trusts for verifying certificate chains.
It's the foundation of PKI trust — if a chain leads to a root in this store, the certificate is trusted.

The trust store is essentially a whitelist of trusted Certificate Authorities.
Each entry includes the root certificate (public key + identity + self-signature).

Different components maintain separate trust stores.
The OS has one, browsers like Firefox have their own, Java applications use cacerts, and specialized software may have custom stores.

Trust stores are read during certificate verification.
When validating a chain, the system checks if the chain terminates at a root present in the trust store.

Entries in the trust store can have constraints limiting their scope.
A root might only be trusted for specific purposes like TLS server authentication or email signing.

Trust store management is critical for security.
Adding a malicious root enables attacks, while accidentally removing legitimate roots breaks functionality.

Organizations sometimes deploy custom trust stores in enterprise environments.
Internal CAs are added to employee devices to enable private PKI for corporate resources.

Trust store updates are distributed through OS and software updates.
When a CA is compromised or fails compliance, vendors remove it via updates.

## Links
- [[Root certificate is pre-installed in operating system trust store]]
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Browser builds chain from server certificate to trusted root]]
- [[Compromised root CA requires global trust store updates]]
- [[PKI MOC]]
