---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

Basic Encoding Rules (BER) is the original ASN.1 encoding with flexibility that allows multiple representations.
Distinguished Encoding Rules (DER) is a restricted subset of BER that ensures exactly one encoding per value.

**BER flexibility** creates problems for digital signatures.
Different encodings of the same data produce different hash values, invalidating signatures.

**Example**: BER allows both short and long length forms.
Length 5 can be encoded as:
- Short form: `0x05`
- Long form: `0x81 0x05` (length takes 1 byte, value is 5)

Both are valid BER but produce different bytes.

**Boolean in BER** can be any non-zero value for TRUE.
`01 01 FF` and `01 01 01` both mean TRUE.

**DER restrictions** eliminate these choices:
- Always use short length form when possible
- Boolean TRUE is always `0xFF`
- SET elements ordered by tag value
- BIT STRING unused bits always zero
- No constructed encoding for primitive strings

The result: any ASN.1 value has exactly one valid DER encoding.
Two implementations encoding the same value produce identical bytes.

**Signatures require DER** for this determinism.
Certificates, CMS structures, and other signed data use DER.

**Verification** sometimes accepts BER but re-encodes to DER internally.
Some parsers strictly require DER to avoid ambiguity attacks.

**CER (Canonical Encoding Rules)** is another variant.
It's for streaming large data structures where length isn't known in advance.

Most cryptographic applications use DER exclusively.
BER appears mainly in legacy systems or streaming protocols.

## Links
- [[DER provides deterministic binary encoding of ASN.1]]
- [[DER provides Tag-Length-Value encoding for ASN.1]]
- [[ASN.1 schema defines field types and structure]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Cryptographic Standards MOC]]
