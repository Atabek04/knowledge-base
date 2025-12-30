---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

Authenticity is the property that confirms the identity of the message sender.
It answers the question: "Did this specific person or entity actually create this signature?"

Digital signatures provide authenticity through asymmetric cryptography.
Only the holder of the private key can create a signature that verifies with the corresponding public key.

The private key acts as a secret credential proving the signer's identity.
If a signature verifies successfully, the verifier knows it was created by the private key holder.

**Certificate binding** links the public key to a verified identity.
A certificate from a trusted CA states "this public key belongs to this person or organization."

Without certificate binding, public keys are just numbers.
The certificate provides the trust link between a cryptographic key and a real-world identity.

Authenticity depends on proper private key protection.
If an attacker steals the private key, they can impersonate the legitimate signer.

**Hardware Security Modules (HSMs)** and smart cards protect private keys from theft.
These devices perform signing operations without exposing the private key to software.

Authenticity differs from integrity.
Authenticity proves WHO signed, while integrity proves the data WASN'T modified.

A signature can have authenticity but fail integrity if someone modified the signed data.
Conversely, data integrity can be verified without knowing the signer's identity.

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Integrity detects any modification to signed data]]
- [[Non-repudiation prevents signer from denying signature]]
- [[Certificate binds public key to verified identity]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Digital Signatures MOC]]
