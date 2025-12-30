---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

The Reference element in XMLDSig identifies a specific piece of data to be signed.
Multiple Reference elements enable signing different data items in one signature.

The **URI attribute** points to the referenced data:
- `URI="#elementID"`: references an element within the same document by its ID attribute
- `URI="http://example.com/data.xml"`: references external data
- `URI=""`: references the entire document containing the signature

An empty URI typically appears in enveloped signatures.
The signature signs its containing document.

**Transforms** element lists operations applied before hashing.
Example: canonicalization, XPath filtering, or Base64 decoding.

**DigestMethod** specifies which hash algorithm to use.
Common values: SHA256, SHA512, or GOST R 34.11-2012.

**DigestValue** contains the Base64-encoded hash of the transformed data.
This is the actual integrity check value.

During verification, each Reference is processed:
1. Locate the data using the URI
2. Apply Transforms in order
3. Hash the result using DigestMethod
4. Compare to DigestValue

If any DigestValue doesn't match, the signature is invalid.
This catches modifications to any referenced data.

**Multiple References** enable selective signing.
Sign header elements separately from body elements, or sign metadata along with content.

Kazakhstan's ИС ЭСФ invoices use multiple References.
Different invoice sections each get their own Reference for granular verification.

## Links
- [[SignedInfo contains what was signed and how]]
- [[DigestValue holds hash of referenced data]]
- [[Transforms apply operations before hashing]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Digital Signatures MOC]]
