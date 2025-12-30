---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

SignatureValue is the XMLDSig element containing the actual digital signature.
It holds the Base64-encoded signature bytes computed over the SignedInfo element.

The signature is created by:
1. Canonicalizing the SignedInfo element using the specified CanonicalizationMethod
2. Hashing the canonicalized bytes (hash algorithm from SignatureMethod)
3. Signing the hash with the private key (signature algorithm from SignatureMethod)
4. Base64-encoding the signature bytes
5. Placing the encoded value in the SignatureValue element

**Example**:
```xml
<SignatureValue>
  MCwCFHG8JGKfGnL+78+j5V2QGzbXkT1UAhRu1PEqTfxHt5uqEqLxo
  J7FlWqKJA==
</SignatureValue>
```

The whitespace and line breaks within SignatureValue are ignored.
Only the Base64 characters matter for decoding.

**Verification** reverses the process:
1. Base64-decode the SignatureValue to get signature bytes
2. Canonicalize the SignedInfo element
3. Verify the signature using the public key

If verification succeeds, it proves:
- The SignedInfo hasn't been modified (including all References)
- The signer possessed the private key corresponding to the public key

The signature algorithm must match what's declared in SignatureMethod.
For GOST signatures, this is typically GOST R 34.10-2012 with Streebog-512.

SignatureValue appears at the same level as SignedInfo and KeyInfo.
These three elements form the core of the Signature structure.

Unlike DigestValue which appears in each Reference, there's only one SignatureValue.
It covers all References through signing the entire SignedInfo.

## Links
- [[SignedInfo contains what was signed and how]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Verification decrypts signature with public key and compares hashes]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[KeyInfo embeds signer public key or certificate]]
- [[Digital Signatures MOC]]
