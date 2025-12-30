---
created: 2025-12-24
tags: [certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

Kazakhstan's national cryptographic standard is ST RK GOST R 34.10-2015 for digital signatures.
This is the Kazakhstan State Standard (ST RK) based on Russia's GOST R 34.10-2012.

The standard mandates **512-bit keys** for all qualified electronic signatures.
This provides enhanced security for legal and government documents requiring long-term validity.

The National Certification Authority (NCA) issues all qualified certificates using this standard.
Citizens and organizations must use GOST R 34.10-2015 for legally binding digital signatures.

The standard specifies the exact elliptic curve parameters to be used.
All implementations must use the same curve to ensure interoperability.

**Streebog-512** (GOST R 34.11-2012 with 512-bit output) is the required hash function.
Documents are hashed with Streebog-512 before signature creation.

The NCA provides **NCALayer** as the middleware for browser-based signing.
NCALayer interfaces with hardware tokens or PKCS#12 files containing GOST keys.

**KalkanCrypt** is the certified cryptographic library implementing ST RK GOST R 34.10-2015.
Application developers use this library to ensure compliance with Kazakhstan standards.

Electronic government services in Kazakhstan only accept GOST signatures.
RSA or ECDSA signatures are not valid for ЭЦП (qualified electronic signatures).

The **Electronic Invoicing System (ИС ЭСФ)** requires GOST signatures on XML documents.
XMLDSig format is used with GOST algorithms for invoice signing.

International software must add GOST support to work with Kazakhstan PKI.
BouncyCastle library provides GOST implementations for Java applications.

## Links
- [[GOST R 34.10-2012 supports 256-bit and 512-bit key sizes]]
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[GOST R 34.11 is hash function called Streebog]]
- [[BouncyCastle and KalkanCrypt provide GOST algorithm implementations]]
- [[GOST signature process hashes message then signs with private key]]
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]]
- [[X.509 Certificates MOC]]
