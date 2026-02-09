---
created: 2025-12-24
tags: [standards/encoding]
sr-due:
sr-interval:
sr-ease:
---

### Definition

A byte is a unit of 8 bits and represents the smallest chunk of data that computer memory can individually address.
It can hold values from 0 to 255 (2^8 = 256 possibilities).

### Memory Addressability

Bits are the fundamental unit (0 or 1), but memory systems work with bytes.
You cannot read or write a single bit in isolation — you work with whole bytes.

### Character Representation

One byte can represent a single ASCII character.
For example, the letter 'A' is byte value 65, 'B' is 66, etc.

### Cryptographic Use

In cryptography, key sizes and data lengths are often measured in bytes or bits.
A 256-bit AES key is 32 bytes (256 ÷ 8 = 32).

### Universality

Bytes are universally the same across all computer systems.
A byte is always 8 bits, making it a reliable cross-platform unit.

### Building Larger Types

Larger data types are built from bytes.
A 32-bit integer uses 4 bytes, a 64-bit number uses 8 bytes.

### Display Format

When displaying binary data, bytes are often shown in hexadecimal.
Each byte becomes two hex digits, making binary data more readable.

### Measurements

File sizes, network throughput, and memory capacity are measured in bytes (KB, MB, GB).
Understanding bytes is fundamental to working with any binary data.

---

## Links
- [[Hexadecimal represents byte using two digits for four bits each]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Cryptographic Standards MOC]]
