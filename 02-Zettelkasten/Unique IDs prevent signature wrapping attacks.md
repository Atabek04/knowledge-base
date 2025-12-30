---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Using unique IDs to reference signed elements prevents signature wrapping attacks.
The ID attribute creates an unambiguous reference that cannot be exploited through structural manipulation.

**Best practice**:
1. Add a unique ID attribute to the element being signed
2. Reference it in the signature using `URI="#elementID"`
3. Process only the element with that exact ID

Example:
```xml
<transfer id="tx-20241224-123456" from="Alice" to="Bob" amount="100">
  ...
</transfer>

<Signature>
  <SignedInfo>
    <Reference URI="#tx-20241224-123456">
      ...
    </Reference>
  </SignedInfo>
</Signature>
```

The application must:
- Verify the signature
- Extract the ID from the Reference URI
- Process only the element with that ID
- Reject if multiple elements share the same ID

**ID uniqueness** must be enforced.
XML schema validation or explicit checks ensure no duplicate IDs exist.

Using XPath like `//transfer` is vulnerable.
It matches all transfer elements, not the one that was signed.

Using `URI="#tx-123"` is precise.
It matches exactly one element, the one that was signed.

**WS-Security** specifications mandate using IDs for all signed elements.
This closed the signature wrapping vulnerability in SOAP services.

The ID must be unpredictable to prevent collision attacks.
Include timestamps, random values, or sequence numbers.

**Processing rule**: If you can't find the element with the referenced ID, reject the message.
Never fall back to searching by element name or other attributes.

## Links
- [[Signature wrapping moves valid signature to different data]]
- [[Reference element points to data being signed]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[XPath filter selects specific XML parts to sign]]
- [[Digital Signatures MOC]]
