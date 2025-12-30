---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

PEM (Privacy-Enhanced Mail) format wraps binary DER data in Base64 encoding with distinctive header and footer lines.
This makes binary cryptographic data safe to transmit through text-only channels like email or configuration files.

A PEM file consists of three parts: header, Base64-encoded DER, and footer.
Example: `-----BEGIN PUBLIC KEY-----`, Base64 data, `-----END PUBLIC KEY-----`.

The header/footer labels indicate what type of object is encoded.
`PUBLIC KEY` for public keys, `CERTIFICATE` for X.509 certificates, `PRIVATE KEY` for private keys.

Base64 encoding converts every 3 bytes of binary into 4 ASCII characters.
This increases size by about 33% but ensures the data won't be corrupted by text processing.

PEM files can be opened in any text editor and copied/pasted safely.
Line breaks in the Base64 data are ignored during decoding.

Multiple PEM objects can be concatenated in one file.
Certificate chains often use this — root cert + intermediate cert in a single `.pem` file.

Despite the "Mail" in the name, PEM is used far beyond email.
Web servers, key management systems, and command-line tools all use PEM format.

The content between headers is identical DER — just Base64-encoded.
Decoding the Base64 recovers the exact same DER bytes.

## Links
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[PEM headers identify content type between markers]]
- [[Encoding converts data format without providing secrecy]]
- [[Cryptographic Standards MOC]]
