---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

Parsing Distinguished Name strings correctly requires handling numerous edge cases and escaping rules.
Manual string parsing of DNs is error-prone and should be avoided.

**Complexity factors**:
- Special characters requiring backslash escaping
- Leading and trailing space preservation
- Multi-valued RDNs joined with plus signs
- Different ordering conventions (X.500 vs LDAP)
- Multiple string encodings (PrintableString vs UTF8String)
- Quoted values as alternative to escaping
- Hexadecimal encoding indicated by leading `#`

**Java standard library** provides `javax.naming.ldap.LdapName` for LDAP-order parsing.
For X.500 order, use `javax.security.auth.x500.X500Principal`.

**BouncyCastle** library provides `org.bouncycastle.asn1.x500.X500Name` for robust DN handling.
It correctly handles escaping, encoding, and ordering for both parsing and formatting.

**OpenSSL** command-line tool can parse and display DNs with various formatting options.
Use `-nameopt` flags to control display format: `RFC2253`, `oneline`, `multiline`, etc.

Libraries work directly with the ASN.1 DER encoding when possible.
This avoids string parsing entirely by reading the structured binary format.

String parsing is only needed when DNs are input by users or read from text configuration.
For certificate validation and chain building, libraries work with DER structures.

Naive string splitting on commas fails for DNs with escaped commas.
Example: `CN=Smith\, John,O=Company` would incorrectly split into three parts.

Incorrect parsing can cause security issues.
A DN with escaped separators might parse differently in different systems, breaking access control.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[RDN is single attribute within DN sequence]]
- [[Special characters in DN values must be escaped with backslash]]
- [[Leading and trailing spaces in DN require escaping]]
- [[Multi-valued RDN joins attributes with plus sign]]
- [[DN ordering differs between LDAP and X.500 conventions]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[X.509 Certificates MOC]]
