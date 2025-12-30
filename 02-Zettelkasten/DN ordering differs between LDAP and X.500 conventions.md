---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

Distinguished Names can be represented in two different orderings depending on the standard used.
The same DN appears with RDNs in opposite order depending on the context.

**X.500 convention** orders RDNs from most specific to least specific.
Example: `CN=IVANOV IVAN,O=Example Org,C=KZ`
The most specific identifier (person name) comes first.

**LDAP convention** reverses this, ordering from least specific to most specific.
Example: `C=KZ,O=Example Org,CN=IVANOV IVAN`
The broadest identifier (country) comes first.

X.509 certificates store DNs in X.500 order internally in the ASN.1 structure.
The DER encoding contains RDNs in most-specific-first order.

LDAP directories and command-line tools often display DNs in LDAP order.
The OpenSSL command-line tool can show DNs in either format depending on flags.

This ordering difference is purely presentational.
The underlying ASN.1 structure remains the same regardless of how humans read it.

When parsing DN strings, code must handle both formats.
Some libraries provide flags to specify which convention to use for parsing and formatting.

The ordering affects string matching and comparison.
String comparison of DNs must canonicalize the order first or work with the ASN.1 structure directly.

Certificate viewer applications often allow users to choose their preferred DN display order.
This prevents confusion when comparing DNs from different sources.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[RDN is single attribute within DN sequence]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DN parsing requires libraries to handle escaping correctly]]
- [[X.509 Certificates MOC]]
