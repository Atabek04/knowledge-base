---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Canonical XML (C14N) is the standard algorithm for normalizing XML documents.
It produces deterministic output by applying consistent formatting rules.

**Attribute ordering** is alphabetized:
First by namespace URI (alphabetically), then by local name (alphabetically).
This ensures `<tag b="2" a="1"/>` always becomes `<tag a="1" b="2"/>`.

**Whitespace normalization**:
- Insignificant whitespace between elements is removed
- Significant whitespace in text content is preserved
- Whitespace in attribute values is normalized (multiple spaces become single space)

**Empty elements** are expanded:
`<element/>` becomes `<element></element>`.
This eliminates byte-level differences between equivalent representations.

**Line endings** are normalized to LF (\n):
CRLF (\r\n) from Windows becomes LF.
This handles cross-platform compatibility.

**Namespace declarations** are included even if redundant:
C14N includes all namespace declarations that are in scope.
This ensures the canonicalized fragment is self-contained.

**Special characters** in text and attributes are escaped:
- `<` becomes `&lt;`
- `>` becomes `&gt;` (in text only)
- `&` becomes `&amp;`
- `"` becomes `&quot;` (in attribute values)

The algorithm is fully specified in the W3C Canonical XML specification.
Implementations must follow every rule precisely to produce identical output.

**Character encoding** output is always UTF-8.
Even if the input uses a different encoding, canonical form is UTF-8.

Testing canonicalization requires comparing byte-for-byte output.
Two implementations must produce absolutely identical bytes for the same input.

## Links
- [[Canonicalization normalizes XML before signing]]
- [[Exclusive C14N includes only used namespaces]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Transforms apply operations before hashing]]
- [[Digital Signatures MOC]]
