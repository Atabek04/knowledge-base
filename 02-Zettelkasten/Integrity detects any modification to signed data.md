---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

Integrity is the property that detects any modification to signed data.
It answers the question: "Has this data been changed since it was signed?"

Digital signatures achieve integrity through cryptographic hashing.
The hash function creates a unique fingerprint of the data that changes completely if the data changes.

The signature is created over the hash, not the original data.
Any modification to the data produces a different hash, making the signature invalid.

**Even minimal changes** invalidate the signature.
Changing a single bit, adding a space, or altering capitalization causes verification to fail.

This property makes digital signatures ideal for ensuring document preservation.
Legal documents, contracts, and certificates cannot be altered without detection.

Integrity detection is automatic during signature verification.
The verifier doesn't need to compare the document manually — the cryptography does it.

**Collision resistance** of the hash function is critical for integrity.
If attackers can find two different messages with the same hash, they can swap content without invalidating the signature.

Modern hash functions like SHA-256 and Streebog-512 provide strong collision resistance.
It's computationally infeasible to find two different inputs producing the same hash.

Integrity differs from authenticity.
Integrity proves the data WASN'T changed, while authenticity proves WHO signed it.

Without proper authenticity checks, an attacker could sign modified data themselves.
Both properties together ensure the data came from the right person AND wasn't modified.

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Authenticity confirms identity of message sender]]
- [[Non-repudiation prevents signer from denying signature]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Verification decrypts signature with public key and compares hashes]]
- [[Digital Signatures MOC]]
