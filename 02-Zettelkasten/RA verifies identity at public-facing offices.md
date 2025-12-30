---
created: 2025-12-24
tags: [pki/ca]
sr-due:
sr-interval:
sr-ease:
---

A Registration Authority (RA) is the front-end entity that verifies identities on behalf of the CA.
The RA meets applicants face-to-face or online, checks documentation, but doesn't sign certificates itself.

The separation of duties enhances security.
The CA's signing key stays in a secure data center while RAs operate in public-facing locations.

RAs verify identities and forward approved requests to the CA for signing.
Think of the RA as the "identity verification department" and the CA as the "signing department."

One CA can have many RAs distributed geographically.
This allows local identity verification without requiring CA infrastructure in every location.

In Kazakhstan's system, service centers across cities act as RAs.
You visit a local center to verify your identity, but the actual certificate signing happens at NCA's central facility.

The RA officer checks your government-issued ID, compares it to you in person, and verifies supporting documentation.
After approval, the request is sent to the CA which signs the certificate.

This model scales well for large organizations or national PKIs.
Banks might have RA desks in every branch, all feeding requests to a central CA.

Some systems use automated RAs for domain validation.
The RA automatically verifies domain control via DNS or email challenges, then forwards the request to the CA.

## Links
- [[CA verifies identity before issuing certificates]]
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[PKI MOC]]
