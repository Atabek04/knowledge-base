---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

Distinguished Encoding Rules (DER) encode ASN.1 structures using a Tag-Length-Value format.
Each piece of data is prefixed with its type (tag) and size (length).

**Tag** identifies the data type:
- `0x02`: INTEGER
- `0x04`: OCTET STRING
- `0x06`: OBJECT IDENTIFIER
- `0x30`: SEQUENCE
- `0x31`: SET

**Length** specifies how many bytes of value follow.
For lengths under 128, it's a single byte.
For longer data, the length is encoded in multiple bytes.

**Value** contains the actual data bytes.
The encoding of the value depends on the tag type.

**Example**: INTEGER with value 500
- Tag: `0x02` (INTEGER)
- Length: `0x02` (2 bytes)
- Value: `0x01 0xF4` (500 in hexadecimal)
- Complete: `02 02 01 F4`

**SEQUENCE encoding** is recursive:
- Tag: `0x30`
- Length: total bytes of all contained TLV structures
- Value: concatenated TLV encodings of each sequence element

DER is **deterministic**: exactly one valid encoding exists for any value.
This is critical for signatures — hashing must produce identical results.

**Boolean encoding**:
- `01 01 FF` for TRUE
- `01 01 00` for FALSE

**String encoding** depends on string type:
- UTF8String: direct UTF-8 bytes
- PrintableString: ASCII subset
- Tag identifies which string type

The TLV structure enables parsing without knowing the schema in advance.
Readers can skip unknown fields by reading the tag and length.

## Links
- [[Tag-Length-Value structure enables unambiguous DER parsing]]
- [[ASN.1 schema defines field types and structure]]
- [[BER allows multiple encodings while DER ensures single encoding]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[PEM Base64-encodes DER for text-safe transport]]
- [[Cryptographic Standards MOC]]
