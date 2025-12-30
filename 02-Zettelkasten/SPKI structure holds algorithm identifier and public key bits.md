---
created: 2025-12-24
tags: [standards/keys]
sr-due:
sr-interval:
sr-ease:
---

SPKI (Subject Public Key Info) is an ASN.1 structure that packages a public key with its algorithm identifier.
It's the standard container for public keys in X.509 certificates and many other contexts.

The structure contains two main fields: algorithm identifier and public key bits.
The algorithm field uses an OID (Object Identifier) to specify RSA, EC, Ed25519, etc.

For elliptic curves, the algorithm field also includes curve parameters.
This specifies which curve (P-256, Curve25519, etc.) the key uses.

The public key is stored as a BIT STRING containing the algorithm-specific encoding.
RSA keys encode as modulus and exponent, EC keys as point coordinates.

SPKI is algorithm-agnostic — the same structure handles any public key type.
The algorithm OID determines how to interpret the key bits.

In PEM format, SPKI appears as `-----BEGIN PUBLIC KEY-----`.
The same structure is used in X.509 certificates to hold the subject's public key.

SPKI should not be confused with PKCS#1 which is RSA-specific.
PKCS#1 can only hold RSA keys, while SPKI works for any algorithm.

The OID system allows adding new algorithms without changing the SPKI structure.
New curves or signature schemes just get new OIDs.

## Links
- [[ASN.1 defines structure of cryptographic data types]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[RSA public key contains modulus and exponent integers]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[Subject Public Key Info contains algorithm and key bits]]
- [[Cryptographic Standards MOC]]
