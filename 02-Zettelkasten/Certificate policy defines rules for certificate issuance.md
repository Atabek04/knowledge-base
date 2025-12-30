---
created: 2025-12-24
tags: [pki/policy]
sr-due:
sr-interval:
sr-ease:
---

A certificate policy is a documented set of rules that defines how a CA issues and manages certificates.
It specifies identity verification procedures, key management requirements, audit procedures, and liability limitations.

Each policy is identified by a unique OID (Object Identifier).
This OID appears in the certificate's Certificate Policies extension, indicating which rules were followed.

Different policies represent different assurance levels.
A policy for domain validation has different requirements than a policy for extended validation.

The Certificate Practice Statement (CPS) details how the CA implements its policies.
The policy says "what must be done," the CPS says "how we do it."

Relying parties can check certificate policies to determine trust levels.
A certificate issued under a strict verification policy deserves more trust than one with minimal verification.

Kazakhstan's NCA has different policy OIDs for different certificate types.
Policies distinguish between physical authentication at service centers versus remote authentication.

Policies can specify allowed key sizes, algorithms, and validity periods.
Some policies require HSM storage for private keys or mandate specific cryptographic algorithms.

CAs publish their Certificate Policy documents publicly.
These lengthy technical documents define all operational and security requirements.

Changes to certificate policies require careful management.
Policy updates may affect thousands of existing certificates and relying party systems.

## Links
- [[Policy OID identifies specific verification requirements]]
- [[Policy constraints limit acceptable policies in chain]]
- [[CA verifies identity before issuing certificates]]
- [[OID uniquely identifies cryptographic algorithms and policies]]
- [[PKI MOC]]
