---
created: 2025-12-24
tags: [pki/policy]
sr-due:
sr-interval:
sr-ease:
---

The requireExplicitPolicy constraint mandates that certificates in the chain must contain specific policy OIDs.
It prevents validation of certificate chains that don't explicitly declare compliance with an acceptable policy.

The constraint includes a skip value indicating how many certificates down the chain before enforcement begins.
`requireExplicitPolicy: 0` enforces immediately, while `requireExplicitPolicy: 1` skips one certificate.

Once enforced, every certificate must contain at least one policy OID from the acceptable policy set.
The "anyPolicy" OID (`2.5.29.32.0`) can satisfy this requirement unless specifically excluded.

This constraint enables organizations to mandate high-assurance certificates.
A system might require all certificates declare compliance with a specific verification policy OID.

The constraint appears in CA certificates to control downstream certificate chains.
An intermediate CA can require all end-entity certificates it signs to have explicit policies.

Validation fails if a certificate lacks the required policy OIDs.
Even if everything else is valid (signatures, dates, revocation), missing policies cause rejection.

Applications can also enforce explicit policy requirements during validation.
The validation code specifies acceptable policy OIDs and rejects chains not meeting them.

Used together with policy mapping controls, this creates sophisticated trust frameworks.
Organizations can accept only certificates meeting their specific security requirements.

## Links
- [[Policy constraints limit acceptable policies in chain]]
- [[Policy OID identifies specific verification requirements]]
- [[Certificate policy defines rules for certificate issuance]]
- [[Policy mapping allows CA to equate different policy OIDs]]
- [[PKI MOC]]
