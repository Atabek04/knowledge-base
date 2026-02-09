---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

### Core Concept

Key agreement is a cryptographic protocol where two parties derive the same secret key through mathematical computation without transmitting the key itself.
Each party contributes randomness, and both compute the shared secret independently.

### Implementation

The classic example is Diffie-Hellman, now typically implemented using elliptic curves (ECDH).
Each side sends a public value derived from their private value, but not the private value itself.

### Security

An eavesdropper sees both public values but cannot compute the shared secret.
This relies on the hardness of the discrete logarithm problem.

### Forward Secrecy

The advantage over key transport is **forward secrecy** when using ephemeral keys.
Even if long-term private keys are compromised later, past session keys remain secure.

### Process

Both parties end up with the same shared secret point on an elliptic curve.
This point is then processed through a KDF (Key Derivation Function) to produce actual encryption keys.

### Difference from Key Transport

Key agreement requires both parties to participate actively.
Unlike key transport where one party chooses the session key unilaterally.

### Modern Usage

Modern TLS uses ECDHE (Ephemeral ECDH) for key agreement.
Fresh private values are generated for each session and immediately discarded afterward.

### Important Note

The shared secret must be properly processed through a KDF.
Using the raw shared point directly as an encryption key is insecure.

---

## Links
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Key transport encrypts session key with recipient public key]]
- [[KDF turns shared point into uniform cryptographic keys]]
- [[Ephemeral ECDH provides forward secrecy by using fresh keys]]
- [[Session key is short-lived symmetric key for single connection]]
- [[Cryptography MOC]]
