---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Canonicalization (C14N) transforms XML into a standard form before signing or hashing.
It ensures consistent byte representation regardless of semantically irrelevant differences.

**Problems without canonicalization**:
- `<element/>` vs `<element></element>` are equivalent but have different bytes
- Attribute order: `<tag a="1" b="2"/>` vs `<tag b="2" a="1"/>` differ in bytes but not meaning
- Whitespace variations: spaces, tabs, newlines between elements
- Namespace declarations at different levels

Canonicalization produces a single normalized representation.
The same logical XML always produces identical bytes after canonicalization.

**Two main canonicalization algorithms**:
- **C14N (Canonical XML)**: includes all namespace declarations
- **Exclusive C14N**: includes only actively used namespaces

The CanonicalizationMethod in SignedInfo specifies which algorithm to use.
Both the signer and verifier must use the same method.

**C14N processing**:
1. Normalize line breaks to LF (\n)
2. Remove XML declaration and DTD
3. Order attributes alphabetically by namespace URI then local name
4. Replace empty elements `<tag/>` with `<tag></tag>`
5. Normalize whitespace in attribute values
6. Add namespace declarations as needed

The result is a consistent UTF-8 byte sequence.
This sequence gets hashed or signed.

**Whitespace handling** is critical.
Significant whitespace is preserved; insignificant whitespace between elements is normalized.

Canonicalization applies to both the signed data and the SignedInfo element itself.
SignedInfo gets canonicalized before computing the signature over it.

## Links
- [[XMLDSig signs XML documents with embedded signatures]]
- [[C14N removes whitespace and orders attributes consistently]]
- [[Exclusive C14N includes only used namespaces]]
- [[SignedInfo contains what was signed and how]]
- [[Transforms apply operations before hashing]]
- [[Digital Signatures MOC]]
