---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

The Enveloped Signature Transform is used when the signature is inside the document being signed.
It removes the `<Signature>` element before hashing to avoid a circular reference.

**The circular reference problem**:
If the signature signs the entire document including itself, the DigestValue changes every time.
Computing the signature requires the DigestValue, but the DigestValue depends on the signature.

**Solution**: Remove the signature element before hashing.
The hash is computed over the document without the signature.
Then the signature is added to the document.

The transform is identified by URI: `http://www.w3.org/2000/09/xmldsig#enveloped-signature`.

**Transform processing**:
1. Start with the document containing the signature
2. Locate the `<Signature>` element
3. Remove it from the tree
4. Pass the modified document to the next transform or hash function

This enables the signature to be embedded directly in the signed document.
The document and signature travel together as a single XML file.

**Verification** applies the same transform.
The verifier removes the signature element and hashes what remains.

**Multiple signatures** in one document each use the enveloped transform.
Each signature's hash excludes that signature but may include other signatures.

The transform only removes the signature element that contains it.
Other signature elements in the document remain.

**Use case**: Configuration files, electronic forms, and documents where signature and content must stay together.

The alternative is a detached signature in a separate file.
Enveloped signatures are more convenient when a single-file format is required.

## Links
- [[Transforms apply operations before hashing]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Reference element points to data being signed]]
- [[Canonicalization normalizes XML before signing]]
- [[DigestValue holds hash of referenced data]]
- [[Digital Signatures MOC]]
