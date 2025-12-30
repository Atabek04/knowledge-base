---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

The Common Name (CN) attribute is the most recognizable component of a Distinguished Name.
Its purpose and content vary depending on the certificate type.

For **individual certificates**, CN contains the person's full name.
Example: `CN=IVANOV IVAN IVANOVICH` for a Kazakhstan citizen's certificate.

For **TLS/SSL certificates**, CN traditionally contained the domain name.
Example: `CN=www.example.com` for a website certificate.

For **organization certificates**, CN might contain the legal entity name.
Example: `CN=Example LLP` for a company certificate.

Modern TLS certificates rely on Subject Alternative Names (SAN) extension rather than CN.
The CA/Browser Forum deprecated using CN for domain validation in favor of explicit SAN entries.

Browsers check the SAN extension first and may ignore CN entirely for domain validation.
However, CN remains important for display purposes and backward compatibility.

In Kazakhstan digital signatures, CN always includes the full name in uppercase.
The format follows national ID cards: surname followed by given names.

The CN value may contain spaces and special characters requiring proper escaping.
Names with commas, apostrophes, or quotes need backslash escaping in DN strings.

Certificate selection interfaces typically display the CN prominently.
Users recognize certificates by the name shown in CN when choosing which key to use.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[Subject DN identifies certificate owner]]
- [[Special characters in DN values must be escaped with backslash]]
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]]
- [[X.509 Certificates MOC]]
