---
created: 2025-12-24
tags: [cryptography/symmetric]
sr-due:
sr-interval:
sr-ease:
---

A session key is a temporary symmetric encryption key used for one communication session or file encryption.
It's generated fresh for each use and discarded afterward.

Typical session keys are AES keys — 128, 192, or 256 bits.
They provide fast symmetric encryption for bulk data.

The key advantage is limiting damage from key compromise.
If a session key leaks, only that one session's data is exposed, not all past or future communications.

Session keys solve the performance problem of asymmetric cryptography.
Use asymmetric encryption only to exchange the session key, then use the fast session key for actual data.

In TLS (HTTPS), a fresh session key is negotiated for every connection.
The asymmetric handshake exchanges a session key, which then encrypts all HTTP traffic.

Session keys should be cryptographically random.
Never derive them from predictable sources like timestamps or sequential counters.

After use, session keys should be securely erased from memory.
Leaving them accessible can enable attacks that recover encrypted data.

Some protocols support session key rotation during long connections.
Periodically generating new session keys limits exposure even if one key is compromised.

## Links
- [[Symmetric cryptography uses single key for encryption and decryption]]
- [[Key transport encrypts session key with recipient public key]]
- [[Key agreement derives shared key without transmitting it]]
- [[Ephemeral ECDH provides forward secrecy by using fresh keys]]
- [[AES is most widely used symmetric encryption algorithm]]
- [[Cryptography MOC]]
