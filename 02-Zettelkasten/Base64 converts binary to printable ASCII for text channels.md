---
created: 2025-12-24
tags: [standards/encoding]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

Base64 encoding transforms binary data into a limited set of 64 printable ASCII characters.
This prevents corruption when transmitting binary through systems designed for text.

### Character Set

The 64 characters are: A-Z, a-z, 0-9, and usually `+` and `/`.
Each character represents 6 bits of data (2^6 = 64 possibilities).

### Encoding Process

Every 3 bytes of input (24 bits) become 4 Base64 characters (4 × 6 = 24 bits).
This creates a 33% size overhead — Base64 data is about 1/3 larger than the original.

### Padding

Padding with `=` characters handles input that isn't a multiple of 3 bytes.
One or two `=` signs may appear at the end to indicate padding.

### Not Security

Base64 provides no security — it's encoding, not encryption.
Anyone can decode Base64 instantly using standard tools.

### Common Uses

It's used extensively in cryptography for PEM files, JWTs, email attachments, and data URLs.
Allows embedding binary keys and certificates in text configuration files.

### Variants

Different Base64 variants exist for special contexts.
URL-safe Base64 replaces `+` and `/` with `-` and `_` to avoid URL encoding issues.

### Decoding

Decoding Base64 reverses the process exactly.
Four Base64 characters convert back to the original 3 bytes.

---

## Links
- [[PEM wraps Base64-encoded DER with header and footer]]
- [[Encoding converts data format without providing secrecy]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Cryptographic Standards MOC]]
