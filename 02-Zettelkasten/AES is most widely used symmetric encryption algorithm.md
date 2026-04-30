---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

### Overview

AES (Advanced Encryption Standard) is the dominant symmetric encryption algorithm worldwide.
It replaced the older DES standard and became the official U.S. government standard in 2001.

### Block and Key Sizes

AES operates on **128-bit blocks** regardless of key size.
It supports three key lengths: 128, 192, or 256 bits.

The algorithm uses substitution-permutation networks with multiple rounds.
**AES-128** uses 10 rounds, **AES-192** uses 12 rounds, and **AES-256** uses 14 rounds.

### Performance

AES is fast in both hardware and software implementations.
Modern processors include specialized AES instructions (AES-NI) that dramatically accelerate encryption.

### Use Cases

It's used everywhere — HTTPS connections, file encryption, VPNs, and wireless security (WPA2/WPA3).
Banks, governments, and cloud providers all rely on AES.

### Security

Security researchers have extensively analyzed AES for over two decades.
No practical attacks exist against full-round AES when used correctly.

The main security risk comes from weak implementation, not the algorithm itself.
Using weak keys, reusing IVs, or skipping authentication can all compromise security.

---

## Links
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Block cipher processes fixed-size data chunks]]
- [[Mode of operation defines how block cipher processes long messages]]
- [[GCM mode combines encryption with authentication tag]]
- [[1. Cryptography MOC]]
