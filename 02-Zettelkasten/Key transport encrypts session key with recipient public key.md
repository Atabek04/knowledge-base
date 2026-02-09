---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

### How It Works

Key transport is a method where one party generates a session key and encrypts it with the recipient's public key.
The recipient decrypts it with their private key to obtain the same session key.

The sender generates a random session key (typically an AES key).
This key is encrypted using the recipient's RSA public key.

Only the recipient can decrypt the encrypted session key using their RSA private key.
Once both parties have the session key, they switch to fast symmetric encryption.

### Limitations

This is the classical RSA key exchange approach.
It's straightforward but has a significant drawback — no forward secrecy.

If the recipient's private key is later compromised, all past sessions can be decrypted.
The attacker can decrypt all the recorded encrypted session keys.

### Modern Alternative

Modern protocols prefer **key agreement** methods like ECDHE instead.
These provide forward secrecy by using ephemeral keys that are discarded after each session.

### Current Use Cases

Key transport is still used in some contexts like encrypting email attachments or files.
The recipient's public key encrypts a file encryption key stored alongside the encrypted file.

### Security Requirement

RSA-OAEP padding must be used when encrypting session keys.
Never use raw RSA encryption — it's mathematically vulnerable.

---

## Links
- [[Session key is short-lived symmetric key for single connection]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Key agreement derives shared key without transmitting it]]
- [[RSA uses modular exponentiation with large primes for encryption]]
- [[Ephemeral ECDH provides forward secrecy by using fresh keys]]
- [[Cryptography MOC]]
