---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS-12 files encrypt sensitive private keys using password-based encryption.
The password protects against unauthorized access to the stored credentials.

**Password-based key derivation** transforms the password into encryption keys.
PBKDF2 or similar functions make brute-force attacks computationally expensive.

**Salt** is a random value mixed with the password.
It prevents pre-computed rainbow table attacks.

**Iteration count** determines how many times the derivation function runs.
Higher iterations make each password guess slower, deterring brute-force.

Modern PKCS-12 files use thousands or millions of iterations.
Legacy files might use only 1024 or 2048 iterations for compatibility.

**Two separate passwords** can protect different parts:
- **Privacy password**: encrypts the private key
- **Integrity password**: protects the MAC

Most implementations use the same password for both.

**Encryption algorithms** vary by implementation:
- Legacy: 3DES (Triple DES)
- Modern: AES-128-CBC or AES-256-CBC
- Weak: RC2 or RC4 (avoid)

The MAC algorithm is typically HMAC-SHA1 or HMAC-SHA256.
It ensures the file hasn't been tampered with.

**Security strength** depends entirely on password quality.
Weak passwords like "password123" are easily cracked.

**Best practices**:
- Use long random passwords (16+ characters)
- Mix letters, numbers, symbols
- Use password managers
- High iteration counts (100,000+)

**Kazakhstan NCALayer** stores user keys in PKCS-12 files.
The password protects the GOST private keys on disk.

Export from browsers typically creates PKCS-12 with user-chosen password.
Import requires the same password to decrypt and install the key.

## Links
- [[PKCS-12 bundles certificate and private key in encrypted archive]]
- [[P12 file extension indicates PKCS-12 format]]
- [[MAC provides integrity and authenticity using keyed hash]]
- [[HMAC creates fingerprint using hash function and secret key]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[Cryptographic Standards MOC]]
