---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

SignedInfo is the core element in XMLDSig that gets signed by the private key.
It contains all the metadata about what was signed and which algorithms were used.

The SignedInfo element includes:
- **CanonicalizationMethod**: how SignedInfo itself is canonicalized before signing
- **SignatureMethod**: which signature algorithm to use (RSA, ECDSA, GOST)
- **Reference**: one or more references to signed data

Each **Reference** element describes one piece of signed data.
Multiple References enable signing different elements in one signature.

The Reference contains:
- **URI**: identifier pointing to the data (element ID, external URL, or empty for whole document)
- **Transforms**: operations applied before hashing
- **DigestMethod**: hash algorithm (SHA-256, SHA-512, Streebog)
- **DigestValue**: the actual hash of the transformed data

The entire SignedInfo is canonicalized using the specified CanonicalizationMethod.
This ensures consistent byte representation before signing.

The signature is computed over the canonicalized SignedInfo bytes.
Changing any element, attribute, or reference invalidates the signature.

**Verification** requires:
1. Canonicalize SignedInfo using specified method
2. For each Reference, apply Transforms and compute digest
3. Verify each DigestValue matches the computed hash
4. Verify SignatureValue over canonicalized SignedInfo

The SignedInfo structure separates "what to sign" from "the signature."
This enables clear distinction between signed content metadata and the signature itself.

## Links
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Reference element points to data being signed]]
- [[DigestValue holds hash of referenced data]]
- [[SignatureValue contains actual signature bytes]]
- [[Canonicalization normalizes XML before signing]]
- [[Transforms apply operations before hashing]]
- [[Digital Signatures MOC]]
