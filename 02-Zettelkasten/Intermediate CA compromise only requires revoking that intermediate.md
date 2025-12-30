---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

When an intermediate CA's private key is compromised, the root CA can revoke just that intermediate certificate without affecting the root's trust status.
This isolation is the primary security benefit of using intermediates instead of signing directly with the root.

The recovery process is straightforward: revoke the compromised intermediate, publish the revocation, and issue a new intermediate.
The root CA (still secure in its vault) signs the new intermediate certificate.

End users and their trust stores don't need any updates.
They still trust the same root CA, which now vouches for the new intermediate instead of the compromised one.

Browsers and clients check revocation status during certificate validation.
They'll see the old intermediate is revoked and reject any certificates it signed.

Certificates signed by the compromised intermediate must be re-issued under the new intermediate.
This affects only the subset of certificates from that specific intermediate, not the entire CA's portfolio.

The time to detect and respond to compromise is critical.
The longer a compromised intermediate remains trusted, the more damage attackers can do.

Large CAs often have multiple intermediates for different purposes or regions.
Compromising one doesn't affect the others — damage is contained to one section of the infrastructure.

This compartmentalization demonstrates defense in depth.
The root key is the crown jewel protected at all costs; intermediates are expendable and replaceable.

## Links
- [[Intermediate CA performs daily certificate signing operations]]
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Compromised root CA requires global trust store updates]]
- [[Revocation forcefully invalidates certificate before expiration]]
- [[PKI MOC]]
