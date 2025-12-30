---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Revocation is the act of forcefully marking a certificate as invalid before its natural expiration date.
This is necessary when something goes wrong — compromised private key, incorrect information, or changed circumstances.

Common revocation reasons include private key compromise, CA compromise, cessation of operation, and affiliation changed.
Each has a specific revocation reason code in the CRL or OCSP response.

Once revoked, a certificate cannot be un-revoked.
If revocation was a mistake, a new certificate must be issued with a different serial number.

The CA adds the certificate's serial number to its Certificate Revocation List (CRL).
Clients check this list during validation and reject revoked certificates.

Online Certificate Status Protocol (OCSP) provides real-time revocation checking.
Instead of downloading a full CRL, clients query for specific certificate status.

Revocation checking is not always enforced by browsers.
Soft-fail policies mean validation continues even if revocation status can't be determined.

Time between compromise and revocation publication is critical.
Attackers can exploit compromised certificates during this window.

Certificate transparency logs help detect unauthorized certificate issuance.
Domain owners can spot and request revocation of fraudulent certificates.

After revoking, immediately obtain and deploy a replacement certificate.
Services will break for users who check revocation status.

## Links
- [[CRL lists serial numbers of revoked certificates]]
- [[OCSP provides real-time certificate status check]]
- [[Certificate lifecycle has issuance active and end-of-life stages]]
- [[Intermediate CA compromise only requires revoking that intermediate]]
- [[PKI MOC]]
