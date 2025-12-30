---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

Asymmetric cryptography uses **two mathematically related keys** instead of one.
The **public key** encrypts data while the **private key** decrypts it.

The public key can be freely distributed to anyone.
Anyone can use it to encrypt messages that only you can decrypt with your private key.

Think of it like a mailbox with a mail slot.
Anyone can drop letters through the slot (public key) but only you have the key to open the box (private key).

Common asymmetric algorithms include **RSA**, **ECDSA**, and **GOST R 34.10**.
Each uses different mathematical foundations — RSA uses factorization, ECDSA and GOST use elliptic curves.

The major advantage is solving the **key distribution problem**.
No need to securely share secret keys — the public key is meant to be public.

The disadvantage is **performance** — asymmetric operations are much slower than symmetric.
Typical use is for key exchange and digital signatures, not bulk data encryption.

Real systems use **hybrid encryption** — asymmetric to exchange a session key, symmetric to encrypt data.
This combines the security of asymmetric with the speed of symmetric.

## Links
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Session key is short-lived symmetric key for single connection]]
- [[Cryptography MOC]]
