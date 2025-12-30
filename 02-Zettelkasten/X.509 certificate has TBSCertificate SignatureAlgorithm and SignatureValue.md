---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

An X.509 certificate consists of three main components at its top level.
The structure separates the actual certificate data from the signature information.

**TBSCertificate** (To Be Signed Certificate) contains all the certificate data including identity, public key, and validity period.
This is the portion that gets hashed and signed by the CA.

**SignatureAlgorithm** identifies which cryptographic algorithm the CA used to create the signature.
Common values include RSA with SHA-256, ECDSA with SHA-384, or GOST R 34.10-2012 for Kazakhstan.

**SignatureValue** contains the actual bytes of the digital signature.
The CA creates this by hashing the TBSCertificate and encrypting the hash with its private key.

This three-part structure enables anyone with the CA's public key to verify the certificate.
They hash the TBSCertificate, decrypt the SignatureValue, and compare the two hashes.

The separation of signed data from signature follows standard digital signature patterns.
The same structure appears in CMS/PKCS#7 and other signed data formats.

## Links
- [[TBSCertificate contains all data that gets signed]]
- [[CA signs certificate with private key to prove authenticity]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[X.509 Certificates MOC]]
