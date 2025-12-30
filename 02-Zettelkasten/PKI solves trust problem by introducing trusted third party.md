---
created: 2025-12-24
tags: [pki/fundamentals]
sr-due:
sr-interval:
sr-ease:
---

Public Key Infrastructure (PKI) addresses the fundamental question: how do you know a public key actually belongs to who it claims to?
Without PKI, anyone could generate a key pair and falsely claim to be Alice, Bob, or your bank.

The core problem is the **trust gap** in asymmetric cryptography.
Public keys are meant to be public, but there's no inherent proof of ownership in the key itself.

PKI solves this by introducing a **trusted third party** called a Certificate Authority (CA).
The CA acts like a digital notary — it verifies identities and vouches for key ownership.

When the CA verifies your identity, it creates a **digital certificate** binding your identity to your public key.
This certificate is signed with the CA's private key, creating cryptographic proof.

Anyone who trusts the CA can verify the certificate signature and trust the binding.
This transfers trust from the pre-trusted CA to the newly verified certificate.

Without PKI, every party would need out-of-band verification of every public key.
This doesn't scale — imagine manually verifying keys for every website you visit.

The analogy is a passport system: governments (CAs) verify identity and issue passports (certificates).
Others trust the passport because they trust the issuing government.

## Links
- [[Certificate binds public key to verified identity]]
- [[CA verifies identity before issuing certificates]]
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[Asymmetric cryptography uses public-private key pairs]]
- [[PKI MOC]]
