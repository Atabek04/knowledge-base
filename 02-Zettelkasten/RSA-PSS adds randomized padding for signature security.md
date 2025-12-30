---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

RSA-PSS (Probabilistic Signature Scheme) is the recommended RSA signature algorithm.
It adds randomized padding to enhance security over older RSA signature schemes.

Traditional RSA signatures (RSASSA-PKCS1-v1_5) use deterministic padding.
The same message with the same key always produces the same signature.

**RSA-PSS uses randomized padding** with salt values.
Each signature includes a random salt, making the same message produce different signatures each time.

The randomization prevents certain cryptographic attacks.
It eliminates mathematical relationships between signatures of related messages.

The salt doesn't need to be kept secret.
It's a public random value that gets embedded in the signature structure.

During verification, the salt is extracted from the signature.
The verifier reconstructs the padded hash using the salt and compares it to the decrypted signature.

RSA-PSS is specified in PKCS#1 v2.1 and later.
It's becoming the standard for new RSA signature applications.

The security proof for RSA-PSS is stronger than older schemes.
Formal cryptographic analysis shows it's secure under minimal assumptions.

**Modern TLS and PKI** increasingly mandate RSA-PSS.
Certificate Authorities may require it for new certificate issuance.

The padding includes both the message hash and the random salt.
A mask generation function spreads randomness throughout the padded structure.

RSA-PSS signatures are slightly larger than PKCS1-v1_5 signatures.
The size difference is minimal and rarely a practical concern.

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Signing hashes message then encrypts hash with private key]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[ECDSA provides efficient signatures using elliptic curves]]
- [[PKCS#1 defines RSA key format with modulus and exponent]]
- [[Digital Signatures MOC]]
