---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

Spaces at the beginning or end of Distinguished Name attribute values require special handling.
Without proper escaping or quoting, these spaces are stripped during parsing.

**Leading spaces** must be escaped with a backslash.
Example: `CN=\ John Smith` preserves the leading space.
Without escaping, `CN= John Smith` would parse as `CN=John Smith`.

**Trailing spaces** must also be escaped with a backslash.
Example: `CN=John Smith\ ` preserves the trailing space.
Without escaping, `CN=John Smith ` would be trimmed to `CN=John Smith`.

An alternative to escaping is quoting the entire value.
Example: `CN=" John Smith "` preserves both leading and trailing spaces.

Spaces in the middle of values never require escaping.
Example: `CN=John Smith` is valid without any escaping.

This escaping requirement stems from DN parsing rules that trim whitespace around separators.
After splitting on commas, parsers trim spaces from RDN strings.

Most real-world DNs do not have leading or trailing spaces.
However, parser implementations must handle them correctly for spec compliance.

Testing DN parsing requires checking these edge cases.
A proper parser should round-trip DNs with leading/trailing spaces correctly.

The DER encoding preserves all spaces including leading and trailing.
The escaping requirement only applies to the string representation of DNs.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[Special characters in DN values must be escaped with backslash]]
- [[DN parsing requires libraries to handle escaping correctly]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[X.509 Certificates MOC]]
