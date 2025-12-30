---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS#8 is the Private-Key Information Syntax Standard providing a container for any private key type.
It wraps algorithm-specific key formats in a uniform structure.

**PKCS#8 structure**:
```
PrivateKeyInfo ::= SEQUENCE {
    version               INTEGER,
    privateKeyAlgorithm   AlgorithmIdentifier,
    privateKey            OCTET STRING,
    attributes            [0] IMPLICIT Attributes OPTIONAL
}
```

The **privateKeyAlgorithm** identifies which algorithm this key belongs to.
OIDs specify RSA, ECDSA, GOST, or other algorithms.

The **privateKey** field contains the algorithm-specific key data.
For RSA, this is PKCS#1 RSAPrivateKey encoded as DER inside the OCTET STRING.
For EC, this is ECPrivateKey structure.

This uniform wrapper enables generic key handling.
Applications can read the algorithm identifier and dispatch to appropriate handlers.

**PEM encoding**: `-----BEGIN PRIVATE KEY-----`
No algorithm name in the header — the algorithm is inside the structure.

**Encrypted PKCS#8** protects the private key with password encryption.
```
EncryptedPrivateKeyInfo ::= SEQUENCE {
    encryptionAlgorithm  AlgorithmIdentifier,
    encryptedData        OCTET STRING
}
```

The entire PrivateKeyInfo is encrypted, not just the key bytes.
PEM header: `-----BEGIN ENCRYPTED PRIVATE KEY-----`

**Password-based encryption** uses PBKDF2 or similar to derive key from password.
Common encryption algorithms include AES-128-CBC or AES-256-CBC.

PKCS#8 is the modern standard for private key storage.
New applications should use PKCS#8 rather than algorithm-specific formats.

**Kazakhstan NCALayer** uses PKCS#12 which internally uses PKCS#8.
The GOST private keys are wrapped in PKCS#8 structures.

## Links
- [[PKCS#1 specifically defines RSA key structures]]
- [[PKCS#12 bundles certificate and private key in encrypted archive]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[PEM headers identify content type between markers]]
- [[Cryptographic Standards MOC]]
