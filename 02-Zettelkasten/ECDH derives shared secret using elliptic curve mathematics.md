---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

ECDH (Elliptic Curve Diffie-Hellman) allows two parties to derive the same shared secret over an insecure channel.
Neither party transmits the secret directly — they exchange public points and each computes the shared secret independently.

### Key Generation

Each party generates a **private scalar** (random number) and a **public point** (private scalar × curve base point).
Alice computes public point A from her private value a, Bob computes public point B from his private value b.

### Exchange Process

Alice and Bob exchange their public points over any channel.
An eavesdropper can see both public points but cannot derive the shared secret.

### Shared Secret Computation

Alice computes the shared secret as `a × B` (her private scalar × Bob's public point).
Bob computes `b × A` (his private scalar × Alice's public point).

The mathematics of elliptic curves ensures both computations yield the same point: `a × B = b × A = (a × b) × G`.
This shared point is then passed through a key derivation function to produce encryption keys.

### Performance Advantages

ECDH provides much better performance than RSA for key exchange.
A 256-bit elliptic curve key provides security equivalent to a 3072-bit RSA key.

### Security

The security relies on the elliptic curve discrete logarithm problem.
Given a public point, finding the private scalar is computationally infeasible.

### Common Curves

Common curves include P-256 (NIST), Curve25519 (modern preference), and GOST curves (Russia/Kazakhstan).

---

## Links
- [[Asymmetric cryptography uses public-private key pairs]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[KDF turns shared point into uniform cryptographic keys]]
- [[Ephemeral ECDH provides forward secrecy by using fresh keys]]
- [[Key agreement derives shared key without transmitting it]]
- [[1. Cryptography MOC]]
