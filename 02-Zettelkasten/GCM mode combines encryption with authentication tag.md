---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

GCM (Galois/Counter Mode) provides both **encryption** and **authentication** in a single cryptographic operation.
It uses CTR mode for encryption and adds a **Galois authentication tag** to detect tampering.

The authentication tag is computed using the GHASH function over the ciphertext and any additional authenticated data (AAD).
AAD allows protecting metadata (like packet headers) without encrypting it.

The tag is typically 128 bits (16 bytes) long.
If even one bit of the ciphertext or AAD changes, tag verification fails.

During decryption, the tag must be verified before revealing any plaintext.
If verification fails, all data must be rejected — using unverified plaintext creates security vulnerabilities.

GCM inherits CTR mode's parallelization advantage.
Both encryption and authentication can be parallelized across multiple processor cores.

The nonce (IV) is critical in GCM — **never reuse a nonce with the same key**.
Nonce reuse catastrophically breaks both confidentiality and authenticity.

GCM is the preferred mode for modern systems.
TLS 1.3 uses GCM almost exclusively, and it's the default for most VPNs and disk encryption.

The main alternative is ChaCha20-Poly1305 which offers similar properties with different performance characteristics.

## Links
- [[Mode of operation defines how block cipher processes long messages]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[Authentication tag detects tampering in GCM mode]]
- [[MAC provides integrity and authenticity using keyed hash]]
- [[IV ensures identical plaintext produces different ciphertext]]
- [[Cryptography MOC]]
