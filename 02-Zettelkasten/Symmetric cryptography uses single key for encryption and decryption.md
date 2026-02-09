---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### Core Concept

Symmetric encryption uses **one shared secret key** for both encrypting and decrypting data.
The same key that locks the data also unlocks it.

Think of it like a physical padlock where the same key locks and unlocks the mechanism.
Both sender and receiver must possess the identical key.

### Common Algorithms

Common symmetric algorithms include **AES**, **3DES**, and **GOST 28147-89**.
AES is the most widely used modern symmetric cipher.

### Advantages

The main advantage is **speed** — symmetric encryption is very fast.
It efficiently handles large volumes of data like file encryption or disk encryption.

### Key Distribution Challenge

The critical challenge is **key distribution** — how do both parties securely share the same key?
If an attacker intercepts the key during sharing, all encrypted data becomes readable.

### Key Sizes

Typical key sizes are 128, 192, or 256 bits for AES.
Longer keys provide stronger security but may be slightly slower.

### Hybrid Approach

Modern systems often combine symmetric and asymmetric encryption.
Use asymmetric to securely exchange a symmetric key, then use symmetric to encrypt the actual data.

---

## Links
- [[Asymmetric cryptography uses public-private key pairs]]
- [[Encryption transforms data using key to ensure confidentiality]]
- [[AES is most widely used symmetric encryption algorithm]]
- [[Session key is short-lived symmetric key for single connection]]
- [[Cryptography MOC]]
