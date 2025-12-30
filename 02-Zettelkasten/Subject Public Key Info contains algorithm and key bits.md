---
created: 2025-12-24
tags: [certificates/x509]
sr-due:
sr-interval:
sr-ease:
---

Subject Public Key Info (SPKI) is the field in an X.509 certificate containing the certificate owner's public key.
It appears in the TBSCertificate and consists of two parts: algorithm identifier and key bits.

The **algorithm identifier** specifies which cryptographic system the key belongs to.
Common identifiers include RSA encryption, ECDSA with specific curves, or GOST R 34.10-2012 for Kazakhstan.

The algorithm identifier also includes parameters needed to use the key.
For elliptic curve keys, it specifies which curve (like secp256r1 or secp384r1) the point lies on.

The **public key bits** contain the actual mathematical values of the public key.
For RSA, this includes the modulus and public exponent encoded in ASN.1.
For elliptic curves, this contains the x and y coordinates of the public key point.

The SPKI structure is also used standalone for public key storage and transmission.
PEM files with `-----BEGIN PUBLIC KEY-----` headers contain Base64-encoded SPKI structures.

The SPKI in a certificate must match the key type declared in signature algorithm fields.
An RSA SPKI cannot appear in a certificate that claims to use ECDSA signatures.

Applications extract the public key from SPKI to perform operations like signature verification or encryption.
The algorithm identifier tells the application which cryptographic library functions to use.

The hash of the SPKI appears in some certificate extensions as a key identifier.
This enables identifying the same key across different certificates.

## Links
- [[TBSCertificate contains all data that gets signed]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[RSA public key contains modulus and exponent integers]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[X.509 Certificates MOC]]
