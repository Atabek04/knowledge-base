---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

TBSCertificate is the portion of an X.509 certificate that contains all the actual certificate data.
The name stands for "To Be Signed Certificate" indicating this is what the CA signs.

It includes the certificate version number, typically v3 to indicate extension support.
The serial number uniquely identifies this certificate among all issued by the CA.

The issuer Distinguished Name identifies which CA signed the certificate.
The subject Distinguished Name identifies the entity that owns the certificate.

Validity period specifies the not-before and not-after timestamps.
The certificate is only valid between these two dates.

Subject Public Key Info contains the public key algorithm identifier and the actual key bits.
This is the public key that corresponds to the private key held by the certificate owner.

Extensions provide additional data like key usage constraints, subject alternative names, or certificate policies.
Extensions are optional but commonly used in v3 certificates.

The CA creates a digital signature over the entire TBSCertificate structure.
Any modification to any field invalidates the signature and makes the certificate untrusted.

## Links
- [[X.509 certificate has TBSCertificate SignatureAlgorithm and SignatureValue]]
- [[Certificate version usually indicates v3 for extensions]]
- [[Serial number uniquely identifies certificate from CA]]
- [[Issuer DN identifies CA that signed certificate]]
- [[Subject DN identifies certificate owner]]
- [[Validity period defines not-before and not-after dates]]
- [[Subject Public Key Info contains algorithm and key bits]]
- [[X.509 Certificates MOC]]
