---
created: 2025-12-24
tags: [pki/ca]
sr-due:
sr-interval:
sr-ease:
---

A Certificate Authority (CA) is the trusted entity responsible for verifying identities before binding them to public keys in certificates.
The CA acts as the trust anchor — its verification process determines how much trust should be placed in a certificate.

Verification methods vary by certificate type and assurance level.
Domain Validation (DV) certificates only verify domain control via DNS or email.
Organization Validation (OV) certificates verify business registration through government databases.
Extended Validation (EV) certificates require the most rigorous verification including legal documentation.

For individual certificates in Kazakhstan, verification requires physical presence at a service center.
You present your national ID, an officer verifies it in person, and only then issues the certificate with your IIN embedded.

The CA doesn't create your key pair — you generate it locally and send only the public key in a CSR.
The CA verifies your identity separately from the cryptographic key generation process.

After successful verification, the CA signs the certificate with its private key.
This signature is the cryptographic proof that the CA performed verification and approved the binding.

The security of the entire PKI system depends on CA diligence.
If a CA issues certificates without proper verification, attackers can obtain valid certificates for identities they don't own.

## Links
- [[Certificate binds public key to verified identity]]
- [[CSR contains public key and identity information]]
- [[DV certificates verify domain ownership via DNS or email]]
- [[OV certificates verify organization through business registration]]
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[PKI MOC]]
