---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

A trust chain (certificate chain) is the sequence of certificates from an end-entity certificate up to a pre-installed root certificate.
Trust flows down the chain through cryptographic signatures — each certificate is signed by the one above it.

The chain typically has three levels: end-entity → intermediate CA → root CA.
Your website certificate is signed by an intermediate, which is signed by the root.

Verification starts at the end and works backward to the root.
Each certificate's signature is verified using the public key from the certificate above it.

The root certificate is self-signed — it signs itself since there's no higher authority.
Trust in the root is established by pre-installing it in your operating system or browser.

This is called **transitive trust** — if you trust A, and A trusts B, then you trust B.
You trust the root, the root trusts the intermediate (by signing it), so you trust the intermediate.

The chain must be complete and unbroken for verification to succeed.
If any certificate in the chain is missing or has an invalid signature, trust fails.

Servers typically send the complete chain (except the root) during TLS handshakes.
The root is already on your system, so it doesn't need to be transmitted.

Chain length affects performance — longer chains mean more signature verifications.
Most deployments use a three-level hierarchy as a balance between security and efficiency.

## Links
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[Transitive trust flows from root through intermediates to end certificate]]
- [[Certificate chain includes end certificate plus all intermediates]]
- [[PKI MOC]]
