---
created: 2025-12-24
tags: [pki/policy]
sr-due:
sr-interval:
sr-ease:
---

Policy mapping is a mechanism where a CA declares that one policy OID is equivalent to another for the purposes of that CA's operations.
This enables cross-CA trust where different CAs use different policy OIDs for equivalent verification procedures.

The Policy Mappings extension contains pairs of OIDs: issuer domain policy and subject domain policy.
The CA says "my policy A is equivalent to their policy B for certificates I issue."

This solves the problem of federated PKI with multiple independent CAs.
Different organizations may have different policy OIDs even though their verification procedures are equivalent.

For example, two CAs might both perform rigorous identity verification but use different OIDs.
Policy mapping allows one CA to recognize the other's policy as equivalent to its own.

The inhibitPolicyMapping constraint can prevent mapping, requiring exact policy matches.
This stops CAs from declaring equivalences that might not truly exist.

Policy mapping appears in intermediate CA certificates.
It affects how policies are interpreted for all certificates downstream from that intermediate.

Relying parties can choose to ignore policy mappings and require exact policy OID matches.
This provides stricter control when cross-CA equivalences are not trusted.

Complex enterprise PKIs often use policy mapping to unify multiple internal CAs.
Departments with separate CAs can map their policies to corporate-wide equivalents.

## Links
- [[Policy constraints limit acceptable policies in chain]]
- [[Policy OID identifies specific verification requirements]]
- [[Certificate policy defines rules for certificate issuance]]
- [[requireExplicitPolicy forces specific policy presence]]
- [[PKI MOC]]
