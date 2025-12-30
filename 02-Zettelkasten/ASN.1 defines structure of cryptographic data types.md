---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

ASN.1 (Abstract Syntax Notation One) is a language for describing the structure of data independent of how it's encoded.
It defines what fields exist, their types, and their order — like a schema or interface definition.

ASN.1 is used throughout cryptography to define structures like certificates, keys, and signatures.
X.509 certificates, PKCS standards, and CMS are all defined using ASN.1.

An ASN.1 definition looks like a type specification.
For example: `RSAPublicKey ::= SEQUENCE { modulus INTEGER, publicExponent INTEGER }`.

ASN.1 itself is not a file format or encoding.
It's the abstract definition that must be encoded into bytes using rules like DER or BER.

The separation of syntax (ASN.1) from encoding (DER) provides flexibility.
The same ASN.1 definition can be encoded multiple ways for different purposes.

Common ASN.1 types include INTEGER, BIT STRING, OCTET STRING, SEQUENCE, and OBJECT IDENTIFIER.
These map to cryptographic concepts like keys, signatures, and algorithm identifiers.

Tools exist to automatically generate code from ASN.1 definitions.
This ensures consistent parsing and encoding across different implementations.

ASN.1 schemas act as documentation.
Reading the ASN.1 definition shows exactly what fields a structure contains.

## Links
- [[DER provides deterministic binary encoding of ASN.1]]
- [[ASN.1 is language not file format]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[Tag-Length-Value structure enables unambiguous DER parsing]]
- [[Cryptographic Standards MOC]]
