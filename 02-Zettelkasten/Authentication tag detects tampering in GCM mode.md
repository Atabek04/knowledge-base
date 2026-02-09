---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

An authentication tag is a cryptographic checksum that proves ciphertext hasn't been modified.
GCM mode computes this tag using the GHASH function over the encrypted data and any additional authenticated data.

### Tag Size

The tag is typically 128 bits (16 bytes) but can be truncated to 96 or 64 bits for bandwidth-constrained applications.
Shorter tags provide weaker security against forgery attempts.

### Security Properties

Computing the tag requires the encryption key — attackers without the key cannot generate valid tags.
This provides both integrity (detect changes) and authenticity (verify sender).

The tag covers both the ciphertext and any AAD (Additional Authenticated Data).
AAD allows protecting unencrypted metadata like packet headers or message IDs.

### Verification Process

During decryption, the receiver recomputes the tag and compares it to the received tag.
If they don't match, the entire message must be rejected without revealing any plaintext.

**Critical security rule**: Never use decrypted plaintext before verifying the tag.
Using unverified plaintext can lead to padding oracle attacks and other vulnerabilities.

### Tampering Detection

Even changing a single bit anywhere in the ciphertext or AAD will cause tag verification to fail.
This all-or-nothing property prevents subtle tampering attacks.

### Transmission

The tag is transmitted alongside the ciphertext.
It doesn't need to be kept secret — its security comes from being unforgeable without the key.

---

## Links
- [[GCM mode combines encryption with authentication tag]]
- [[MAC provides integrity and authenticity using keyed hash]]
- [[Integrity detects any modification to signed data]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[Cryptography MOC]]
