---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

GOST R 34.11-2012, commonly known as Streebog, is Russia's cryptographic hash function standard.
It serves as the GOST equivalent of SHA-2 family hash functions.

Streebog produces hash values in two sizes: 256 bits or 512 bits.
The algorithm can be configured for either output length depending on security requirements.

The hash function uses a compression function based on block cipher operations.
It processes input data in 512-bit blocks through multiple rounds of transformations.

**GOST R 34.11-94** was the original hash function, now considered outdated.
Streebog (GOST R 34.11-2012) replaced it with improved security properties.

Streebog is specifically designed to pair with GOST R 34.10 digital signatures.
Messages are hashed with Streebog before signing with GOST R 34.10.

The 512-bit hash variant provides security comparable to SHA-512.
This is mandatory for 512-bit GOST signature keys in Kazakhstan.

The algorithm has undergone international cryptanalysis.
No practical attacks have been found against Streebog when used correctly.

Kazakhstan certificates use Streebog for all hashing operations.
Both document hashing and certificate signature verification use GOST R 34.11-2012.

Implementation must follow the exact specification to ensure interoperability.
Different implementations must produce identical hash values for the same input.

## Links
- [[GOST provides Russian cryptographic independence from Western algorithms]]
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[GOST signature process hashes message then signs with private key]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[X.509 Certificates MOC]]
