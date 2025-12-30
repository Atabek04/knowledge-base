---
created: 2025-12-24
tags: [pki/policy]
sr-due:
sr-interval:
sr-ease:
---

A policy OID is an Object Identifier that uniquely identifies a certificate policy within a certificate.
It tells relying parties exactly which set of rules and verification procedures were followed during issuance.

The OID appears in the Certificate Policies extension of X.509 certificates.
Multiple policy OIDs can be present if the certificate satisfies multiple policies simultaneously.

Policy OIDs follow the standard OID hierarchy.
For example, NCA Kazakhstan might use `1.2.398.3.1.2.1.1` for physical authentication and `1.2.398.3.1.2.1.2` for remote authentication.

Applications can make trust decisions based on policy OIDs.
A banking application might require certificates with specific policy OIDs indicating high-assurance verification.

The special OID `2.5.29.32.0` represents "anyPolicy" indicating acceptance of all policies.
This is a wildcard often used by intermediate CAs to avoid listing every possible policy.

Policy OIDs enable fine-grained access control.
Different services can require different policies even when all certificates come from the same CA.

Relying parties must maintain mappings of policy OIDs to their meanings.
Without documentation, OIDs are just numbers without semantic value.

Some certificates include policy qualifier information providing additional policy details.
Common qualifiers include CPS URIs pointing to the CA's Certificate Practice Statement.

## Links
- [[Certificate policy defines rules for certificate issuance]]
- [[Policy constraints limit acceptable policies in chain]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[requireExplicitPolicy forces specific policy presence]]
- [[PKI MOC]]
