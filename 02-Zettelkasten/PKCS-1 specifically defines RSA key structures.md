---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS-1 is the RSA Cryptography Standard defining structures specific to RSA keys.
It provides formats for RSA public keys, RSA private keys, and RSA signatures.

**RSA Public Key structure** (PKCS-1):
```
RSAPublicKey ::= SEQUENCE {
    modulus           INTEGER,
    publicExponent    INTEGER
}
```

This contains just the two RSA public key components.
No algorithm identifier is included — the structure itself implies RSA.

**RSA Private Key structure** (PKCS-1):
```
RSAPrivateKey ::= SEQUENCE {
    version           INTEGER,
    modulus           INTEGER,
    publicExponent    INTEGER,
    privateExponent   INTEGER,
    prime1            INTEGER,
    prime2            INTEGER,
    exponent1         INTEGER,
    exponent2         INTEGER,
    coefficient       INTEGER
}
```

It includes all components needed for efficient RSA operations.
The CRT (Chinese Remainder Theorem) parameters enable faster computations.

**PEM encoding** distinguishes PKCS-1:
- `-----BEGIN RSA PRIVATE KEY-----` for PKCS-1 private key
- `-----BEGIN RSA PUBLIC KEY-----` for PKCS-1 public key

PKCS-1 v2.1 introduced RSA-PSS and RSA-OAEP.
These are modern RSA schemes with better security properties.

**PKCS-1 vs PKCS-8**:
PKCS-1 is RSA-only; PKCS-8 works with any algorithm.
Modern applications prefer PKCS-8 for flexibility.

**Signature schemes** are also defined in PKCS-1.
RSA-PSS (Probabilistic Signature Scheme) is the recommended method.

The standard specifies padding schemes for encryption and signatures.
Proper padding prevents mathematical attacks on RSA.

## Links
- [[PKCS-8 provides generic private key container for all algorithms]]
- [[RSA public key contains modulus and exponent integers]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[RSA-PSS adds randomized padding for signature security]]
- [[PEM headers identify content type between markers]]
- [[Cryptographic Standards MOC]]
