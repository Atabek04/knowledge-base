---
created: 2025-12-24
tags: [standards/encoding]
sr-due:
sr-interval:
sr-ease:
---

### Number System

Hexadecimal (hex) is a base-16 number system that represents each byte as exactly two digits.
The 16 digits are 0-9 and A-F, where A=10, B=11, C=12, D=13, E=14, F=15.

### Bit Mapping

One hex digit represents 4 bits (called a nibble), and two hex digits represent one byte (8 bits).
For example, byte value 255 is `FF` in hex, byte value 0 is `00`.

### Readability

Hex is far more readable than binary for displaying binary data.
The byte `11111111` in binary becomes `FF` in hex — much shorter.

### Notation

The `0x` prefix indicates hexadecimal in many programming languages.
`0xFF` means hex FF (decimal 255), `0x10` means hex 10 (decimal 16).

### Cryptographic Use

Hex is ubiquitous in cryptography for displaying keys, hashes, and signatures.
A SHA-256 hash is 32 bytes, displayed as 64 hex digits.

### Direct Mapping

Each hex digit maps directly to 4 bits: `0=0000, 1=0001, ... E=1110, F=1111`.
This direct mapping makes hex-to-binary conversion trivial.

### Common Applications

Cryptographic tools often output data in hex format.
Key fingerprints, message digests, and byte arrays all use hex representation.

### Comparison with Base64

Hex is more compact than Base64 for viewing but not for transmission.
Base64 uses only printable ASCII characters, while hex may need escaping in some contexts.

---

## Links
- [[Byte is eight-bit unit as smallest addressable memory storage]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Cryptographic Standards MOC]]
