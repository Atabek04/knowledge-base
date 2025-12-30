---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

DER (Distinguished Encoding Rules) is a binary encoding format for ASN.1 data structures that ensures exactly one encoding for any given value.
The "deterministic" aspect means the same data always produces identical bytes.

DER uses a Tag-Length-Value structure for each field.
The tag identifies the type (INTEGER, SEQUENCE, etc.), the length specifies how many bytes follow, and the value contains the actual data.

For example, encoding the integer 65537 as DER: `02 03 01 00 01`.
`02` = INTEGER tag, `03` = 3 bytes long, `01 00 01` = value.

Determinism is critical for digital signatures.
The exact bytes being signed must be reproducible — different encodings would produce different signatures.

DER is a subset of BER (Basic Encoding Rules).
BER allows multiple ways to encode the same data, while DER enforces one canonical way.

Common DER file extensions include `.der`, `.cer`, and `.crt` for certificates.
Private keys might use `.key` or `.der`.

DER is compact but not human-readable.
It's pure binary data meant for machines, not people.

For human readability, DER is often wrapped in Base64 and given PEM headers.
This creates `.pem` files that can be copied through text channels.

## Links
- [[ASN.1 defines structure of cryptographic data types]]
- [[Tag-Length-Value structure enables unambiguous DER parsing]]
- [[PEM wraps Base64-encoded DER with header and footer]]
- [[BER allows multiple encodings while DER ensures single encoding]]
- [[Cryptographic Standards MOC]]
