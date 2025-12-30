---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Signature wrapping is an attack where an attacker moves a valid signature to cover different data.
It exploits differences between how XML is parsed for signature verification versus business logic processing.

**The attack**:
1. Interceptor captures a legitimately signed XML message
2. Attacker wraps the original signed element in a new parent element
3. Attacker adds their own malicious element at the expected location
4. The signature still verifies (it covers the original element)
5. But the application processes the attacker's malicious element instead

**Example scenario**:
Original: `<transfer from="Alice" to="Bob" amount="100">...</transfer>`
Wrapped:
```xml
<wrapper>
  <transfer from="Alice" to="Bob" amount="100">
    [original signed content]
  </transfer>
  <transfer from="Alice" to="Attacker" amount="1000">
    [attacker's data]
  </transfer>
</wrapper>
```

If the signature verifier finds and validates the first transfer but the business logic processes the second one, the attack succeeds.

**The vulnerability** stems from:
- Using XPath to locate signed elements
- XPath expressions that match multiple elements
- Processing logic that uses different XPath than verification logic

**SOAP web services** historically suffered from signature wrapping.
Complex message structures with multiple similar elements created opportunities.

The signature verification finds one element, confirms it's valid.
But the SOAP processor finds a different element and executes that one.

## Links
- [[Unique IDs prevent signature wrapping attacks]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Reference element points to data being signed]]
- [[XPath filter selects specific XML parts to sign]]
- [[Digital Signatures MOC]]
