---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

Implementing GOST algorithms requires specialized cryptographic libraries.
Two primary libraries support GOST standards for application development.

**BouncyCastle** is an open-source cryptographic library for Java, C#, and other languages.
It includes comprehensive GOST support: GOST R 34.10 signatures, GOST R 34.11 hashing, and GOST block ciphers.

BouncyCastle provides both the cryptographic primitives and X.509 certificate handling.
Developers can parse GOST certificates, verify signatures, and create new signatures.

The library is internationally recognized and widely used.
However, for Kazakhstan government systems, certified libraries may be required.

**KalkanCrypt** is the Kazakhstan-certified cryptographic library.
It is officially approved for use in systems handling qualified electronic signatures.

KalkanCrypt implements ST RK GOST R 34.10-2015 with exact compliance to Kazakhstan standards.
Systems processing ЭЦП (qualified electronic signatures) must use certified implementations.

The library provides native interfaces for Windows, Linux, and other platforms.
Applications call KalkanCrypt through its API to perform signing and verification.

**NCALayer** uses KalkanCrypt internally for all cryptographic operations.
This ensures browser-based signing complies with Kazakhstan certification requirements.

BouncyCastle is suitable for development, testing, and non-critical applications.
KalkanCrypt is mandatory for production systems requiring legal compliance.

Some projects use BouncyCastle for parsing and general PKI operations.
Critical signing operations are delegated to KalkanCrypt for certification compliance.

Both libraries handle the complexity of GOST parameter selection and encoding.
Developers work with high-level APIs rather than implementing elliptic curve math directly.

## Links
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[GOST signature process hashes message then signs with private key]]
- [[GOST provides Russian cryptographic independence from Western algorithms]]
- [[X.509 Certificates MOC]]
