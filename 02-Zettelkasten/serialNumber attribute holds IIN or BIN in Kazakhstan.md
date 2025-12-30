---
created: 2025-12-24
tags: [certificates/dn, certificates/gost]
sr-due:
sr-interval:
sr-ease:
---

The serialNumber attribute in Kazakhstan certificates contains the unique identification number of the certificate owner.
This differs from the certificate's serial number issued by the CA.

For **individual citizens**, serialNumber holds the IIN (Individual Identification Number).
The format is `IIN` followed by 12 digits: `serialNumber=IIN123456789012`.

For **legal entities**, serialNumber holds the BIN (Business Identification Number).
The format is `BIN` followed by 12 digits: `serialNumber=BIN987654321098`.

Kazakhstan's National Certification Authority (NCA) mandates this attribute for all qualified certificates.
The IIN or BIN serves as the primary unique identifier in government information systems.

The serialNumber attribute uses OID 2.5.4.5 in the X.500 naming standard.
Despite the name, it has no relationship to the certificate serial number (which uses a different field).

This attribute enables automatic identity verification in electronic government services.
Systems extract the IIN or BIN from the certificate and use it to look up citizen or organization data.

The serialNumber appears alongside CN in the subject DN.
Example: `CN=IVANOV IVAN,serialNumber=IIN123456789012,C=KZ`.

When parsing Kazakhstan certificates, both CN and serialNumber are essential.
CN provides the display name while serialNumber provides the unique system identifier.

Some international certificates use serialNumber differently.
European eIDAS certificates might use it for passport numbers or national ID numbers.

## Links
- [[DN is structured identifier with multiple attributes]]
- [[Subject DN identifies certificate owner]]
- [[CN attribute contains person name or domain]]
- [[Serial number uniquely identifies certificate from CA]]
- [[X.509 Certificates MOC]]
