---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

Tag-Length-Value (TLV) is the fundamental encoding pattern used in DER where each data element has three parts.
The tag identifies the type, the length specifies the size, and the value contains the actual data.

The tag byte indicates the ASN.1 type: `02` for INTEGER, `03` for BIT STRING, `30` for SEQUENCE, etc.
This tells the parser how to interpret the following value bytes.

The length field specifies how many bytes the value occupies.
For lengths under 128, one byte suffices. Longer values use multi-byte length encoding.

The value contains the actual data bytes for that element.
Its interpretation depends on the tag — integers, strings, sequences, etc.

TLV structure is self-describing — parsers can navigate without prior knowledge.
Each element announces its type and length, so the parser knows where it ends.

This enables robust parsing of complex nested structures.
A SEQUENCE contains TLV elements, which themselves may contain more TLV elements.

Without TLV, parsers would need external information about field sizes and types.
Fixed-length fields waste space, and variable-length fields without length markers are ambiguous.

DER's deterministic rules ensure consistent TLV encoding.
The same ASN.1 data always produces identical TLV byte sequences.

TLV appears in many other formats beyond DER.
EMV payment cards, TLS records, and binary protocols use similar TLV structures.

## Links
- [[DER provides deterministic binary encoding of ASN.1]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[Raw values lack type and length information]]
- [[Cryptographic Standards MOC]]
