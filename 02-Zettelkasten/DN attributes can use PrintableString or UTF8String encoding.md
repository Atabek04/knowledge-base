---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

Distinguished Name attributes can be encoded using different ASN.1 string types.
The choice of string type affects which characters can appear in DN values.

**PrintableString** supports only a limited ASCII subset: letters, digits, space, and a few punctuation marks.
Allowed punctuation: `' ( ) + , - . / : = ?`
This encoding cannot represent Cyrillic, Arabic, Chinese, or other non-Latin scripts.

**UTF8String** supports the full Unicode character set.
This enables DNs with Cyrillic names, Arabic text, or Chinese characters.

Older PKI systems and standards defaulted to PrintableString for compatibility.
Modern systems increasingly use UTF8String to support international names.

Kazakhstan certificates use UTF8String for DN attributes containing Cyrillic names.
A DN like `CN=ИВАНОВ ИВАН` requires UTF8String encoding.

Some government systems in Kazakhstan transliterate Cyrillic to Latin for PrintableString compatibility.
`ИВАНОВ` becomes `IVANOV` in the certificate DN.

**BMPString** and **UniversalString** are alternative Unicode encodings rarely used in practice.
UTF8String has become the standard for international character support.

Libraries must correctly decode the string type to display DN values.
Treating UTF8String as PrintableString produces garbled output for non-ASCII characters.

The string type is specified in the ASN.1 tag for each attribute value.
DER encoding includes this type information so parsers know how to decode the bytes.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[X.509 Certificates MOC]]
