---
created: 2026-04-27
tags: [signatures/digital, cryptography/asymmetric]
aliases: [why hash before sign, signing size constraint]
sr-due:
sr-interval:
sr-ease:
---

Asymmetric algorithms (RSA, ECDSA, GOST) operate on data smaller than their key size.

A 2048-bit RSA key can only sign up to ~256 bytes directly.
A real document — PDF, XML, contract — is far larger.

Hashing solves this: any document produces a fixed-size digest (e.g. 256 or 512 bits).
The algorithm signs the digest, not the document itself.

This is why "signing a document" always means:
1. Hash the document → fixed-length digest
2. Sign the digest with private key

The hash also provides integrity — any change to the document changes the digest.
So hashing serves two purposes: **size reduction** and **tamper detection**.

---

### Read more
- [[Cryptographic algorithms cannot encrypt arbitrary-length data for different reasons]]

- [[Signing hashes message then encrypts hash with private key]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
