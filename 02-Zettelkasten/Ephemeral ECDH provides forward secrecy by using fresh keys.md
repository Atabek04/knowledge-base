---
created: 2025-12-24
tags: [cryptography/asymmetric]
sr-due:
sr-interval:
sr-ease:
---

Ephemeral ECDH generates a fresh private-public key pair for each session and deletes the private key immediately after use.
This provides **forward secrecy** — compromise of long-term keys doesn't reveal past session keys.

The "E" in ECDHE stands for "ephemeral" meaning temporary.
Each TLS connection uses brand new ECDH keys that exist only for that connection.

After deriving the session key, both parties securely erase their ephemeral private keys.
An attacker who later steals the server's long-term private key cannot decrypt recorded past sessions.

This contrasts with RSA key transport where the same server private key decrypts all session keys.
Compromising that key exposes all past communications.

The ephemeral keys are authenticated using long-term keys (certificates).
The server signs its ephemeral public key with its certificate's private key to prove identity.

Ephemeral keys add computational cost — generating a fresh key pair for each connection.
Modern elliptic curves like X25519 make this efficient enough for practical use.

Forward secrecy is crucial for long-term confidentiality.
Even if an attacker records encrypted traffic and breaks the encryption years later, ephemeral keys protect past sessions.

TLS 1.3 requires forward secrecy by removing non-ephemeral key exchange methods.
All connections must use ECDHE or DHE.

## Links
- [[ECDH derives shared secret using elliptic curve mathematics]]
- [[Key agreement derives shared key without transmitting it]]
- [[Session key is short-lived symmetric key for single connection]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Key transport encrypts session key with recipient public key]]
- [[Cryptography MOC]]
