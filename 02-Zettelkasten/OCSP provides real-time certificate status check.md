---
created: 2025-12-24
tags: [pki/revocation]
sr-due:
sr-interval:
sr-ease:
---

OCSP (Online Certificate Status Protocol) allows clients to query a CA's server in real-time for the status of a specific certificate.
Instead of downloading a full CRL, the client asks "Is certificate serial number X valid?" and receives an immediate response.

The OCSP request contains the certificate serial number and issuer information.
The OCSP responder checks its database and returns: "Good," "Revoked," or "Unknown."

OCSP responses are signed by the CA or an authorized OCSP signing certificate.
This signature proves the response is authentic and current.

Responses include a timestamp and validity period.
Clients can cache responses until they expire, reducing repeated queries.

OCSP is much more efficient than CRL for checking individual certificates.
A tiny request and response replace downloading a multi-megabyte CRL.

The real-time nature provides up-to-date revocation information.
CRLs may be hours or days old, while OCSP can reflect revocations immediately.

Privacy concerns exist — OCSP queries reveal which sites you're visiting to the CA.
The CA sees every OCSP check, potentially creating browsing surveillance.

OCSP stapling addresses this by having servers query OCSP and include the signed response in the TLS handshake.
Clients verify the stapled response without contacting the OCSP server.

## Links
- [[CRL lists serial numbers of revoked certificates]]
- [[OCSP stapling attaches status response to TLS handshake]]
- [[Revocation forcefully invalidates certificate before expiration]]
- [[PKI MOC]]
