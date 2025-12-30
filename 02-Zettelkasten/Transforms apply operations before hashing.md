---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Transforms in XMLDSig are operations applied to referenced data before computing the hash.
They enable signing data in various forms and selecting specific portions of documents.

The Transforms element contains an ordered list of Transform elements.
Each Transform is applied in sequence; the output of one becomes the input of the next.

**Common transforms**:
- **Canonicalization**: normalizes XML to consistent byte representation
- **Enveloped Signature**: removes the signature element from the document being signed
- **XPath Filtering**: selects specific XML elements or attributes
- **Base64 Decode**: decodes Base64-encoded binary data
- **XSLT**: applies XSLT transformation to reshape XML

**Transform pipeline example**:
1. Start with the referenced data
2. Apply Enveloped Signature transform (remove `<Signature>`)
3. Apply XPath filter (select specific elements)
4. Apply Canonicalization (normalize to bytes)
5. Hash the result

Each Transform is identified by a URI:
- `http://www.w3.org/2000/09/xmldsig#enveloped-signature` for enveloped signature
- `http://www.w3.org/2001/10/xml-exc-c14n#` for Exclusive C14N
- `http://www.w3.org/2000/09/xmldsig#base64` for Base64 decode

**The final transform** must produce a byte sequence.
Canonicalization transforms convert XML to bytes for hashing.

Verification applies the same Transforms in the same order.
If any Transform differs, the hash won't match.

**Security consideration**: Complex Transform chains increase attack surface.
XPath injection and XSLT attacks can manipulate the signed data.

Best practice limits Transforms to well-known, simple operations.
Avoid dynamic XPath expressions from untrusted sources.

## Links
- [[Reference element points to data being signed]]
- [[Canonicalization normalizes XML before signing]]
- [[Enveloped signature transform removes signature element]]
- [[XPath filter selects specific XML parts to sign]]
- [[Base64 transform decodes embedded binary data]]
- [[DigestValue holds hash of referenced data]]
- [[Digital Signatures MOC]]
