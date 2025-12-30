---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

GOST R 34.10-2012 enhanced the original GOST signature standard by adding support for larger key sizes.
The standard defines two security levels through different key sizes.

**256-bit keys** provide the base security level.
This is considered equivalent to 128-bit symmetric security or 3072-bit RSA keys.

**512-bit keys** provide enhanced security for long-term applications.
This is considered equivalent to 256-bit symmetric security or 15360-bit RSA keys.

The key size determines the elliptic curve parameters used.
Each size has specific curves defined in the standard with appropriate security properties.

The hash function size must match the key size.
256-bit keys use Streebog-256, while 512-bit keys use Streebog-512.

The signature size is twice the key size.
256-bit keys produce 512-bit signatures, and 512-bit keys produce 1024-bit signatures.

**Long-term document signatures** typically use 512-bit keys.
The higher security level ensures signature validity even as computational power increases.

Kazakhstan mandates 512-bit keys for qualified electronic signatures.
This provides assurance that signatures remain secure for legal document retention periods.

The larger key size increases signature verification time slightly.
However, modern processors handle 512-bit GOST operations efficiently.

Certificates must declare the specific key size and curve parameters in the Subject Public Key Info.
The OID identifies whether the key is 256-bit or 512-bit variant.

## Links
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[Subject Public Key Info contains algorithm and key bits]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[X.509 Certificates MOC]]
