---
created: 2025-12-24
tags: [pki/revocation]
sr-due:
sr-interval:
sr-ease:
---

A CRL (Certificate Revocation List) is a signed list published by a CA containing the serial numbers of all revoked certificates.
Clients download the CRL periodically and check if a certificate's serial number appears in the list.

The CRL structure includes the issuing CA, publication timestamp, next update time, and the list of revoked certificate entries.
Each entry contains the serial number, revocation date, and reason code.

CRLs are signed by the CA to prevent tampering.
This signature proves the list is authentic and hasn't been modified.

The CA publishes updated CRLs at regular intervals — daily, hourly, or continuously depending on the CA's policy.
The CRL includes a "Next Update" field indicating when the next version will be published.

CRL distribution points are specified in certificates via the CRL Distribution Points extension.
This extension contains URLs where clients can download the current CRL.

The major disadvantage is size — CRLs grow linearly with the number of revoked certificates.
Large CAs may have CRLs containing millions of entries, making downloads slow.

Clients must download and process the entire list even if checking only one certificate.
This creates bandwidth and processing overhead.

Delta CRLs provide incremental updates containing only changes since the last full CRL.
This reduces download size but adds complexity.

## Links
- [[OCSP provides real-time certificate status check]]
- [[Revocation forcefully invalidates certificate before expiration]]
- [[CRL download can be slow due to large file size]]
- [[PKI MOC]]
