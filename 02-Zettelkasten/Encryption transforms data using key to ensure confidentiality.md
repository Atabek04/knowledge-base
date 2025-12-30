---
created: 2025-12-24
tags: [cryptography/core]
sr-due:
sr-interval:
sr-ease:
---

Encryption converts plaintext into unreadable ciphertext using a secret **key**.
The transformation is reversible — decryption uses the key to recover the original plaintext.

The primary goal is **confidentiality** — keeping data secret from unauthorized parties.
Without the correct key, the ciphertext appears as random noise.

Two main categories exist based on key usage.
**Symmetric encryption** uses the same key for both encryption and decryption.
**Asymmetric encryption** uses a public key for encryption and a private key for decryption.

Common symmetric algorithms include **AES**, **DES**, and **GOST 28147-89**.
Common asymmetric algorithms include **RSA**, **ECDH**, and **GOST R 34.10**.

The key must remain secret to maintain confidentiality.
If an attacker obtains the key, they can decrypt all protected data.

Encryption differs from encoding which doesn't use keys and provides no security.
It differs from hashing which is one-way and cannot be reversed.

## Links
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Encoding converts data format without providing secrecy]]
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Asymmetric cryptography uses public-private key pairs]]
- [[Cryptography MOC]]
