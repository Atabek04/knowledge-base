---
created: 2025-12-24
tags: [pki/policy]
sr-due:
sr-interval:
sr-ease:
---

Policy constraints are certificate extensions that restrict which certificate policies are acceptable during chain validation.
They provide fine-grained control over trust, allowing relying parties to accept only certificates meeting specific policy requirements.

Two main constraint types exist: requireExplicitPolicy and inhibitPolicyMapping.
These work together to enforce policy requirements throughout the certificate chain.

The constraints can apply immediately or after a certain number of certificates in the chain.
A value of 0 means "enforce now," 1 means "enforce after one certificate," etc.

Policy constraints appear in intermediate CA certificates to control downstream issuance.
An intermediate can mandate that all end-entity certificates must satisfy specific policies.

Without policy constraints, any certificate from a trusted CA would be accepted.
Constraints add granularity — trust the CA but only for specific purposes or verification levels.

Banking applications commonly use policy constraints to require high-assurance certificates.
They might reject domain-validated certificates and accept only organization or extended validation.

Policy constraints differ from basic constraints which control CA certificate usage.
Basic constraints say "is this a CA?"; policy constraints say "which policies are acceptable?"

Misconfigured policy constraints can cause valid certificates to be rejected.
Testing constraint settings thoroughly is essential before deployment.

## Links
- [[requireExplicitPolicy forces specific policy presence]]
- [[Policy mapping allows CA to equate different policy OIDs]]
- [[Policy OID identifies specific verification requirements]]
- [[Certificate policy defines rules for certificate issuance]]
- [[PKI MOC]]
