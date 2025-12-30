---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

A complete certificate chain consists of the end-entity certificate and all intermediate certificates needed to reach a trusted root.
The root certificate itself is excluded since it's already in the trust store.

For a typical TLS connection, the server sends: end-entity cert → intermediate cert → (root is on your system).
This provides everything needed for the client to build and verify the trust chain.

The chain must be ordered correctly — each certificate signed by the next one in the sequence.
End-entity signed by Intermediate #1, Intermediate #1 signed by Intermediate #2, Intermediate #2 signed by Root.

Missing intermediates cause validation failures even if the certificates are otherwise valid.
The client cannot build a complete path to a trusted root without all links.

Some systems use cross-signing where a certificate has multiple valid chains.
This provides redundancy if one intermediate or root becomes distrusted.

Chain length affects TLS handshake performance.
Each additional certificate adds bytes to transmit and another signature to verify.

Modern protocols optimize chain transmission.
TLS 1.3 allows certificate compression, and some systems cache intermediate certificates.

Websites can test their chain configuration using tools like SSL Labs.
Common errors include missing intermediates or providing them in the wrong order.

## Links
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[Root certificate is pre-installed in operating system trust store]]
- [[Browser builds chain from server certificate to trusted root]]
- [[PKI MOC]]
