---
created: 2025-12-24
tags: [pki/revocation]
sr-due:
sr-interval:
sr-ease:
---

CRLs from major CAs can grow to many megabytes as they accumulate revoked certificates over time.
Downloading these large files creates latency and bandwidth overhead, especially on mobile or slow connections.

A CRL with millions of entries can easily exceed 10-50 MB in size.
Downloading this before establishing every TLS connection would make web browsing unusably slow.

Most browsers cache CRLs and only download updates periodically.
This reduces overhead but means revocation information may be stale.

The size problem compounds for clients connecting to many different sites.
Each unique issuing CA requires downloading a separate CRL.

Delta CRLs help by providing only changes since the last download.
But this requires more complex logic to merge deltas with base CRLs.

OCSP emerged as a solution, replacing bulk CRL downloads with targeted queries.
A small request for one certificate status replaces downloading an entire list.

Some CAs partition CRLs — instead of one huge list, publish multiple smaller CRLs by date range or certificate type.
This reduces individual CRL size but adds complexity.

Modern browser behavior increasingly ignores CRLs in favor of OCSP or OCSP stapling.
CRLs remain important for specialized environments with specific security requirements.

## Links
- [[CRL lists serial numbers of revoked certificates]]
- [[OCSP provides real-time certificate status check]]
- [[OCSP stapling attaches status response to TLS handshake]]
- [[PKI MOC]]
