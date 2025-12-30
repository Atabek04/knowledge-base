---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

X.509 certificates have evolved through three versions with increasing capabilities.
The version field appears at the beginning of the TBSCertificate structure.

**Version 1 (v1)** was the original specification with basic fields only.
It included just the essential data: serial number, issuer, subject, public key, and validity period.

**Version 2 (v2)** added unique identifiers for issuer and subject.
These identifiers help distinguish between entities that might share the same Distinguished Name.

**Version 3 (v3)** introduced extensions which dramatically expanded certificate capabilities.
Extensions enable features like key usage constraints, subject alternative names, certificate policies, and authority information access.

Modern certificates are almost always v3 because extensions are essential for contemporary PKI.
Key usage extensions prevent signing keys from being used for encryption and vice versa.

Subject Alternative Names (SAN) allow certificates to cover multiple domains or IP addresses.
Authority Information Access extensions provide URLs for OCSP responders and CA issuer certificates.

The version field uses zero-based numbering in the encoding.
v1 is encoded as 0, v2 as 1, and v3 as 2 in the ASN.1 structure.

## Links
- [[TBSCertificate contains all data that gets signed]]
- [[X.509 certificate has TBSCertificate SignatureAlgorithm and SignatureValue]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[X.509 Certificates MOC]]
