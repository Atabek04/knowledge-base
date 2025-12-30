---
created: 2025-12-24
tags: [moc]
---

Concepts for understanding cryptographic algorithms, key management, and data protection.
Covers fundamental cryptographic operations, symmetric and asymmetric encryption, hash functions, and key formats.

## Core Concepts

- [[Hashing produces fixed-length fingerprint that cannot be reversed]] — one-way transformation for integrity
- [[Encryption transforms data using key to ensure confidentiality]] — reversible transformation with secret key
- [[Encoding converts data format without providing secrecy]] — format conversion for safe transport
- [[Symmetric cryptography uses single key for encryption and decryption]] — shared secret approach
- [[Asymmetric cryptography uses public-private key pairs]] — two-key cryptographic system

## Symmetric Cryptography

### Algorithms & Ciphers

- [[AES is most widely used symmetric encryption algorithm]] — modern standard for symmetric encryption
- [[Block cipher processes fixed-size data chunks]] — fixed-size block encryption

### Modes of Operation

- [[Mode of operation defines how block cipher processes long messages]] — systematic approach for block chaining
- [[CBC mode chains blocks by XORing with previous ciphertext]] — sequential block chaining
- [[CTR mode converts block cipher into stream cipher using counter]] — parallelizable counter-based mode
- [[GCM mode combines encryption with authentication tag]] — authenticated encryption mode

### Supporting Concepts

- [[IV ensures identical plaintext produces different ciphertext]] — randomization for security
- [[XOR operation reversibly mixes two equal-length byte strings]] — fundamental bitwise operation
- [[Keystream is generated from counter values in CTR mode]] — pseudo-random sequence generation
- [[Authentication tag detects tampering in GCM mode]] — integrity verification
- [[MAC provides integrity and authenticity using keyed hash]] — message authentication code
- [[HMAC creates fingerprint using hash function and secret key]] — keyed-hash message authentication

## Asymmetric Cryptography

### Key Pair Systems

- [[Public key encrypts while private key decrypts in asymmetric systems]] — dual-key mechanism
- [[RSA uses modular exponentiation with large primes for encryption]] — factorization-based cryptography
- [[ECDH derives shared secret using elliptic curve mathematics]] — key agreement protocol

### Key Exchange

- [[Session key is short-lived symmetric key for single connection]] — temporary encryption key
- [[Key transport encrypts session key with recipient public key]] — RSA-style key exchange
- [[Key agreement derives shared key without transmitting it]] — Diffie-Hellman approach
- [[KDF turns shared point into uniform cryptographic keys]] — key derivation function
- [[Ephemeral ECDH provides forward secrecy by using fresh keys]] — temporary key pairs

## Key Formats & Standards

### Binary Representations

- [[Raw key consists of mathematical values without metadata]] — bare mathematical representation
- [[RSA public key contains modulus and exponent integers]] — RSA key components
- [[EC public key contains x y coordinates on elliptic curve]] — elliptic curve point
- [[Byte is eight-bit unit as smallest addressable memory storage]] — fundamental data unit
- [[Hexadecimal represents byte using two digits for four bits each]] — hex notation

### Encoding Standards

- [[ASN.1 defines structure of cryptographic data types]] — abstract syntax notation
- [[DER provides deterministic binary encoding of ASN.1]] — unambiguous binary format
- [[PEM wraps Base64-encoded DER with header and footer]] — text-safe encoding
- [[Base64 converts binary to printable ASCII for text channels]] — binary-to-text encoding
- [[Tag-Length-Value structure enables unambiguous DER parsing]] — TLV encoding
- [[OID uniquely identifies cryptographic algorithms and policies]] — object identifiers

### Key Container Formats

- [[SPKI structure holds algorithm identifier and public key bits]] — subject public key info

## Related MOCs

- [[PKI MOC]] — certificate authorities and trust systems
- [[Digital Signatures MOC]] — signature algorithms and formats
- [[Cryptographic Standards MOC]] — encoding standards and file formats
- [[X.509 Certificates MOC]] — certificate structure and parsing

## Practice

(Flashcards to be added)

## External Resources

- [Cryptography I - Stanford Online](https://www.coursera.org/learn/crypto)
- [Practical Cryptography for Developers](https://cryptobook.nakov.com/)
- [NIST Cryptographic Standards](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
- [The Cryptopals Crypto Challenges](https://cryptopals.com/)
