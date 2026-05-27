---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

A mode of operation specifies the systematic method for applying a block cipher to messages longer than one block.
The mode determines how blocks are linked together and how the cipher is applied repeatedly.

Block ciphers like AES can only encrypt one fixed-size block at a time.
Real messages are usually much longer, requiring a strategy for processing multiple blocks.

### Common Modes

Different modes provide different security and performance trade-offs.
**CBC** (Cipher Block Chaining) provides good security but cannot parallelize encryption.
**CTR** (Counter Mode) allows parallel encryption but requires careful nonce management.
**GCM** (Galois/Counter Mode) adds authentication to encryption in one operation.

### Parallelization

The mode affects whether encryption can be parallelized.
Sequential modes like CBC must encrypt blocks one after another.
Parallel modes like CTR and GCM can encrypt multiple blocks simultaneously on multi-core systems.

### Initialization Vector

Some modes require an **initialization vector (IV)** to ensure randomness.
The IV must be unique for each encryption with the same key.

### Security Considerations

Wrong mode selection can undermine security.
ECB mode is notoriously insecure as it produces identical ciphertext for identical plaintext blocks.

---

## Links
- [[Block cipher processes fixed-size data chunks]]
- [[CBC mode chains blocks by XORing with previous ciphertext]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[GCM mode combines encryption with authentication tag]]
- [[IV ensures identical plaintext produces different ciphertext]]