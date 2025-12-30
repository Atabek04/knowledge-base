---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

Cryptographic Message Syntax (CMS) is a standard format for digitally signing and encrypting data.
It provides a container structure that bundles data, signatures, and certificates together.

CMS evolved from PKCS#7 (Public-Key Cryptography Standards #7).
The terms CMS and PKCS#7 are often used interchangeably, though CMS is the newer specification.

The CMS structure wraps signed content in an ASN.1 container.
This container includes the original data, the signature, and optionally the signer's certificate.

**Including the certificate** enables verification without external certificate lookup.
Recipients have everything needed to verify: the data, signature, and public key.

CMS supports different content types:
- **SignedData**: data with one or more signatures
- **EnvelopedData**: encrypted data
- **EncryptedData**: encrypted without key transport
- **DigestedData**: data with hash value

The SignedData content type is most commonly used for digital signatures.
It can contain the original document or just the signature metadata.

CMS uses **DER encoding** for the ASN.1 structure.
The binary format ensures consistent encoding across all implementations.

The file extension `.p7s` commonly indicates detached CMS signatures.
The extension `.p7m` indicates attached CMS signatures containing the data.

Kazakhstan's NCALayer produces CMS signatures for qualified electronic signatures.
All ЭЦП (qualified signatures) use CMS format with GOST algorithms.

## Links
- [[CMS structure includes content signature algorithm and certificates]]
- [[CMS signing hashes data then wraps in ASN.1 container]]
- [[Detached CMS signature stores data separately from signature]]
- [[Attached CMS signature includes original document]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Digital Signatures MOC]]
