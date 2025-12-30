---
created: 2025-12-24
tags: [certificates/dn]
sr-due:
sr-interval:
sr-ease:
---

A Distinguished Name (DN) is a structured identifier consisting of multiple attributes that uniquely identify an entity.
DNs appear in X.509 certificates as both issuer DN and subject DN.

Each DN is a sequence of Relative Distinguished Names (RDNs).
Each RDN contains one or more attribute-value pairs.

Common attributes include:
- **CN** (Common Name): person name or domain name
- **O** (Organization): company or organization name
- **OU** (Organizational Unit): department or division
- **C** (Country): two-letter country code
- **L** (Locality): city name
- **ST** (State/Province): state or province name
- **serialNumber**: identification number (IIN/BIN in Kazakhstan)

Example DN: `CN=IVANOV IVAN,serialNumber=IIN123456789012,O=Example Org,C=KZ`
This DN has four RDNs, each with a single attribute.

DN ordering differs between standards.
**X.500** standard orders from most specific to least specific (CN first).
**LDAP** standard reverses this, going from least specific to most specific (C first).

DNs use standardized OIDs to identify attribute types.
CN is actually OID 2.5.4.3, while C is OID 2.5.4.6.

The structured nature enables hierarchical naming and unique identification.
No two entities in the same namespace should have identical DNs.

## Links
- [[RDN is single attribute within DN sequence]]
- [[CN attribute contains person name or domain]]
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]]
- [[Issuer DN identifies CA that signed certificate]]
- [[Subject DN identifies certificate owner]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[X.509 Certificates MOC]]
