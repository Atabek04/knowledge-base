---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

ИС ЭСФ (Информационная Система Электронных Счетов-Фактур) is Kazakhstan's Electronic Invoicing System.
It requires XMLDSig signatures using GOST algorithms for all invoice documents.

**Invoice structure**:
- XML document following national schema
- Multiple signature elements for different parties
- Supplier signs first
- Buyer signs to confirm receipt
- Tax authority validates signatures

**XMLDSig with GOST**:
The signature uses XML Digital Signature format but with Kazakhstan-specific algorithms:
- Hash algorithm: GOST R 34.11-2012 (Streebog-512)
- Signature algorithm: GOST R 34.10-2015 (512-bit)
- Canonicalization: Exclusive C14N

**Signature process**:
1. Supplier creates invoice XML
2. NCALayer signs using enveloped XMLDSig
3. XML with embedded signature sent to ИС ЭСФ
4. System validates signature and certificate
5. Invoice registered in national database

**Multiple signatures** on one invoice:
- Initial supplier signature
- Buyer confirmation signature
- Amendments might require additional signatures

**Reference elements** point to specific invoice sections.
Different parts can be signed separately if needed.

**Validation requirements**:
- Signature must be cryptographically valid
- Certificate must be ЭЦП from NCA
- Certificate must have been valid at signing time
- Signer must match invoice party (supplier or buyer)

**Integration**:
Accounting software integrates NCALayer for signing.
Users don't manually handle XML or signatures.

The system prevents tax evasion through mandatory electronic invoices.
All business-to-business transactions above a threshold require ИС ЭСФ invoices.

**Rejection reasons**:
- Invalid signature
- Expired certificate
- Wrong signer (company mismatch)
- Schema validation failure
- Missing required fields

The XMLDSig format enables XML-aware processing.
Tax authorities can extract and verify individual invoice elements.

## Links
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Kazakhstan NCALayer uses CMS for legal digital signatures]]
- [[ЭЦП requires GOST signature for legal force]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[Exclusive C14N includes only used namespaces]]
- [[SignedInfo contains what was signed and how]]
- [[Cryptographic Standards MOC]]
