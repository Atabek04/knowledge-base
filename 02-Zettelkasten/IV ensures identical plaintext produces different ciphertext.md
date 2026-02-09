---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

An Initialization Vector (IV) is a random block of bits used to ensure that encrypting the same plaintext twice produces different ciphertext.
Without an IV, identical messages encrypted with the same key would produce identical ciphertext, revealing that messages are the same.

### Size Requirements

The IV must be the same size as the cipher's block size.
For AES with 128-bit blocks, the IV is also 128 bits (16 bytes).

### Usage

The IV is used only for the first block in modes like CBC.
It substitutes for "previous ciphertext" which doesn't exist for the first block.

### Secrecy vs Randomness

The IV does not need to be secret — it's often transmitted alongside the ciphertext.
Its purpose is randomization, not secrecy.

However, the IV must be **unpredictable and unique** for each encryption with the same key.
Never reuse an IV with the same key — this can leak information or even reveal the plaintext.

### Mode-Specific Requirements

Different modes have different IV requirements.
CBC requires a random IV, while CTR requires a unique nonce (which can be a simple counter).

### Generation

Generating IVs from weak sources like timestamps or sequential counters can be dangerous.
Use cryptographically secure random number generators.

---

## Links
- [[CBC mode chains blocks by XORing with previous ciphertext]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[GCM mode combines encryption with authentication tag]]
- [[Mode of operation defines how block cipher processes long messages]]
- [[Cryptography MOC]]
