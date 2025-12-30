---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

The certificate issuance process starts when the requester generates a public-private key pair locally.
This is critical — the private key must never be transmitted to the CA or anyone else.

Key generation happens on your device, server, or HSM.
Standard tools include openssl, ssh-keygen, or specialized cryptographic libraries.

The private key remains under your exclusive control throughout the process.
If the CA generated your key pair, they would have access to your private key, breaking the security model.

For RSA, you generate the large primes and compute the modulus and exponents.
For elliptic curves, you generate a random scalar and compute the public point.

The key strength depends on the parameters chosen.
Modern standards require RSA-2048 minimum (preferably RSA-4096) or EC P-256 minimum.

Some systems use hardware-generated keys in smart cards or HSMs.
The key never exists outside the secure hardware — even you can't extract it.

After generation, you protect the private key with strong file permissions and optionally encryption.
Store it in a secure location with backups in case of hardware failure.

The public key from this pair will be included in the CSR sent to the CA.
The CA will bind this public key to your verified identity in the issued certificate.

## Links
- [[CSR contains public key and identity information]]
- [[CA signs certificate with private key to prove authenticity]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[PKCS#12 bundles certificate and private key in encrypted archive]]
- [[PKI MOC]]
