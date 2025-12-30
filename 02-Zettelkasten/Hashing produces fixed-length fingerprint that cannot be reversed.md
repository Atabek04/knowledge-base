---
created: 2025-12-24
tags: [cryptography/hash]
sr-due:
sr-interval:
sr-ease:
---

Hashing transforms input data of any size into a fixed-length output called a digest or fingerprint.
The transformation is one-way — you cannot recover the original input from the hash.

Common hash algorithms produce different output sizes.
**SHA-256** always generates 256 bits (32 bytes) regardless of input size.
**GOST R 34.11-2012** offers 256-bit and 512-bit variants.

Primary uses include **integrity verification** and **password storage**.
When you download a file, comparing its hash with the published hash confirms the file wasn't corrupted or tampered with.

The one-way property makes hashes ideal for storing passwords.
Systems store the hash instead of the password itself.
During login, the entered password is hashed and compared with the stored hash.

Even a single bit change in input produces a completely different hash output.
This property is called the **avalanche effect**.

## Links
- [[Encryption transforms data using key to ensure confidentiality]]
- [[Encoding converts data format without providing secrecy]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[MAC provides integrity and authenticity using keyed hash]]
- [[Cryptography MOC]]
