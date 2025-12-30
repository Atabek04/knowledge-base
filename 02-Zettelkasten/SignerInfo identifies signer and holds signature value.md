---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

SignerInfo is a critical component within CMS SignedData containing one signer's signature.
Each SignerInfo represents one entity's signature over the content.

**sid** (Signer Identifier) references the signer's certificate.
It can be either an IssuerAndSerialNumber or a SubjectKeyIdentifier.

**IssuerAndSerialNumber** contains the signer certificate's issuer DN and serial number.
This uniquely identifies which certificate's private key created the signature.

**SubjectKeyIdentifier** contains a hash of the public key.
This alternative is more compact than the full issuer name.

**digestAlgorithm** specifies which hash function this signer used.
Example: SHA-256, SHA-512, or GOST R 34.11-2012.

**signedAttrs** (optional) contains authenticated attributes.
Common attributes include content-type, message-digest, and signing-time.

The **content-type** attribute identifies what kind of data was signed.
The **message-digest** attribute contains the hash of the content.
The **signing-time** attribute provides a timestamp of when the signature was created.

When signed attributes are present, the signature is computed over the attributes.
The attributes themselves reference the content hash, creating a two-level integrity check.

**signatureAlgorithm** identifies the algorithm used to create the signature.
Example: RSA with SHA-256, ECDSA with SHA-384, or GOST R 34.10-2012.

**signature** contains the actual signature bytes.
This is the result of signing the hash (or signed attributes) with the private key.

**unsignedAttrs** (optional) contains unauthenticated attributes.
These might include countersignatures or timestamps added after the original signature.

Multiple SignerInfo structures can exist in one SignedData.
This enables multiple parties to sign the same document.

## Links
- [[CMS structure includes content signature algorithm and certificates]]
- [[CMS wraps data with signature and signer certificate]]
- [[CMS supports multiple signers on same document]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Serial number uniquely identifies certificate from CA]]
- [[Issuer DN identifies CA that signed certificate]]
- [[Digital Signatures MOC]]
