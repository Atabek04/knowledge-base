---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

A certificate progresses through three distinct lifecycle stages from creation to invalidity.
Understanding these stages helps manage certificates and plan for renewal or revocation.

**Issuance stage** begins with key generation and ends when the CA signs the certificate.
The certificate is created, verified, and becomes active at the "Not Before" date.

**Active stage** is the normal operational period where the certificate is valid and in use.
The certificate authenticates servers, signs documents, or encrypts communications as intended.

**End-of-life stage** occurs when the certificate becomes invalid — either through expiration or revocation.
Expired certificates automatically become invalid at the "Not After" date.
Revoked certificates forcefully transition to end-of-life when added to the CRL.

The timeline for a typical 1-year certificate: Day 1 (issued) → Days 2-365 (active) → Day 365+ (expired).
For a revoked certificate: Day 1 (issued) → Days 2-150 (active) → Day 151+ (revoked and end-of-life).

Best practices involve renewing before expiration, typically 30 days prior.
This provides overlap where both old and new certificates are valid during transition.

Certificate management systems track lifecycle stages automatically.
They alert administrators about upcoming expirations and handle automated renewal.

Some compliance frameworks require tracking certificate lifecycles for audit purposes.
Documentation must show when certificates were issued, used, and retired.

## Links
- [[Certificate expiration automatically invalidates after validity period]]
- [[Revocation forcefully invalidates certificate before expiration]]
- [[Certificate issuance begins with key pair generation]]
- [[Certificate renewal reuses existing key pair with new dates]]
- [[PKI MOC]]
