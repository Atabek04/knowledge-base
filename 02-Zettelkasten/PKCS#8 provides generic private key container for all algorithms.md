---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS#8 defines a universal format for private keys that works with any algorithm.
It wraps the algorithm-specific key data with an algorithm identifier, just like SPKI does for public keys.

The structure includes: version, algorithm identifier (OID + parameters), and private key bytes.
The private key bytes contain the algorithm-specific encoding (PKCS#1 for RSA, SEC1 for EC, etc.).

This algorithm-agnostic design allows one format to handle RSA, EC, Ed25519, and future algorithms.
New algorithms only need an OID and their specific encoding — the PKCS#8 wrapper stays the same.

PKCS#8 comes in two variants: unencrypted and encrypted.
Encrypted PKCS#8 password-protects the private key using algorithms like AES.

In PEM format, unencrypted PKCS#8 uses `-----BEGIN PRIVATE KEY-----`.
Encrypted PKCS#8 uses `-----BEGIN ENCRYPTED PRIVATE KEY-----`.

Modern tools default to PKCS#8 for new key generation.
It's the standard format for storing private keys securely.

The encryption uses PBKDF2 or similar to derive a key from the password.
This protects the private key even if the file is stolen (assuming a strong password).

PKCS#8 replaces older algorithm-specific formats like PKCS#1 for RSA.
The older formats still exist for backward compatibility.

## Links
- [[PKCS#1 defines RSA key format with modulus and exponent]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[PKCS#12 encrypts bundle of certificate and private key]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[Cryptographic Standards MOC]]
