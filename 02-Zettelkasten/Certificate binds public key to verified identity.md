---
created: 2025-12-24
tags: [pki/fundamentals]
sr-due:
sr-interval:
sr-ease:
---

A digital certificate is a data structure that cryptographically links a public key to a verified identity.
It's the fundamental output of the PKI system — proof that a specific public key belongs to a specific entity.

The certificate contains the subject's identity information (name, organization, domain, etc.) and their public key.
These fields are signed by the Certificate Authority's private key, creating unforgeable proof of the binding.

Think of it as a digitally signed ID card.
The ID card shows your photo and name (identity + public key), and the government's seal proves it's genuine (CA signature).

Anyone with the CA's public key can verify the certificate signature.
This proves the CA vouched for the identity-to-key binding, not that someone just made up a certificate.

Certificates have expiration dates limiting their validity period.
This forces periodic identity re-verification and limits damage if a private key is compromised.

The binding is only as trustworthy as the CA's verification process.
If the CA issues certificates without proper identity verification, the entire system breaks down.

X.509 is the standard certificate format used in TLS, email security, code signing, and most PKI applications.

## Links
- [[PKI solves trust problem by introducing trusted third party]]
- [[CA verifies identity before issuing certificates]]
- [[X.509 certificate has TBSCertificate SignatureAlgorithm and SignatureValue]]
- [[Certificate expiration automatically invalidates after validity period]]
- [[PKI MOC]]
