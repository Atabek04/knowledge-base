---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### How It Works

CTR (Counter Mode) transforms a block cipher into a stream-like cipher by generating a keystream from counter values.
Instead of encrypting the plaintext directly, CTR encrypts successive counter values and XORs the result with plaintext.

The counter starts from a **nonce** (number used once) and increments for each block.
Encrypting `nonce||1`, `nonce||2`, `nonce||3` generates a pseudo-random keystream.

Each keystream block is XORed with the corresponding plaintext block to produce ciphertext.
`Ciphertext = Plaintext XOR Keystream`.

### Advantages

The major advantage is **parallelization** — all counter encryptions are independent.
Multiple blocks can be encrypted simultaneously on multi-core processors.

CTR never encrypts the same counter value twice with the same key if nonces are unique.
The nonce must be different for each message encrypted with the same key.

Decryption is identical to encryption — generate the same keystream and XOR with ciphertext.
This symmetry simplifies implementation.

### Security Considerations

CTR provides no integrity protection by itself.
An attacker can flip bits in the ciphertext, causing predictable bit flips in the decrypted plaintext.

For this reason, CTR is often combined with authentication.
**GCM mode** is essentially CTR plus authentication.

---

## Links
- [[Mode of operation defines how block cipher processes long messages]]
- [[Keystream is generated from counter values in CTR mode]]
- [[XOR operation reversibly mixes two equal-length byte strings]]
- [[GCM mode combines encryption with authentication tag]]
- [[IV ensures identical plaintext produces different ciphertext]]
- [[Cryptography MOC]]
