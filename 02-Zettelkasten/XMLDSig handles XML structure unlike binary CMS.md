---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

XMLDSig differs from CMS by working with XML's hierarchical structure rather than binary data.
This creates both advantages and unique challenges.

**CMS** treats data as opaque bytes.
It hashes and signs the exact byte sequence without understanding content structure.

**XMLDSig** understands XML element hierarchy.
It can sign specific elements, attributes, or combinations within a document.

XML's flexibility creates signature challenges:
- Whitespace (spaces, tabs, newlines) can vary without changing meaning
- Attribute order is semantically irrelevant but affects byte representation
- Namespace declarations can appear at different levels
- Character encoding affects byte representation

**Canonicalization** solves these problems by normalizing XML.
It produces a consistent byte representation regardless of superficial differences.

XMLDSig can sign parts of a document while leaving others unsigned.
Example: Sign the transaction data but leave the routing information unsigned.

**Transforms** enable complex signing scenarios.
An XPath filter can select specific elements; a Base64 transform can decode embedded data.

CMS signatures are simpler and more reliable for arbitrary binary data.
XMLDSig is essential when working with XML-based protocols and systems.

**SOAP web services** require XMLDSig for message-level security.
HTTP-level signatures (like CMS) don't work for messages passing through intermediaries.

Kazakhstan's ИС ЭСФ (Electronic Invoicing System) chose XMLDSig because invoices are XML.
The signature can be validated by XML-aware systems throughout the processing chain.

## Links
- [[XMLDSig signs XML documents with embedded signatures]]
- [[CMS wraps data with signature and signer certificate]]
- [[Canonicalization normalizes XML before signing]]
- [[Transforms apply operations before hashing]]
- [[SignedInfo contains what was signed and how]]
- [[Digital Signatures MOC]]
