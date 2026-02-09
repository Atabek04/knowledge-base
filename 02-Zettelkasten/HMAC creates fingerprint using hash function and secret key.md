---
created: 2025-12-24
tags: [cryptography/hash]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

HMAC (Keyed-Hash Message Authentication Code) combines a cryptographic hash function with a secret key to create an authentication tag.
It can use any hash function — HMAC-SHA256, HMAC-SHA512, HMAC-SHA3, etc.

### Construction

The construction involves hashing the message twice with the key mixed in a specific way.
This two-hash pattern prevents length extension attacks that could forge tags.

The basic pattern is: `HMAC(K, M) = H((K ⊕ opad) || H((K ⊕ ipad) || M))`.
`K` is the key, `M` is the message, `H` is the hash function, and `opad`/`ipad` are constants.

### Security

HMAC's security depends on the underlying hash function.
If SHA-256 is secure, then HMAC-SHA256 is secure for authentication.

The output size equals the hash function's output size.
HMAC-SHA256 produces 256 bits (32 bytes), HMAC-SHA512 produces 512 bits (64 bytes).

### Standardization and Usage

HMAC is standardized in RFC 2104 and is used everywhere in cryptographic protocols.
TLS, SSH, IPsec, JWT, and countless others rely on HMAC.

### Key Management

The key should be at least as long as the hash output size for full security.
Shorter keys don't provide the full strength of the hash function.

Never use the same key for HMAC and encryption.
Derive separate keys for different purposes using a KDF.

---

## Links
- [[MAC provides integrity and authenticity using keyed hash]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[KDF turns shared point into uniform cryptographic keys]]
- [[Authentication tag detects tampering in GCM mode]]
- [[Cryptography MOC]]
