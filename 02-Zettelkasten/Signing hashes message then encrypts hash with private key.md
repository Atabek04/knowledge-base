---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

Creating a digital signature follows a two-step process: hash then sign.
This approach enables signing messages of any length while maintaining security.

**Step 1: Hash the message** using a cryptographic hash function.
The hash produces a fixed-length fingerprint regardless of message size.
Common hash functions include SHA-256, SHA-512, or GOST R 34.11 (Streebog).

**Step 2: Encrypt the hash** with the signer's private key.
This produces the signature value that can be verified with the corresponding public key.

Hashing first is essential because asymmetric algorithms have size limits.
RSA and elliptic curve algorithms can only operate on data smaller than the key size.

The hash creates a fixed-size representation that fits within cryptographic constraints.
A 256-bit hash can be signed by any key large enough for that size.

The term "encrypt the hash" is a simplification.
RSA signatures use modular exponentiation, while ECDSA and GOST use elliptic curve point operations.

The mathematical operations are similar to encryption but with different parameters.
For RSA, signing uses the private exponent while encryption uses the public exponent.

**Deterministic signatures** like RSA-PSS or deterministic ECDSA use randomization for security.
The same message signed twice produces different signatures due to random padding or nonces.

The hash function must be collision-resistant.
If attackers can find two messages with the same hash, they can substitute content without detection.

The private key must remain absolutely secret.
Anyone with the private key can create signatures that appear authentic.

## Links
- [[Hashing before signing is required because asymmetric algorithms cannot process arbitrary-length data]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[Verification decrypts signature with public key and compares hashes]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[RSA-PSS adds randomized padding for signature security]]
- [[GOST signature process hashes message then signs with private key]]
- [[Digital Signatures MOC]]
