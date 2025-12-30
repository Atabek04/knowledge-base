---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

A Relative Distinguished Name (RDN) is a single component within a Distinguished Name sequence.
Each RDN consists of one or more attribute-value pairs.

Most RDNs are **single-valued** containing just one attribute-value pair.
Example: `CN=IVANOV IVAN` is a single RDN with the CN attribute.

RDNs can be **multi-valued** containing multiple attribute-value pairs joined with a plus sign.
Example: `CN=John Doe+UID=jdoe` represents one RDN with two attributes.

The complete DN is a sequence of RDNs separated by commas.
Example: `CN=Server,O=Example,C=US` contains three RDNs.

Each RDN is encoded as a SET of attribute-value pairs in ASN.1.
This SET can contain one or multiple attribute-value pairs.

The "relative" in RDN means it's relative to the parent in the naming hierarchy.
In LDAP directory trees, each RDN defines one level of the hierarchy.

RDN values may contain special characters that require escaping.
Commas, plus signs, quotes, backslashes, and other characters need backslash escaping.

Parsing DNs requires breaking the string into RDNs, then extracting attributes from each RDN.
Libraries like BouncyCastle or standard X.500 parsers handle this correctly.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[Multi-valued RDN joins attributes with plus sign]]
- [[Special characters in DN values must be escaped with backslash]]
- [[DN parsing requires libraries to handle escaping correctly]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[X.509 Certificates MOC]]
