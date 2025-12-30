---
created: 2025-12-24
tags: [pki/ca]
sr-due:
sr-interval:
sr-ease:
---

A Hardware Security Module (HSM) is a physical device designed to generate, store, and use cryptographic keys without ever exposing them.
The private key never leaves the HSM — all cryptographic operations happen inside the tamper-resistant hardware.

HSMs differ fundamentally from storing keys in software files.
Software-stored keys can be copied, stolen by malware, or extracted from memory dumps.

The HSM contains secure cryptographic processors and memory protected by physical security measures.
Tamper detection circuits destroy keys if someone attempts to open the device or probe its internals.

Operations work by sending data into the HSM, which performs signing or decryption internally, and returns only the result.
You can use the key but never extract it — even with physical access to the HSM.

HSMs require authentication for every operation.
Multiple administrators might need to authorize critical operations like key generation or backup.

Root CA private keys are always stored in HSMs kept in vaults with multiple layers of physical security.
The room is access-controlled, the HSM is in a locked cage, and multiple people must be present for use.

HSMs are certified to standards like FIPS 140-2 Level 3 or Level 4.
These certifications require extensive security testing and documentation.

Modern cloud HSMs allow using secure hardware without owning physical devices.
Cloud providers operate HSMs in their data centers, providing API access to cryptographic operations.

## Links
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[Compromised root CA requires global trust store updates]]
- [[PKI MOC]]
