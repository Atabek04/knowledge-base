---
created: 2025-12-24
tags: [cryptography/hash]
sr-due:
sr-interval:
sr-ease:
---

> Hashing transforms input data of any size into a **fixed-length** output called a <mark style="background: #BBFABBA6;">digest</mark> or <mark style="background: #BBFABBA6;">fingerprint</mark>.
>
> The transformation is one-way — you cannot recover the original input from the hash.

### Hash Algorithms

Common hash algorithms produce different output sizes.
- **SHA-256** always generates 256 bits (32 bytes) regardless of input size.
- **SHA-512** produces 512 bits (64 bytes) for extra security margin.
- **GOST R 34.11-2012** offers 256-bit and 512-bit variants.
- **MD5** generates 128 bits but is cryptographically broken.

### Security Properties

> **Larger hash size provides exponentially stronger security.**

#### Collision Resistance

**Collision resistance** measures how hard it is to find two inputs with the same hash.
Attack difficulty is 2^(n/2) where n is the bit length.
SHA-256 requires ~2^128 operations to find a collision.
SHA-512 requires ~2^256 operations — vastly more secure.

#### Preimage Resistance

**Preimage resistance** measures how hard it is to find an input matching a specific hash.
Attack difficulty is 2^n operations.
SHA-256 needs 2^256 attempts.
SHA-512 needs 2^512 attempts — exponentially harder.

#### MD5 Weakness

MD5 is broken because its 128-bit size allows collision attacks with ~2^64 operations.
Modern computing power makes this feasible.
Never use MD5 for security purposes.

#### Performance Trade-off

> **Performance trade-off:** Larger hashes are slower to compute.

SHA-512 takes more CPU cycles than SHA-256.
For most applications, SHA-256 provides sufficient security with better performance.
Use SHA-512 for long-term security (decades) or highly sensitive data.

### Use Cases

- **integrity verification**
	- When you download a file, comparing its hash with the published hash confirms the file wasn't corrupted or tampered with.
	- Example: 
		- Linux ISOs publish SHA-256 hashes; you run `sha256sum ubuntu.iso` to verify.
		- GitHub releases include checksums in release notes.
- **password storage**
	- The one-way property makes hashes ideal for storing passwords.
	- Systems store the hash instead of the password itself.
	- During login, the entered password is hashed and compared with the stored hash.

### Properties

Even a single bit change in input produces a completely different hash output.
This property is called the **avalanche effect**.

## Links
- [[Birthday problem explains why collision resistance requires double the security bits]]
- [[Checksum verifies integrity but signature on checksum verifies authenticity]]
- [[Encryption transforms data using key to ensure confidentiality]]
- [[Encoding converts data format without providing secrecy]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[MAC provides integrity and authenticity using keyed hash]]
- [[1. Cryptography MOC]]
