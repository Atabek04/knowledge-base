---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

Distinguished Name values may contain characters that have special meaning in DN syntax.
These characters must be escaped with a backslash to appear as literal values.

**Characters requiring escaping**:
- Comma (`,`) - separates RDNs
- Plus (`+`) - separates attributes in multi-valued RDNs
- Quotes (`"`) - used for quoting values
- Backslash (`\`) - escape character itself
- Less than (`<`) and greater than (`>`) - legacy bracket syntax
- Semicolon (`;`) - alternative RDN separator in some syntaxes

Example: A name containing a comma requires escaping.
Unescaped: `CN=Smith, John` would parse as two RDNs.
Escaped: `CN=Smith\, John` correctly represents a single name.

Example: A value with a plus sign.
Unescaped: `O=A+B Company` would parse as multi-valued RDN.
Escaped: `O=A\+B Company` correctly represents the literal organization name.

Leading and trailing spaces also require special handling.
They must be escaped or the value must be quoted to preserve them.

The backslash itself must be escaped as a double backslash.
Example: `OU=IT\\Security` represents the literal string `IT\Security`.

**Hash characters** (`#`) at the beginning of values have special meaning.
Leading `#` indicates hexadecimal encoding of the value.

Incorrect escaping causes parsing errors or silent data corruption.
A DN string without proper escaping might parse successfully but with wrong values.

Libraries like BouncyCastle and Java's X500Principal handle escaping automatically.
Application code should use these libraries rather than attempting manual string parsing.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[RDN is single attribute within DN sequence]]
- [[Leading and trailing spaces in DN require escaping]]
- [[Multi-valued RDN joins attributes with plus sign]]
- [[DN parsing requires libraries to handle escaping correctly]]
- [[X.509 Certificates MOC]]
