---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

KalkanCrypt is the officially certified cryptographic library for Kazakhstan.
It implements GOST algorithms in compliance with Kazakhstan national standards.

The library is certified by Kazakhstan's national security authorities.
This certification is required for systems handling qualified electronic signatures (ЭЦП).

**Implemented algorithms**:
- **GOST R 34.10-2015**: Digital signature (512-bit keys)
- **GOST R 34.11-2012**: Hash function (Streebog-512)
- **GOST 28147-89**: Block cipher for encryption
- **GOST R 34.12-2015**: Newer block cipher standards

The library provides native interfaces for different platforms.
Windows DLL, Linux shared library, and macOS dylib versions exist.

**API functions** cover all cryptographic operations:
- Key generation
- Signing and verification
- Encryption and decryption
- Certificate operations
- Hardware token access

NCALayer uses KalkanCrypt for all cryptographic operations.
This ensures legal compliance for government services.

**Alternative**: BouncyCastle implements GOST algorithms.
But KalkanCrypt is required for systems needing official certification.

Applications can choose their approach:
- Use KalkanCrypt directly for maximum control
- Use NCALayer for browser-based convenience
- Use both depending on deployment context

**Licensing**: KalkanCrypt is proprietary.
The NCA provides it free for use with Kazakhstan e-government systems.

Development and testing use KalkanCrypt APIs.
Production systems require proper licensing and deployment.

The library includes comprehensive error handling.
Return codes indicate specific failure reasons for debugging.

## Links
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[BouncyCastle and KalkanCrypt provide GOST algorithm implementations]]
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[NCALayer bridges browsers to local cryptographic hardware]]
- [[Cryptographic Standards MOC]]
