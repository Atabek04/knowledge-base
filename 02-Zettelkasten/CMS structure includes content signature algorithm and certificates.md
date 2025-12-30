---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

The CMS SignedData structure contains multiple components organized in a defined hierarchy.
Understanding this structure is essential for creating and parsing CMS signatures.

**version** indicates which CMS specification version is used.
Typically v1 for basic signatures or v3 for advanced features.

**digestAlgorithms** lists the hash algorithms used by all signers.
For GOST signatures, this includes GOST R 34.11-2012 (Streebog).

**encapContentInfo** (encapsulated content info) contains or references the signed data.
The content can be embedded (attached signature) or external (detached signature).

**certificates** (optional) contains the signer's certificate and optionally the certificate chain.
Including certificates enables verification without accessing external certificate sources.

**crls** (optional) contains Certificate Revocation Lists.
This allows verifiers to check revocation status without external queries.

**signerInfos** contains one or more SignerInfo structures.
Each SignerInfo represents one signature over the content.

The SignerInfo structure itself contains:
- **version**: SignerInfo version
- **sid**: Signer Identifier (certificate reference)
- **digestAlgorithm**: hash algorithm used by this signer
- **signedAttrs** (optional): authenticated attributes like signing time
- **signatureAlgorithm**: signature algorithm (RSA, ECDSA, GOST)
- **signature**: the actual signature bytes
- **unsignedAttrs** (optional): unauthenticated attributes like countersignatures

The entire structure is encoded in ASN.1 using DER encoding.
This ensures byte-for-byte identical encoding across different implementations.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[SignerInfo identifies signer and holds signature value]]
- [[CMS signing hashes data then wraps in ASN.1 container]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Digital Signatures MOC]]
