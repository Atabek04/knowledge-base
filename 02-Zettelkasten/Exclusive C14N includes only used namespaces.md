---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Exclusive Canonicalization (Exclusive C14N) is a variant that includes only actively used namespaces.
It solves problems that occur when signed XML is embedded in other documents.

**Standard C14N** includes all namespace declarations in scope.
This causes problems when moving signed XML to a different context.

**Example problem**:
A SOAP message signs an element with C14N.
When the message is forwarded, the intermediary wraps it in additional SOAP elements.
The new wrapper adds namespace declarations that change the in-scope namespaces.
Standard C14N would now produce different bytes, invalidating the signature.

**Exclusive C14N** only includes namespaces that are:
- Used by the element itself
- Used by attributes on the element
- Used by descendant elements or attributes

Namespaces declared in ancestors but not used are excluded.
This makes the canonical form independent of the surrounding context.

The signed fragment becomes context-independent.
It can be moved to different documents without affecting its canonical form.

**Namespace prefixes** are handled specially:
Exclusive C14N preserves the actual prefixes used.
Standard C14N can change prefixes while maintaining namespace URIs.

**Web services** and **SOAP** prefer Exclusive C14N.
Messages pass through multiple intermediaries that add/remove wrapper elements.

The algorithm is specified as "http://www.w3.org/2001/10/xml-exc-c14n#" in XMLDSig.
Standard C14N is "http://www.w3.org/TR/2001/REC-xml-c14n-20010315".

Applications must specify which canonicalization to use.
Mixing standard and exclusive C14N between signing and verification causes failures.

## Links
- [[Canonicalization normalizes XML before signing]]
- [[C14N removes whitespace and orders attributes consistently]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[SignedInfo contains what was signed and how]]
- [[Transforms apply operations before hashing]]
- [[Digital Signatures MOC]]
