---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

After verifying identity, the CA creates a certificate structure containing the requester's public key and identity information.
The CA then signs this structure with its private key, creating cryptographic proof that the CA vouches for the binding.

The signing process computes a hash of the TBSCertificate (To Be Signed Certificate) content.
This hash is then encrypted with the CA's private key using the signature algorithm (RSA-SHA256, ECDSA-P256, GOST, etc.).

The signature proves three things: the CA created this certificate, the content hasn't been tampered with, and the CA verified the identity.
Anyone with the CA's public key can verify the signature and trust the certificate.

The signature is what makes the certificate cryptographically secure.
Without the CA's signature, anyone could create a certificate claiming any identity.

Different signature algorithms provide different security levels.
Modern CAs use SHA-256 or SHA-384 with RSA-2048+ or ECDSA-P256+.

The CA's signing key is typically an intermediate CA certificate, not the root.
This protects the root key which stays offline in an HSM.

The signature is appended to the certificate along with the algorithm identifier.
The complete structure is: TBSCertificate + SignatureAlgorithm + SignatureValue.

Clients verify the signature during certificate validation.
They hash the TBSCertificate, decrypt the signature value with the CA's public key, and compare the hashes.

## Links
- [[CA verification confirms identity through various methods]]
- [[Certificate binds public key to verified identity]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[X.509 certificate has TBSCertificate SignatureAlgorithm and SignatureValue]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[PKI MOC]]
