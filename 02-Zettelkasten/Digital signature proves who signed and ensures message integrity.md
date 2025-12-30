---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

A digital signature is a cryptographic mechanism that provides proof of origin and data integrity.
It combines hashing and asymmetric cryptography to create unforgeable evidence of who signed a document.

Digital signatures provide three critical security properties: authenticity, integrity, and non-repudiation.
These properties make digital signatures legally equivalent to handwritten signatures in many jurisdictions.

**Authenticity** proves the identity of the signer.
Only the holder of the private key can create a valid signature for that public key.

**Integrity** detects any modification to the signed data.
Changing even one bit of the signed content invalidates the signature.

**Non-repudiation** prevents the signer from denying they signed.
The private key is known only to the signer, making it impossible to claim someone else created the signature.

The signature creation process hashes the message then encrypts the hash with the signer's private key.
This produces a signature value that can be verified by anyone with the corresponding public key.

Verification decrypts the signature with the public key and compares it to a fresh hash of the message.
If the values match, the signature is valid and the message is unchanged.

Digital signatures differ from Message Authentication Codes (MACs).
MACs use symmetric keys, providing integrity and authenticity but not non-repudiation.

## Links
- [[Authenticity confirms identity of message sender]]
- [[Integrity detects any modification to signed data]]
- [[Non-repudiation prevents signer from denying signature]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Verification decrypts signature with public key and compares hashes]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Digital Signatures MOC]]
