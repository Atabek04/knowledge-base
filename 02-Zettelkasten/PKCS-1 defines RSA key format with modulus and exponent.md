---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS-1 (Public-Key Cryptography Standards #1) defines the specific ASN.1 structure for RSA keys.
It specifies exactly how to encode RSA modulus, exponents, and other RSA-specific parameters.

For RSA public keys, PKCS-1 defines: `RSAPublicKey ::= SEQUENCE { modulus INTEGER, publicExponent INTEGER }`.
This is simpler than SPKI because it assumes RSA — no algorithm identifier needed.

For RSA private keys, PKCS-1 includes the modulus, both exponents, primes, and CRT coefficients.
These additional values enable faster private key operations.

PKCS-1 is RSA-only and cannot represent other key types like elliptic curves.
This limitation led to the creation of PKCS-8 for algorithm-agnostic keys.

In PEM format, PKCS-1 RSA private keys use `-----BEGIN RSA PRIVATE KEY-----`.
This differs from the generic `-----BEGIN PRIVATE KEY-----` used by PKCS-8.

Modern systems prefer PKCS-8 even for RSA keys.
PKCS-8 adds an algorithm identifier wrapper around the PKCS-1 structure.

Legacy systems and some tools still generate PKCS-1 format.
OpenSSL can convert between PKCS-1 and PKCS-8 formats.

PKCS-1 also defines RSA encryption and signature padding schemes like OAEP and PSS.
These padding methods are essential for secure RSA usage.

## Links
- [[RSA public key contains modulus and exponent integers]]
- [[PKCS-8 provides generic private key container for all algorithms]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[Cryptographic Standards MOC]]
