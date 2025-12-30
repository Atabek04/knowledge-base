---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

ECDSA (Elliptic Curve Digital Signature Algorithm) creates signatures using elliptic curve cryptography.
It provides security equivalent to RSA with much smaller key sizes.

A **256-bit ECDSA key** provides security comparable to a **3072-bit RSA key**.
This dramatic size reduction makes ECDSA attractive for constrained environments and faster operations.

The algorithm operates on points on an elliptic curve rather than large integers.
Security relies on the elliptic curve discrete logarithm problem.

**Signature creation** uses the private key (a random scalar) and a random nonce.
The algorithm computes curve point operations to produce two values: r and s.

The signature is the pair (r, s), each the same size as the curve order.
For a 256-bit curve, the signature is 512 bits (64 bytes) total.

**Nonce security is critical** for ECDSA.
Reusing a nonce with the same private key allows attackers to compute the private key.
Several high-profile security breaches resulted from nonce reuse.

**Deterministic ECDSA** (RFC 6979) generates nonces from the message hash.
This eliminates nonce reuse vulnerabilities while maintaining security.

ECDSA verification uses the public key (a curve point) to check the signature.
The verifier performs curve operations to verify the mathematical relationship holds.

Popular curves include **secp256r1** (NIST P-256), **secp384r1** (NIST P-384), and **secp256k1** (Bitcoin).
Each curve has different security properties and performance characteristics.

GOST R 34.10 is similar to ECDSA but uses different curves and parameters.
Both rely on elliptic curve mathematics for security.

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Signing hashes message then encrypts hash with private key]]
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[GOST R 34.10 is signature algorithm using elliptic curves]]
- [[RSA-PSS adds randomized padding for signature security]]
- [[Digital Signatures MOC]]
