---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

If a root CA's private key is compromised, the root must be removed from trust stores on every device globally.
This is a massive undertaking affecting billions of devices — browsers, operating systems, IoT devices, embedded systems.

The compromise allows attackers to issue valid certificates for any domain or identity.
They can impersonate banks, governments, or any website, and browsers would trust the fraudulent certificates.

Removing the root requires coordinated software updates from all OS and browser vendors.
Microsoft, Apple, Google, Mozilla, and others must all push updates to remove the compromised root.

Legacy devices that never receive updates remain permanently vulnerable.
Old phones, embedded systems, and unsupported OS versions will continue trusting the compromised root.

All certificates ever issued by that root (and its intermediates) become suspect.
Even legitimate certificates must be replaced with new ones from different CAs.

The financial and reputational damage is catastrophic for the CA.
DigiNotar went bankrupt after a 2011 compromise; similar fates await other compromised CAs.

This is why root private keys are kept in HSMs in vaults with extensive security controls.
The consequences of root compromise are so severe that extraordinary protection is justified.

Intermediate CA compromise is recoverable — just revoke that intermediate and issue a new one.
The root stays trusted, avoiding the global update nightmare.

## Links
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Intermediate CA compromise only requires revoking that intermediate]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[Root certificate is pre-installed in operating system trust store]]
- [[Trust store contains database of trusted root certificates]]
- [[PKI MOC]]
