---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

A Relative Distinguished Name can contain multiple attribute-value pairs joined with a plus sign.
This creates a multi-valued RDN representing a single component of the DN hierarchy.

Example: `CN=John Doe+UID=jdoe` is one RDN with two attributes.
Both attributes together identify the entity at that level of the naming hierarchy.

Multi-valued RDNs are less common than single-valued RDNs in practice.
Most certificates use separate RDNs for each attribute: `CN=John Doe,UID=jdoe`.

The ASN.1 encoding represents RDNs as a SET of attribute-value pairs.
Multi-valued RDNs have multiple elements in that SET.

The plus sign in DN string notation represents the SET nature.
Attributes joined with `+` are members of the same SET (same RDN).

Attributes in a multi-valued RDN are unordered in the ASN.1 structure.
However, string representations must choose a deterministic order for consistency.

Multi-valued RDNs are sometimes used for combining CN with a unique identifier.
Example: `CN=Administrator+UID=admin001` bundles display name with system ID.

Parsing multi-valued RDNs requires splitting on `+` within each RDN after splitting on `,`.
The order of operations is: split on commas (RDNs), then split each RDN on plus signs (attributes).

A literal plus sign in an attribute value must be escaped.
Example: `O=A\+B Company` is a single-valued RDN with a literal plus in the value.

## Links
- [[RDN is single attribute within DN sequence]]
- [[DN is structured identifier with multiple attributes]]
- [[Special characters in DN values must be escaped with backslash]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DN parsing requires libraries to handle escaping correctly]]
- [[X.509 Certificates MOC]]
