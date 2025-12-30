---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

The Subject Distinguished Name identifies the entity that owns the certificate and holds the corresponding private key.
It appears in the TBSCertificate as a structured sequence of naming attributes.

For individual certificates in Kazakhstan, the subject DN includes the person's name and identification number.
Example: `CN=IVANOV IVAN IVANOVICH,serialNumber=IIN123456789012,C=KZ` identifies a citizen.

For organization certificates, the subject DN includes company name and business identification number.
Example: `CN=Example LLP,serialNumber=BIN987654321098,O=Example LLP,C=KZ` identifies a legal entity.

For TLS/SSL certificates, the CN typically contains the domain name.
Example: `CN=example.com,O=Example Inc,C=US` for a website certificate.

The subject DN must be unique among all certificates issued by the same CA.
Two certificates with identical subject DNs from the same issuer would be indistinguishable.

**Subject Alternative Names (SAN)** extension provides additional identities beyond the DN.
SANs can include multiple domain names, email addresses, or IP addresses.

Modern browsers rely primarily on SAN for domain validation rather than the CN field.
The CN field is often deprecated for TLS certificates in favor of explicit SAN entries.

The subject DN appears in certificate selection dialogues when multiple certificates are available.
Users or applications choose certificates based on recognizable subject information.

## Links
- [[Issuer DN identifies CA that signed certificate]]
- [[DN is structured identifier with multiple attributes]]
- [[CN attribute contains person name or domain]]
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]]
- [[TBSCertificate contains all data that gets signed]]
- [[X.509 Certificates MOC]]
