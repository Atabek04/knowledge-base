---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### How It Works

CBC (Cipher Block Chaining) mode links each plaintext block with the previous ciphertext block before encryption.
Each block is **XORed** with the previous block's ciphertext, then encrypted.

The first block has no previous ciphertext, so it uses an **initialization vector (IV)** instead.
The IV must be random and unique for each message.

### Security Benefits

This chaining mechanism ensures identical plaintext blocks produce different ciphertext.
Even if two messages start with the same content, different IVs make the ciphertext completely different.

CBC hides patterns in plaintext data.
Unlike ECB mode, repeating data patterns don't create repeating ciphertext patterns.

### Performance

The main disadvantage is **sequential processing** — you cannot encrypt blocks in parallel.
Each block must wait for the previous block's encryption to complete.

Decryption can be parallelized because all ciphertext blocks are already available.
Each block decrypts independently, then XORs with the previous ciphertext.

### Security Considerations

CBC requires careful IV management.
Never reuse an IV with the same key — this can reveal information about the plaintext.

Padding oracle attacks can exploit CBC when error messages leak decryption information.
Modern systems should use authenticated encryption modes like GCM instead.

---

## Links
- [[Mode of operation defines how block cipher processes long messages]]
- [[XOR operation reversibly mixes two equal-length byte strings]]
- [[IV ensures identical plaintext produces different ciphertext]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[GCM mode combines encryption with authentication tag]]
- [[Cryptography MOC]]
