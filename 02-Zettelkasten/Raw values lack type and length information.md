---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

Raw cryptographic values are just the mathematical bytes without any structural metadata.
They lack the tag and length information that DER encoding provides.

**Raw RSA public key**: just the modulus and exponent as bare integers.
No indication of which bytes are the modulus vs the exponent.
No indication that this is a public key vs some other data.

**Raw EC public key**: just the x and y coordinates.
No indication of which elliptic curve.
No algorithm identifier.

Raw values require external context to interpret.
The application must know "these bytes are a 256-bit ECC public key on secp256r1."

**Structured formats add metadata**:
- **SPKI** (Subject Public Key Info): includes algorithm identifier and public key bits
- **PKCS-1**: includes structure identifying this as an RSA key
- **PKCS-8**: includes algorithm identifier for any key type

The metadata enables self-describing data.
You can parse a SPKI structure and determine "this is an RSA-2048 public key."

**Protocol designers** must choose between raw and structured formats.
Raw values are smaller but less flexible.
Structured values are larger but self-describing.

**TLS** historically used raw values in handshakes.
The protocol specified exact positions and formats.
Modern TLS uses structured formats for flexibility.

**Signatures** typically use raw values for the signature bytes.
The signature algorithm is specified in surrounding structure (CMS, XMLDSig, X.509).

Raw public keys appear in some blockchain protocols.
Bitcoin addresses are derived from raw public key bytes.

Developers usually work with structured formats.
Libraries handle the encoding/decoding automatically.

## Links
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[DER provides Tag-Length-Value encoding for ASN.1]]
- [[RSA public key contains modulus and exponent integers]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[PKCS-1 defines RSA key format with modulus and exponent]]
- [[Cryptographic Standards MOC]]
