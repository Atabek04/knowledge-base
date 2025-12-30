---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

CMS SignedData can contain multiple SignerInfo structures for the same content.
This enables multiple parties to digitally sign a single document.

Each SignerInfo is independent and uses its own key and certificate.
Multiple signers can use different signature algorithms and hash functions.

**Use cases for multiple signatures**:
- Contracts requiring approval from multiple parties
- Documents needing signatures from different organizational roles
- Multi-party agreements like real estate transactions
- Workflow approval chains

Each signer adds their SignerInfo to the signerInfos collection.
The order of SignerInfos doesn't imply signing sequence without timestamps.

**Countersignatures** are a special case of multiple signatures.
A countersignature signs another signature rather than the original content.

Verification checks each SignerInfo independently.
A document is considered fully signed when all required signatures verify successfully.

Different signers can use different key types.
One might use RSA, another ECDSA, and a third GOST depending on their certificates.

The certificates collection includes certificates for all signers.
This enables verification of all signatures without external certificate lookup.

**Parallel signing** means all signers sign the same content.
The document doesn't change between signatures.

**Sequential signing** in workflows requires each signer to sign the previous state.
CMS itself doesn't enforce sequence; applications must manage this through timestamps or countersignatures.

Kazakhstan documents sometimes require dual signatures.
Both the individual and an organization representative might sign the same document.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[SignerInfo identifies signer and holds signature value]]
- [[CMS structure includes content signature algorithm and certificates]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[Digital Signatures MOC]]
