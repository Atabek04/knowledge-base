---
created: 2025-12-24
tags: [moc]
---

Concepts for understanding Public Key Infrastructure, certificate authorities, and trust systems.
Covers PKI fundamentals, CA hierarchy, trust chains, certificate lifecycle, and revocation mechanisms.

## PKI Fundamentals

- [[PKI solves trust problem by introducing trusted third party]] — addressing public key ownership verification
- [[Certificate binds public key to verified identity]] — authenticated key-to-identity mapping
- [[CA verifies identity before issuing certificates]] — trusted verification authority
- [[Trust chain transfers trust from pre-installed root to end certificate]] — hierarchical trust model

## Certificate Authorities

### CA Types & Hierarchy

- [[Root CA is ultimate trust anchor with self-signed certificate]] — top-level trust authority
- [[Intermediate CA performs daily certificate signing operations]] — operational CA layer
- [[RA verifies identity at public-facing offices]] — registration authority role

### Security Infrastructure

- [[HSM protects private keys with tamper-resistant hardware]] — hardware security module

## Trust Chain & Verification

- [[Transitive trust flows from root through intermediates to end certificate]] — trust propagation
- [[Root certificate is pre-installed in operating system trust store]] — trust anchor distribution
- [[Certificate chain includes end certificate plus all intermediates]] — complete chain of trust
- [[Trust store contains database of trusted root certificates]] — trusted root repository
- [[Browser builds chain from server certificate to trusted root]] — chain validation process
- [[Compromised root CA requires global trust store updates]] — root compromise impact
- [[Intermediate CA compromise only requires revoking that intermediate]] — isolated compromise recovery

## Certificate Lifecycle

### Issuance Process

- [[Certificate issuance begins with key pair generation]] — first step in certificate request
- [[CSR contains public key and identity information]] — certificate signing request
- [[CA verification confirms identity through various methods]] — identity proofing process
- [[DV certificates verify domain ownership via DNS or email]] — domain validation
- [[OV certificates verify organization through business registration]] — organization validation
- [[CA signs certificate with private key to prove authenticity]] — cryptographic binding

### Expiration & Renewal

- [[Certificate expiration automatically invalidates after validity period]] — time-based invalidation
- [[Certificate renewal reuses existing key pair with new dates]] — simple renewal process
- [[Certificate re-issuance generates fresh key pair for security]] — re-keying for enhanced security

### Revocation

- [[Revocation forcefully invalidates certificate before expiration]] — early termination

## Revocation Systems

- [[CRL lists serial numbers of revoked certificates]] — certificate revocation list
- [[OCSP provides real-time certificate status check]] — online certificate status protocol
- [[CRL download can be slow due to large file size]] — CRL scalability issue
- [[OCSP stapling attaches status response to TLS handshake]] — performance optimization
- [[Certificate lifecycle has issuance active and end-of-life stages]] — three lifecycle phases

## Certificate Policies

- [[Certificate policy defines rules for certificate issuance]] — policy framework
- [[Policy OID identifies specific verification requirements]] — policy identification
- [[Policy constraints limit acceptable policies in chain]] — policy validation rules
- [[requireExplicitPolicy forces specific policy presence]] — explicit policy requirement
- [[Policy mapping allows CA to equate different policy OIDs]] — cross-CA policy equivalence

## Related MOCs

- [[Cryptography MOC]] — cryptographic fundamentals
- [[X.509 Certificates MOC]] — certificate structure and format
- [[Digital Signatures MOC]] — signature mechanisms
- [[Cryptographic Standards MOC]] — encoding and standards

## Practice

(Flashcards to be added)

## External Resources

- [PKI Basics - Mozilla](https://wiki.mozilla.org/CA)
- [RFC 5280 - X.509 Certificate and CRL Profile](https://datatracker.ietf.org/doc/html/rfc5280)
- [CA/Browser Forum Baseline Requirements](https://cabforum.org/baseline-requirements-documents/)
- [NIST PKI Publications](https://csrc.nist.gov/projects/pki)
