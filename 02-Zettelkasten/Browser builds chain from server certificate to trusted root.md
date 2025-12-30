---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

Certificate chain building is the process where a client constructs a path from an end-entity certificate up to a root certificate in its trust store.
The browser or application uses the certificates provided by the server plus any cached intermediates to build this path.

The process starts with the server's certificate and works backward.
Check who signed this certificate (Issuer DN), find that issuer's certificate, repeat until reaching a self-signed root.

Each certificate contains an "Issuer" field pointing to the certificate that signed it.
The browser uses this field to find the next certificate in the chain.

Some browsers maintain a cache of intermediate certificates.
If a server forgets to send an intermediate, the browser might have it cached from a previous connection.

Modern certificates include an "Authority Information Access" extension with URLs to download missing intermediates.
This allows automatic recovery from incomplete chains sent by servers.

Chain building can find multiple valid paths if cross-signing exists.
The browser typically chooses the shortest path to a trusted root.

Validation happens after building: check signatures, validity periods, revocation status, and policy constraints.
A successfully built chain must pass all these checks to be accepted.

Chain building failures produce certificate error warnings.
Common causes: server didn't send intermediates, no path to a trusted root, or certificates out of order.

## Links
- [[Certificate chain includes end certificate plus all intermediates]]
- [[Trust store contains database of trusted root certificates]]
- [[Transitive trust flows from root through intermediates to end certificate]]
- [[Root certificate is pre-installed in operating system trust store]]
- [[PKI MOC]]
