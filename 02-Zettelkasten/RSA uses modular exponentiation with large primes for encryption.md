---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

### Mathematical Foundation

RSA (Rivest-Shamir-Adleman) is an asymmetric algorithm based on the computational difficulty of factoring large composite numbers.
Security relies on the fact that multiplying two large primes is easy, but finding those primes from their product is extremely hard.

### Key Components

The public key consists of two numbers: **modulus (n)** and **public exponent (e)**, typically 65537.
The private key contains the **private exponent (d)** which is computed from the prime factors of n.

### Operations

Encryption works by raising the message to power e modulo n: `Ciphertext = Message^e mod n`.
Decryption raises the ciphertext to power d modulo n: `Message = Ciphertext^d mod n`.

### Key Sizes

Typical RSA key sizes are 2048 or 4096 bits for the modulus.
Longer keys are more secure but slower to operate on.

### Dual Purpose

RSA can be used for both encryption and digital signatures.
For signatures, the roles reverse — sign with the private key, verify with the public key.

### Padding Requirements

Modern RSA always uses padding schemes like OAEP for encryption or PSS for signatures.
Without padding, RSA has mathematical weaknesses that make it insecure.

### Modern Trend

RSA is being gradually replaced by elliptic curve cryptography in many applications.
ECC provides equivalent security with much smaller keys and faster operations.

---

## Links
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Asymmetric cryptography uses public-private key pairs]]
- [[RSA-PSS adds randomized padding for signature security]]
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Key transport encrypts session key with recipient public key]]
- [[Cryptography MOC]]
