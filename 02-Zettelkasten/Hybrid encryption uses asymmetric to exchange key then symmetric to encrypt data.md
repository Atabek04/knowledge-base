---
created: 2026-04-27
tags: [cryptography/symmetric, cryptography/asymmetric]
aliases: [hybrid encryption]
sr-due:
sr-interval:
sr-ease:
---

Asymmetric encryption is secure but slow — impractical for large data.
Symmetric encryption is fast but has a key distribution problem — how to share the secret key safely?

Hybrid encryption solves both by combining them:

1. Generate a random **session key** (symmetric)
2. Encrypt the session key with recipient's **public key** (asymmetric) — solves key distribution
3. Encrypt the actual data with the **session key** (symmetric) — solves performance

Recipient decrypts the session key with their private key, then decrypts the data.

---

### Used everywhere

- **TLS** — asymmetric handshake establishes session key, symmetric encrypts the traffic
- **ЭЦП / CMS** — session key encrypts document, asymmetric protects the session key
- **PGP / S/MIME** — same pattern for email encryption

---

### Read more

- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Asymmetric cryptography uses public-private key pairs]]
- [[Session key is short-lived symmetric key for single connection]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
