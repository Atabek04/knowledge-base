---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

Creating a GOST digital signature follows the standard signature process with GOST-specific algorithms.
The process ensures message integrity and proves the signer's identity.

**Step 1: Hash the message** using GOST R 34.11-2012 (Streebog).
For 256-bit keys, use Streebog-256. For 512-bit keys, use Streebog-512.
This produces a fixed-length hash regardless of message size.

**Step 2: Generate signature values** using the private key and hash.
The GOST R 34.10 algorithm computes two values (r, s) through elliptic curve operations.

**Step 3: Encode the signature** as an ASN.1 structure.
The signature contains the two integers in a defined format.

**Verification process** reverses the operations using the public key.
The verifier hashes the message with the same algorithm.
Then uses GOST R 34.10 and the public key to check if the signature is valid for that hash.

The signature algorithm uses a random value (nonce) during creation.
This nonce must be cryptographically random and never reused with the same key.
Nonce reuse allows private key recovery, completely breaking the signature scheme.

Unlike RSA, GOST signatures cannot be created without hashing first.
The elliptic curve operations require a hash value as input.

The signature size is twice the key size for GOST.
512-bit keys produce 1024-bit (128-byte) signatures.

The entire process is deterministic except for the nonce generation.
Given the same message and key, different signatures are produced due to different nonces.

## Links
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[X.509 Certificates MOC]]
