---
created: 2025-12-24
tags: [cryptography/core]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

Encoding transforms data into a different representation for safe transport or storage.
The transformation provides **no security** — anyone can reverse it without needing a key.

### Common Schemes

Common encoding schemes include **Base64**, **URL encoding**, and **hex encoding**.
These convert binary data to printable ASCII characters that won't break when transmitted through text-only systems.

The purpose is compatibility, not confidentiality.
Base64 encoding allows binary files to be safely embedded in email or JSON.

### Properties

Decoding is trivial and requires no secret information.
Any program can decode Base64 back to the original binary data.

This fundamentally differs from encryption which requires a secret key to decrypt.
It differs from hashing which cannot be reversed at all.

### Common Mistake

Treating encoding as encryption is a common security mistake.
Storing passwords as Base64 provides zero protection — attackers can immediately decode them.

---

## Links
- [[Encryption transforms data using key to ensure confidentiality]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[PEM wraps Base64-encoded DER with header and footer]]
- [[1. Cryptography MOC]]
