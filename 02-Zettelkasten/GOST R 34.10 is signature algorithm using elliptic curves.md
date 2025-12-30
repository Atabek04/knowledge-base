---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

GOST R 34.10 is Russia's digital signature standard based on elliptic curve cryptography.
It defines the mathematical operations for creating and verifying digital signatures.

The algorithm is similar to ECDSA but uses different elliptic curves and parameters.
GOST defines specific curves rather than allowing arbitrary curve selection.

**GOST R 34.10-2001** was the original standard supporting 256-bit keys.
It used curves defined over prime fields with specific parameters.

**GOST R 34.10-2012** is the current standard supporting both 256-bit and 512-bit keys.
The 512-bit version provides higher security for long-term signature validity.

The signature algorithm operates on elliptic curve points using modular arithmetic.
Like ECDSA, security relies on the elliptic curve discrete logarithm problem.

GOST signatures require a hash function to process messages before signing.
GOST R 34.11 (Streebog) is the standard hash function paired with GOST R 34.10.

The signature output consists of two integers (r, s) similar to ECDSA.
The signature size matches the key size: 512 bits for 256-bit keys, 1024 bits for 512-bit keys.

Kazakhstan requires GOST R 34.10-2015 for qualified electronic signatures.
This is the Kazakhstan national standard based on GOST R 34.10-2012.

## Links
- [[GOST provides Russian cryptographic independence from Western algorithms]]
- [[GOST R 34.10-2012 supports 256-bit and 512-bit key sizes]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[GOST signature process hashes message then signs with private key]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[X.509 Certificates MOC]]
