---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

The Issuer Distinguished Name identifies the Certificate Authority that signed and issued the certificate.
It appears in the TBSCertificate as a structured sequence of naming attributes.

The issuer DN must exactly match the subject DN of the CA certificate that signed this certificate.
This exact match enables building the certificate chain during validation.

A typical issuer DN includes organizational attributes and country code.
Example: `CN=National Certification Authority,O=Government,C=KZ` identifies Kazakhstan's NCA.

When validating a certificate, software searches for a CA certificate whose subject DN matches the issuer DN.
If found, it uses that CA certificate's public key to verify the signature.

The chain continues upward until reaching a root CA certificate.
At each level, the child certificate's issuer DN matches the parent certificate's subject DN.

Intermediate CAs have both an issuer DN (their parent) and appear as issuers for end-entity certificates.
A single CA certificate can be the issuer for thousands of end-entity certificates.

The issuer DN is encoded as an ASN.1 Name structure using the same format as subject DNs.
Parsing requires handling special characters, multi-valued RDNs, and different string encodings.

## Links
- [[Subject DN identifies certificate owner]]
- [[DN is structured identifier with multiple attributes]]
- [[Certificate chain includes end certificate plus all intermediates]]
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[TBSCertificate contains all data that gets signed]]
- [[X.509 Certificates MOC]]
