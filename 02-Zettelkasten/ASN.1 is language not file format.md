---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

ASN.1 is a schema definition language, not a file format or encoding.
It describes the structure of data abstractly, separate from how the data is represented.

Think of ASN.1 like a programming language's type system.
It defines what a Certificate or PublicKey structure looks like.

**ASN.1 defines the "what"**:
- A Certificate has three fields
- The first field is a TBSCertificate
- An INTEGER is a whole number

**Encoding rules define the "how"**:
- DER: Binary encoding with specific rules
- BER: Binary encoding with flexibility
- XER: XML encoding
- JER: JSON encoding

The same ASN.1 schema can be encoded multiple ways.
Different applications might use different encodings for the same data structure.

**This separation is powerful**:
- Schema changes don't affect encoding choice
- New encodings can support existing schemas
- Tools can convert between encodings automatically

Cryptographic standards specify both ASN.1 schemas AND encoding rules.
X.509 certificates use ASN.1 schemas with DER encoding.

Developers rarely write ASN.1 schemas manually.
They use libraries that implement standard schemas (X.509, PKCS, CMS).

**ASN.1 modules** organize related type definitions.
Standards like X.509 are published as ASN.1 modules.

Understanding the distinction helps avoid confusion.
When someone says "this is ASN.1," they mean "this follows an ASN.1 schema" not "this is how the bytes are formatted."

## Links
- [[ASN.1 schema defines field types and structure]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[BER allows multiple encodings while DER ensures single encoding]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[Cryptographic Standards MOC]]
