---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

Every certificate issued by a CA must have a unique serial number.
The serial number combined with the issuer DN creates a globally unique identifier for the certificate.

The CA is responsible for ensuring no two certificates it issues share the same serial number.
Reusing serial numbers would make it impossible to distinguish between certificates in revocation lists.

Serial numbers are arbitrary positive integers with no inherent meaning.
CAs typically use sequential numbers, random numbers, or timestamps as serial numbers.

The serial number appears in the TBSCertificate and gets signed by the CA.
Changing the serial number would invalidate the signature.

**Certificate Revocation Lists (CRLs)** identify revoked certificates by serial number.
The CRL contains issuer DN plus a list of serial numbers and revocation dates.

**OCSP requests** specify a certificate by its issuer and serial number.
The OCSP responder returns the status of that specific certificate.

Some implementations display serial numbers in hexadecimal while others use decimal.
The same certificate might show serial number `123456` or `1E240` depending on the tool.

Serial numbers must be positive and no longer than 20 octets (160 bits).
This limit ensures compatibility across different ASN.1 implementations.

## Links
- [[TBSCertificate contains all data that gets signed]]
- [[CRL lists serial numbers of revoked certificates]]
- [[OCSP provides real-time certificate status check]]
- [[Issuer DN identifies CA that signed certificate]]
- [[X.509 Certificates MOC]]
