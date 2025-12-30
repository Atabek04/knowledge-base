---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

Asymmetric cryptography uses two mathematically related keys where data encrypted with one key can only be decrypted with the other.
The **public key** is shared openly and used for encryption, while the **private key** is kept secret and used for decryption.

Anyone can encrypt a message using your public key.
Only you can decrypt it with your corresponding private key.

The keys are generated together as a matched pair.
They cannot be used independently — a public key from one pair won't work with a private key from another pair.

This solves the key distribution problem of symmetric cryptography.
You can freely publish your public key without compromising security.

The relationship also works in reverse for digital signatures.
Encrypting (signing) with the private key can be verified (decrypted) with the public key, proving the signer's identity.

The mathematics ensures that deriving the private key from the public key is computationally infeasible.
RSA relies on factoring large numbers, while ECDSA and ECDH rely on the discrete logarithm problem on elliptic curves.

Asymmetric operations are 100-1000x slower than symmetric operations.
This is why hybrid systems use asymmetric encryption only for key exchange, then symmetric encryption for data.

## Links
- [[Asymmetric cryptography uses public-private key pairs]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Key transport encrypts session key with recipient public key]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[Cryptography MOC]]
