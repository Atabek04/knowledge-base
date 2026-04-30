---
created: 2025-12-24
tags: [cryptography/core]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

A KDF (Key Derivation Function) transforms input material into one or more cryptographically strong keys with uniform randomness.
It ensures the output keys are indistinguishable from true random keys.

### Necessity

KDFs are essential after key agreement protocols like ECDH.
The raw shared point has mathematical structure — using it directly as an encryption key is insecure.

### Types

Common KDFs include HKDF (HMAC-based KDF), PBKDF2, and bcrypt/scrypt/Argon2 (password-based).
HKDF is the standard for deriving session keys in modern protocols.

### Inputs

KDFs typically take three inputs: **input key material**, **salt**, and **context info**.
The salt prevents rainbow table attacks, and the context info binds keys to specific purposes.

### Multiple Key Generation

A single KDF can derive multiple keys for different purposes.
From one shared secret, generate separate keys for encryption, MAC, and IV generation.

### Password-Based KDFs

Password-based KDFs like PBKDF2 are intentionally slow.
They include many iterations to make brute-force password cracking expensive.

### Key-Based KDFs

Key-based KDFs like HKDF focus on extracting and expanding entropy.
They're fast because the input is already high-entropy (from ECDH, not a password).

### Output

The output length is configurable.
Generate exactly as many bits as needed for your keys — 256 bits for AES-256, etc.

---

## Links
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Key agreement derives shared key without transmitting it]]
- [[HMAC creates fingerprint using hash function and secret key]]
- [[Session key is short-lived symmetric key for single connection]]
- [[1. Cryptography MOC]]
