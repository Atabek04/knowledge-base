---
created: 2025-12-24
tags: [pki/ca]
sr-due:
sr-interval:
sr-ease:
---

An Intermediate CA is a Certificate Authority that sits between the root CA and end-entity certificates in the trust hierarchy.
It's signed by the root CA but does the actual work of signing user, server, and device certificates.

The intermediate's private key is online and accessible for automated certificate signing.
This allows the CA to issue thousands of certificates daily without accessing the offline root key.

Using intermediates provides a critical security layer.
If an intermediate's private key is compromised, only that intermediate needs to be revoked — the root stays secure.

The root CA can revoke a compromised intermediate and issue a new one.
End users don't need to update their trust stores — they still trust the same root.

One root CA typically has multiple intermediate CAs for different purposes.
Separate intermediates might handle TLS certificates, code signing, email certificates, or different geographic regions.

Intermediate certificates have shorter validity periods than roots, often 5-10 years.
This provides more opportunities to rotate keys and update cryptographic algorithms.

The intermediate certificate is transmitted along with the end-entity certificate during TLS handshakes.
Clients use it to build the complete chain from the end certificate back to their trusted root.

Some deployments use multiple levels of intermediates (subordinate CAs).
This creates longer chains but provides more granular access control and risk isolation.

## Links
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[Intermediate CA compromise only requires revoking that intermediate]]
- [[Certificate chain includes end certificate plus all intermediates]]
- [[PKI MOC]]
