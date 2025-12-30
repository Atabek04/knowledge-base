---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

A block cipher encrypts data in **fixed-size chunks** called blocks rather than processing the entire message at once.
Each block is encrypted independently using the same key.

AES uses **128-bit blocks** (16 bytes).
Every chunk of plaintext must be exactly this size before encryption.

If the message doesn't divide evenly into blocks, **padding** is added to the final block.
Common padding schemes include PKCS#7 which fills remaining bytes with the padding length value.

The block cipher itself is just a transformation function.
It doesn't specify how to handle messages longer than one block.

For long messages, you need a **mode of operation** that defines block chaining.
Modes like CBC, CTR, and GCM determine how blocks relate to each other.

Without a mode, encrypting identical blocks produces identical ciphertext.
This leaks information about patterns in the plaintext — the famous ECB penguin problem.

Block size affects both security and performance.
Larger blocks are generally more secure but may be slower and waste space on small messages.

## Links
- [[AES is most widely used symmetric encryption algorithm]]
- [[Mode of operation defines how block cipher processes long messages]]
- [[CBC mode chains blocks by XORing with previous ciphertext]]
- [[CTR mode converts block cipher into stream cipher using counter]]
- [[Cryptography MOC]]
