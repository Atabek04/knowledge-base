---
created: 2025-12-24
tags: [cryptography/asymmetric, standards/keys]
sr-due:
sr-interval:
sr-ease:
---

### Representation

An elliptic curve public key is a point on a specific elliptic curve represented by two coordinates: x and y.
Each coordinate is a large integer, typically 256 bits for curves like P-256 or Curve25519.

### Curve Specification

The curve itself must also be specified — P-256, Curve25519, secp384r1, etc.
The same x,y coordinates on different curves represent completely different keys.

### Encoding Formats

Points can be encoded in uncompressed or compressed format.
Uncompressed format includes both x and y coordinates (65 bytes for P-256).
Compressed format includes only x and a single bit indicating y's sign (33 bytes for P-256).

### Raw Format

The raw point representation is just these coordinate values.
A typical uncompressed P-256 point is: `04` (prefix) + 32 bytes (x) + 32 bytes (y).

The `04` prefix indicates uncompressed format.
`02` or `03` prefix indicates compressed format with y parity.

### Generation

These coordinates are the public result of scalar multiplication: Public = Private × Generator.
The private key is a scalar (large integer), the generator is a fixed base point on the curve.

### Dependencies

Without the curve parameters, the coordinate values are meaningless.
The curve equation, generator point, and field size are all required to use the key.

---

## Links
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Raw key consists of mathematical values without metadata]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[Cryptographic Standards MOC]]
