---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Every certificate has a validity period defined by "Not Before" and "Not After" dates.
When the current time moves past the "Not After" date, the certificate automatically becomes invalid.

Expiration happens without any action from the CA or certificate holder.
Clients simply check the date during validation and reject expired certificates.

The expiration date is part of the signed certificate content.
Neither the CA nor anyone else can extend it — a new certificate must be issued.

Modern browser standards limit certificate lifetimes to encourage security best practices.
Maximum validity is currently 398 days (about 13 months) for publicly trusted TLS certificates.

Shorter validity periods limit the damage from compromised private keys.
If a key is stolen but the certificate expires soon, the exposure window is limited.

Expiration also forces periodic identity re-verification.
CAs check that domain ownership or organizational status hasn't changed.

Automated renewal systems handle expiration for most certificates.
Tools like certbot renew certificates 30 days before expiration.

Some organizations struggle with certificate expiration tracking.
Forgotten certificates can cause unexpected outages when they expire.

Certificate transparency logs help identify certificates before they expire.
Monitoring services alert administrators about upcoming expirations.

## Links
- [[Certificate renewal reuses existing key pair with new dates]]
- [[Certificate re-issuance generates fresh key pair for security]]
- [[Validity period defines not-before and not-after dates]]
- [[PKI MOC]]
