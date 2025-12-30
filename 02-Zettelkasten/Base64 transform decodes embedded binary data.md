---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

The Base64 Transform decodes Base64-encoded data embedded in XML elements.
It enables signing the actual binary data rather than its text encoding.

**Use case**: An XML document contains Base64-encoded image, PDF, or other binary data.
The signature should cover the actual binary content, not the Base64 text.

Without this transform, changing the Base64 encoding (adding whitespace or changing line breaks) would invalidate the signature.
The Base64 transform makes the signature cover the decoded bytes.

The transform is identified by URI: `http://www.w3.org/2000/09/xmldsig#base64`.

**Processing**:
1. Extract text content from the referenced element
2. Remove all whitespace (spaces, tabs, newlines)
3. Base64-decode the text to binary
4. Output the binary data

The output is a byte sequence passed to the next transform or hash function.

**Example**:
```xml
<Reference URI="#document-data">
  <Transforms>
    <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#base64"/>
  </Transforms>
  <DigestMethod Algorithm="...sha256"/>
  <DigestValue>...</DigestValue>
</Reference>

<Data Id="document-data">
  JVBERi0xLjQKJeLjz9MKMSAwIG9iago8P...
</Data>
```

The signature covers the decoded PDF bytes, not the Base64 text.

**Verification** applies the same decode.
The verifier decodes the Base64 and hashes the binary result.

This transform is often combined with canonicalization.
The Base64 transform produces binary; a subsequent transform might process it further.

**Whitespace handling** is critical.
The transform must ignore all whitespace to handle different Base64 formatting styles.

## Links
- [[Transforms apply operations before hashing]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[Reference element points to data being signed]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[DigestValue holds hash of referenced data]]
- [[Digital Signatures MOC]]
