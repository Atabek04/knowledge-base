---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

XPath Filter Transforms select specific parts of an XML document for signing.
They enable signing selected elements or attributes while leaving others unsigned.

**XPath** is a query language for navigating XML documents.
An XPath expression selects nodes (elements, attributes, text) matching certain criteria.

Example XPath: `//invoice:items/invoice:item[@id='001']`
This selects the item element with id attribute equal to '001'.

The XPath Filter Transform evaluates the expression against the document.
Only the selected nodes are passed to subsequent transforms or hashing.

**Use cases**:
- Sign transaction data but not routing information
- Sign business content but not display formatting
- Sign specific elements in a complex document
- Implement partial document signatures

**Two XPath filter variants exist**:
- **XPath Filter**: includes nodes matching the expression
- **XPath Filter 2.0**: supports intersection, union, and subtraction of node sets

**Security risk**: XPath injection.
If XPath expressions are built from untrusted input, attackers can manipulate selection.

**Safe practice**: Use fixed XPath patterns only.
Never concatenate user input into XPath expressions.

Example:
```xml
<Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
  <XPath>
    //invoice:items
  </XPath>
</Transform>
```

The transform output is a node set.
A subsequent canonicalization transform converts it to bytes for hashing.

**Kazakhstan ИС ЭСФ** uses XPath to sign specific invoice sections.
Different parts of the invoice can have different signature requirements.

Complex XPath expressions can significantly impact performance.
Simple, targeted expressions are preferred.

## Links
- [[Transforms apply operations before hashing]]
- [[XPath injection manipulates queries from unsanitized input]]
- [[Reference element points to data being signed]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Canonicalization normalizes XML before signing]]
- [[Digital Signatures MOC]]
