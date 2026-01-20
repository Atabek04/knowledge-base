---
created: 2025-12-24
tags: [moc]
---

Concepts for understanding X.509 certificate structure, Distinguished Names, and GOST algorithms.
Covers certificate fields, DN parsing, encoding formats, and Kazakhstan cryptographic standards.

## Certificate Structure

- [[X.509 certificate has TBSCertificate SignatureAlgorithm and SignatureValue]] — three main components
- [[TBSCertificate contains all data that gets signed]] — to-be-signed certificate content
- [[Certificate version usually indicates v3 for extensions]] — version field usage
- [[Serial number uniquely identifies certificate from CA]] — per-CA unique identifier
- [[Issuer DN identifies CA that signed certificate]] — certificate issuer
- [[Subject DN identifies certificate owner]] — certificate subject
- [[Validity period defines not-before and not-after dates]] — time constraints
- [[Subject Public Key Info contains algorithm and key bits]] — public key encoding

## Distinguished Names

### DN Structure

- [[DN is structured identifier with multiple attributes]] — hierarchical naming
- [[RDN is single attribute within DN sequence]] — relative distinguished name
- [[CN attribute contains person name or domain]] — common name field
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]] — Kazakhstan national ID

### DN Encoding & Parsing

- [[DN attributes can use PrintableString or UTF8String encoding]] — character encoding options
- [[DN ordering differs between LDAP and X.500 conventions]] — two ordering conventions
- [[Special characters in DN values must be escaped with backslash]] — escaping requirements
- [[Leading and trailing spaces in DN require escaping]] — whitespace handling
- [[Multi-valued RDN joins attributes with plus sign]] — multi-valued RDNs
- [[DN parsing requires libraries to handle escaping correctly]] — proper parsing approach

## GOST Algorithms

### Standards & Versions

- [[GOST provides Russian cryptographic independence from Western algorithms]] — Russian state standards
- [[GOST R 34.10 is signature algorithm using elliptic curves]] — GOST signature standard
- [[GOST R 34.11 is hash function called Streebog]] — GOST hash standard
- [[GOST R 34.10-2012 supports 256-bit and 512-bit key sizes]] — modern GOST version

### Kazakhstan Implementation

- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]] — Kazakhstan national standard
- [[GOST signature process hashes message then signs with private key]] — signature creation flow
- [[BouncyCastle and KalkanCrypt provide GOST algorithm implementations]] — GOST library support

## Related MOCs

- [[PKI MOC]] — certificate authorities and trust
- [[Cryptography MOC]] — cryptographic foundations
- [[Cryptographic Standards MOC]] — encoding standards
- [[Digital Signatures MOC]] — signature formats

## Practice

(Flashcards to be added)

## External Resources

- [RFC 5280 - X.509 Certificate Profile](https://datatracker.ietf.org/doc/html/rfc5280)
- [RFC 4514 - DN String Representation](https://datatracker.ietf.org/doc/html/rfc4514)
- [GOST Standards - TC 26](https://tc26.ru/en/)
- [Kazakhstan NCA Documentation](https://pki.gov.kz/)
