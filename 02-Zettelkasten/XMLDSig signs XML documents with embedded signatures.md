---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

XML Digital Signature (XMLDSig) is a W3C standard for signing XML documents.
It provides a way to embed signatures directly within XML or reference external data.

Unlike CMS which uses binary ASN.1 encoding, XMLDSig uses XML syntax.
The signature itself is represented as XML elements within the document structure.

**Three signature types** are supported:
- **Enveloped**: signature inside the signed document
- **Enveloping**: signed document inside the signature
- **Detached**: signature and document are separate

The standard defines XML elements for all signature components.
`<Signature>`, `<SignedInfo>`, `<SignatureValue>`, and `<KeyInfo>` are the main elements.

XMLDSig handles XML-specific challenges like whitespace and namespace handling.
Canonicalization ensures consistent representation before hashing.

**Web services** and **SOAP** commonly use XMLDSig for message signing.
APIs can sign individual XML elements or entire documents.

**Kazakhstan's Electronic Invoicing System (ИС ЭСФ)** requires XMLDSig.
Invoices are XML documents signed using GOST algorithms in XMLDSig format.

XMLDSig can reference multiple data items in one signature.
Different elements can be signed together, each with its own hash.

The flexibility of XMLDSig comes with complexity.
Numerous options for transforms, canonicalization, and references create implementation challenges.

## Links
- [[XMLDSig handles XML structure unlike binary CMS]]
- [[SignedInfo contains what was signed and how]]
- [[SignatureValue contains actual signature bytes]]
- [[Canonicalization normalizes XML before signing]]
- [[Enveloped signature transform removes signature element]]
- [[Digital Signatures MOC]]
