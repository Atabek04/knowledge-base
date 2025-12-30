---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

CA verification is the process of confirming the requester's identity before issuing a certificate.
The verification method and thoroughness determine the assurance level — how much trust to place in the certificate.

Different certificate types require different verification levels.
Domain Validation checks only domain control, while Extended Validation requires extensive legal documentation.

The CA must verify that the requester legitimately owns or controls the identity they claim.
For domains, this means proving domain control; for organizations, proving legal existence.

Verification methods vary by certificate type and CA policy.
Some are automated (DNS challenges), others require human review (document verification).

The verification directly impacts certificate trustworthiness.
Weak verification allows attackers to obtain certificates for identities they don't own.

Time to issuance depends on verification complexity.
DV certificates can be issued in minutes, while EV certificates may take days or weeks.

Multi-domain (SAN) certificates require verifying control of all listed domains.
Each domain in the certificate must pass verification separately.

Some CAs maintain databases of previously verified organizations.
This can speed up re-issuance for known customers.

## Links
- [[DV certificates verify domain ownership via DNS or email]]
- [[OV certificates verify organization through business registration]]
- [[CA verifies identity before issuing certificates]]
- [[CSR contains public key and identity information]]
- [[PKI MOC]]
