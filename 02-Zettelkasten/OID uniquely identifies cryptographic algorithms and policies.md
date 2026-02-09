---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

### Definition

An OID (Object Identifier) is a globally unique identifier represented as a sequence of integers separated by dots.
Each cryptographic algorithm, hash function, certificate policy, and extension has its own OID.

### Hierarchical Structure

OIDs form a hierarchical namespace managed by standards bodies.
For example, RSA encryption is `1.2.840.113549.1.1.1`, SHA-256 is `2.16.840.1.101.3.4.2.1`.

The hierarchy prevents conflicts — different organizations control different branches.
`1.2.840` is controlled by ISO, who delegated `113549` to RSA Security.

### Common Uses

OIDs appear throughout cryptographic structures.
Algorithm identifiers in certificates, signature algorithms, certificate policies, and extensions all use OIDs.

### Extensibility

They enable extensibility without format changes.
New algorithms get new OIDs; parsers that don't recognize an OID can skip it gracefully.

### Encoding

OIDs are encoded in DER as a compact binary format.
The dotted notation is for human readability; in DER they're compressed sequences of bytes.

### Delegation

No central registration is required for sub-delegated OIDs.
If you control an OID branch, you can create unlimited child OIDs.

### Regional Standards

Kazakhstan cryptographic standards have their own OID subtree.
GOST algorithms and NCA policies use OIDs under the Russian/Kazakhstan allocation.

### Human-Readable Mapping

Tools and libraries maintain OID databases mapping numbers to algorithm names.
This allows displaying "SHA-256" instead of "2.16.840.1.101.3.4.2.1".

---

## Links
- [[ASN.1 defines structure of cryptographic data types]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[Certificate policy defines rules for certificate issuance]]
- [[Policy OID identifies specific verification requirements]]
- [[Cryptographic Standards MOC]]
