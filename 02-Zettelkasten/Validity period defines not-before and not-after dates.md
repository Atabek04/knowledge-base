---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

Every X.509 certificate contains a validity period specifying when the certificate is valid.
The period consists of two timestamps: notBefore and notAfter.

The **notBefore** timestamp indicates when the certificate becomes valid.
Attempting to use a certificate before this time should result in rejection.

The **notAfter** timestamp indicates when the certificate expires.
After this time, the certificate is no longer considered valid regardless of signature verification.

The validity period protects against long-term key exposure and cryptographic advances.
Limiting certificate lifetime reduces the window during which a compromised key can be misused.

Modern CA/Browser Forum requirements mandate maximum lifetimes for public TLS certificates.
Currently, public TLS certificates cannot exceed 398 days (about 13 months) from issuance.

Internal enterprise certificates often have longer validity periods.
Code signing certificates might be valid for 3 years, while root CA certificates can be valid for 20+ years.

The notBefore time is usually set slightly in the past to account for clock skew.
If a CA sets notBefore to the exact issuance moment, clock differences might cause immediate validation failures.

**Certificate renewal** involves issuing a new certificate before the current one expires.
The new certificate reuses the same key pair but has fresh notBefore and notAfter dates.

Expired certificates can still verify signatures created while the certificate was valid.
Document signatures remain verifiable even after the signing certificate expires.

## Links
- [[TBSCertificate contains all data that gets signed]]
- [[Certificate expiration automatically invalidates after validity period]]
- [[Certificate renewal reuses existing key pair with new dates]]
- [[Certificate re-issuance generates fresh key pair for security]]
- [[X.509 Certificates MOC]]
