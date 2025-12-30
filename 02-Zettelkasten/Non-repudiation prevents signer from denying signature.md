---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

Non-repudiation is the property that prevents a signer from denying they created a signature.
It provides legal accountability by making signatures unforgeable and undeniable.

The private key is known only to the signer.
If proper key protection is maintained, only that person could have created the signature.

This property makes digital signatures legally binding in court.
The signer cannot claim "someone else must have signed it" if they protected their private key.

Non-repudiation requires proper **private key custody**.
Keys stored on shared computers or accessible to multiple people weaken non-repudiation.

**Hardware tokens** and **smart cards** strengthen non-repudiation.
These devices require physical possession and often a PIN, making key theft more difficult.

**Certificate policies** often mandate hardware key storage for qualified signatures.
Kazakhstan requires hardware tokens for ЭЦП to ensure non-repudiation.

Non-repudiation depends on timestamp evidence.
Without timestamps, signers might claim their key was compromised before they actually signed.

**Trusted timestamps** from a Time Stamping Authority (TSA) prove when the signature was created.
The timestamp is itself digitally signed, providing undeniable temporal evidence.

Non-repudiation differs from authenticity.
Authenticity proves the signature matches the key; non-repudiation proves the keyholder cannot deny signing.

**Message Authentication Codes (MACs)** provide authenticity but not non-repudiation.
Since both parties know the symmetric key, either could have created the MAC.

Legal systems vary in how they recognize digital signature non-repudiation.
Many countries have laws specifically addressing digital signature validity and legal force.

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Authenticity confirms identity of message sender]]
- [[Integrity detects any modification to signed data]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[Certificate policy defines rules for certificate issuance]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Digital Signatures MOC]]
