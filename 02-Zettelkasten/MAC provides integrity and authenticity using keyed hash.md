---
created: 2025-12-24
tags: [cryptography/hash]
sr-due:
sr-interval:
sr-ease:
---

### Purpose

A MAC (Message Authentication Code) is a short fixed-size value that proves both message integrity and authenticity.
It's computed using a hash function combined with a secret key.

### Key Property

The key property is that only someone with the secret key can generate valid MACs.
This proves the message came from someone who knows the key (authenticity) and wasn't altered (integrity).

### Difference from Hashing

MACs differ from regular hashes by requiring a key.
A hash like SHA-256 can be computed by anyone — it only provides integrity, not authenticity.

### Common Construction

The most common MAC construction is HMAC (Hash-based MAC).
HMAC can use any hash function: HMAC-SHA256, HMAC-SHA512, etc.

Computing the MAC involves hashing the message mixed with the key in a specific pattern.
The exact pattern prevents certain cryptographic attacks.

### Verification

Verifying a MAC requires recomputing it with the same key and comparing results.
If the MACs match, the message is authentic and unmodified.

### Use Cases

MACs are used extensively in network protocols.
TLS, IPsec, SSH, and others use MACs to protect message integrity and authenticity.

### Modern Approach

Modern practice prefers **authenticated encryption** modes like GCM that integrate MAC functionality.
This avoids the complexity and potential bugs of manually combining encryption and MAC operations.

The encrypt-then-MAC pattern is considered most secure when using separate primitives.
Encrypt first, then compute MAC over the ciphertext.

---

## Links
- [[HMAC creates fingerprint using hash function and secret key]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Authentication tag detects tampering in GCM mode]]
- [[GCM mode combines encryption with authentication tag]]
- [[Integrity detects any modification to signed data]]
- [[1. Cryptography MOC]]
