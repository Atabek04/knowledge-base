---
created: 2025-12-24
tags: [cryptography/asymmetric, standards/keys]
sr-due:
sr-interval:
sr-ease:
---

### Components

An RSA public key consists of two integers: the **modulus (n)** and the **public exponent (e)**.
These are the only mathematical values needed for RSA encryption and signature verification.

### Modulus

The modulus n is the product of two large secret prime numbers (p and q).
Typical sizes are 2048 bits or 4096 bits for modern RSA keys.

### Public Exponent

The public exponent e is usually 65537 (0x010001 in hex).
This value provides good security while enabling fast encryption operations.

### Raw Representation

The raw representation is just these two numbers stored as big integers.
For a 2048-bit RSA key, n is about 617 decimal digits long.

### Sufficiency

These values alone are sufficient for encrypting or verifying signatures.
To decrypt or create signatures, the private exponent d is also needed (kept secret).

### Practical Storage

In practice, RSA public keys are never stored as raw integers.
They're wrapped in structures like SPKI (Subject Public Key Info) that include algorithm identifiers.

### Security Foundation

The security of RSA relies on the difficulty of factoring n back into its prime factors.
If someone factors n to find p and q, they can compute the private exponent d.

---

## Links
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[Raw key consists of mathematical values without metadata]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[PKCS-1 defines RSA key format with modulus and exponent]]
- [[Cryptographic Standards MOC]]
