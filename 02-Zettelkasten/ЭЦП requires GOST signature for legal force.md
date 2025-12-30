---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

ЭЦП (Электронная Цифровая Подпись, Electronic Digital Signature) is Kazakhstan's term for qualified electronic signatures.
These signatures have the same legal force as handwritten signatures under Kazakhstan law.

**Requirements for ЭЦП**:
- Certificate issued by National Certification Authority (NCA)
- GOST R 34.10-2015 signature algorithm (512-bit)
- GOST R 34.11-2012 hash function (Streebog-512)
- Hardware token or certified key storage
- Proper certificate policies

**Legal framework** establishes that ЭЦП signatures:
- Are equivalent to handwritten signatures
- Cannot be repudiated by the signer
- Prove document integrity
- Prove identity of the signer

**Non-qualified signatures** using RSA or ECDSA don't have legal force.
They may provide technical security but lack legal recognition.

Only signatures from NCA-issued certificates count as ЭЦП.
Commercial CAs can issue certificates but they're not qualified signatures.

**Government services** require ЭЦП for:
- Tax filing and reporting
- Business registration
- Electronic invoicing (ИС ЭСФ)
- Public procurement
- Legal document submission

The **certificate must be active** at signing time.
Expired or revoked certificates don't produce valid ЭЦП.

**Timestamp services** prove when the signature was created.
This prevents backdating or claiming expiration at signing time.

**Signature formats**:
- CMS (PKCS#7) for binary documents
- XMLDSig for XML documents (invoices)
- Both must use GOST algorithms

**Verification** requires checking:
1. Signature cryptographically valid
2. Certificate issued by NCA
3. Certificate was valid at signing time
4. Certificate not revoked
5. Correct GOST algorithms used

International signatures (RSA, ECDSA) are not recognized as ЭЦП.
Foreign entities doing business in Kazakhstan need NCA certificates.

## Links
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[Kazakhstan NCALayer uses CMS for legal digital signatures]]
- [[Certificate policy defines rules for certificate issuance]]
- [[Non-repudiation prevents signer from denying signature]]
- [[ИС ЭСФ uses XMLDSig for electronic invoices]]
- [[Cryptographic Standards MOC]]
