---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

A CSR (Certificate Signing Request) is a data structure containing the public key and identity information that you send to a CA.
It's essentially an application for a certificate — you're asking the CA to bind your public key to your claimed identity.

The CSR includes several fields: Subject DN (your identity), public key, and cryptographic algorithm.
For a web server, the CN field contains the domain name; for a person, it contains their name.

The entire CSR is signed with your private key.
This proves you possess the private key corresponding to the public key in the CSR.

Standard CSR formats use PKCS-10 encoded in DER or PEM.
You'll see `-----BEGIN CERTIFICATE REQUEST-----` in PEM format.

The CA verifies the CSR signature before proceeding with identity verification.
If the signature is invalid, you don't control the claimed public key.

The CSR never contains the private key — only the public key.
Sending the private key would completely defeat the purpose of asymmetric cryptography.

After the CA verifies your identity, they sign the CSR content to create a certificate.
The CA adds validity periods, serial numbers, and extensions, then signs the whole structure.

You can generate a CSR using tools like openssl or automated certificate management systems.
Many web hosting panels and cloud services automate CSR generation.

## Links
- [[Certificate issuance begins with key pair generation]]
- [[CA verification confirms identity through various methods]]
- [[CA signs certificate with private key to prove authenticity]]
- [[PKCS-10 standard defines CSR format]]
- [[PKI MOC]]
