---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

ASN.1 (Abstract Syntax Notation One) is a schema language that defines the structure of data types.
It specifies what fields exist, their types, and how they relate to each other.

ASN.1 describes structure abstractly, independent of how it's encoded.
The same ASN.1 schema can be encoded as binary (DER/BER), XML, or JSON.

**Example ASN.1 schema for a certificate**:
```
Certificate ::= SEQUENCE {
    tbsCertificate       TBSCertificate,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}
```

This defines that a Certificate is a sequence containing three fields.
Each field has a specific type.

**Common ASN.1 types**:
- **SEQUENCE**: ordered collection of fields (like a struct)
- **SET**: unordered collection of fields
- **INTEGER**: whole number
- **BIT STRING**: sequence of bits
- **OCTET STRING**: sequence of bytes
- **UTF8String, PrintableString**: text strings
- **OBJECT IDENTIFIER**: OID

**OPTIONAL** keyword marks fields that may be absent.
**DEFAULT** keyword specifies values for omitted fields.

Tags enable distinguishing between multiple fields of the same type.
Example: `[0] EXPLICIT` or `[1] IMPLICIT` creates context-specific tags.

ASN.1 is used throughout PKI and cryptography.
X.509 certificates, CMS signatures, PKCS standards all use ASN.1 schemas.

The schema is NOT embedded in the data.
Both sender and receiver must know the schema to encode/decode correctly.

## Links
- [[ASN.1 is language not file format]]
- [[DER provides Tag-Length-Value encoding for ASN.1]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[Cryptographic Standards MOC]]
