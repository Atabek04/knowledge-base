---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

### Core Concept

Asymmetric cryptography uses **two mathematically related keys** instead of one.

The keys work in two opposite modes depending on the goal:

| Goal | Operation | Who does it |
|---|---|---|
| **Confidentiality** | encrypt with public key | anyone |
| | decrypt with private key | owner only |
| **Signatures** | sign with private key | owner only |
| | verify with public key | anyone |

The public key can be freely distributed to anyone.

Think of it like a mailbox 📫 with a mail slot.
Anyone can drop letters through the slot (public key) but only you have the key to open the box (private key).

> Note: "encrypting with private key" in signatures is technically imprecise.
> The math is similar, but the operation is called **sign/verify**, not encrypt/decrypt.
> Purpose is proving identity, not hiding data.

### Common Algorithms

Common asymmetric algorithms include **RSA**, **ECDSA**, and **GOST R 34.10**.
Each uses different mathematical foundations — RSA uses factorization, ECDSA and GOST use elliptic curves.

### Advantages

The major advantage is solving the **key distribution problem**.
No need to securely share secret keys — the public key is meant to be public.

### Disadvantages

The disadvantage is **performance** — asymmetric operations are much slower than symmetric.
Typical use is for key exchange and digital signatures, not bulk data encryption.

### Hybrid Encryption

Real systems combine both — see [[Hybrid encryption uses asymmetric to exchange key then symmetric to encrypt data]].

---

## Links
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Session key is short-lived symmetric key for single connection]]
- [[1. Cryptography MOC]]
