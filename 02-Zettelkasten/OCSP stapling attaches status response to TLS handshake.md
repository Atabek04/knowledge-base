---
created: 2025-12-24
tags: [pki/revocation]
sr-due:
sr-interval:
sr-ease:
---

OCSP stapling is a TLS extension where the server queries the OCSP responder and includes the signed response in the handshake.
This eliminates the need for clients to contact the OCSP server, improving both performance and privacy.

The server periodically requests OCSP status for its own certificate.
The CA's OCSP responder provides a signed response with a validity period (typically 24 hours).

During TLS handshakes, the server includes this signed OCSP response as part of the certificate message.
Clients verify the response signature and check that it's current.

This solves multiple OCSP problems at once.
Clients don't leak browsing patterns to CAs, no additional round-trip to OCSP server, and reduced load on OCSP infrastructure.

The server bears the burden of OCSP queries instead of individual clients.
This is more efficient — one server querying for all clients rather than thousands of clients each querying.

If the server's OCSP response expires or becomes stale, it must refresh it.
Responsible servers query OCSP well before responses expire to avoid gaps.

Clients can verify the stapled response is current by checking the timestamp and validity period.
The CA's signature ensures the server hasn't forged the response.

OCSP Must-Staple is a certificate extension requiring stapling.
Browsers reject the connection if the server doesn't provide a stapled OCSP response.

## Links
- [[OCSP provides real-time certificate status check]]
- [[CRL lists serial numbers of revoked certificates]]
- [[Revocation forcefully invalidates certificate before expiration]]
- [[PKI MOC]]
