---
created: 2025-12-24
tags: [cryptography/core]
sr-due:
sr-interval:
sr-ease:
---

XOR (exclusive OR) is a bitwise operation where bits are compared: same bits produce 0, different bits produce 1.
It's fundamental to many cryptographic operations because of its reversible property.

For each bit position: `0 XOR 0 = 0`, `1 XOR 1 = 0`, `0 XOR 1 = 1`, `1 XOR 0 = 1`.
The key property is that XORing twice with the same value returns the original: `X XOR Y XOR Y = X`.

This reversibility makes XOR perfect for encryption and decryption.
In CTR mode: `Plaintext XOR Keystream = Ciphertext`, then `Ciphertext XOR Keystream = Plaintext`.

Both inputs to XOR must be the same length.
You cannot XOR a 128-bit block with a 256-bit block — they must match.

XOR appears everywhere in cryptography.
CBC mode XORs blocks together, stream ciphers XOR keystreams with plaintext, and MAC algorithms use XOR in their mixing functions.

XOR by itself provides **no security** — it's not encryption.
The security comes from XORing with truly random or cryptographically strong pseudo-random data.

Reusing the same XOR key for multiple messages is catastrophic.
If `C1 = M1 XOR K` and `C2 = M2 XOR K`, then `C1 XOR C2 = M1 XOR M2`, revealing information about both messages.

## Links
- [[CBC mode chains blocks by XORing with previous ciphertext]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[Keystream is generated from counter values in CTR mode]]
- [[Cryptography MOC]]
