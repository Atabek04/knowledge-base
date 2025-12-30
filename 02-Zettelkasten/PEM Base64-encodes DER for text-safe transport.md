---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

PEM (Privacy-Enhanced Mail) format wraps Base64-encoded DER with header and footer lines.
It enables embedding binary cryptographic data in text files and protocols.

**PEM structure**:
```
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKWPZcXEfhP3MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
...
-----END CERTIFICATE-----
```

The header identifies what kind of data is encoded.
Common headers include:
- `-----BEGIN CERTIFICATE-----`
- `-----BEGIN PRIVATE KEY-----`
- `-----BEGIN PUBLIC KEY-----`
- `-----BEGIN RSA PRIVATE KEY-----`

The content is Base64-encoded DER.
Base64 converts binary to printable ASCII using only letters, digits, +, /, and =.

The footer matches the header with END instead of BEGIN.
This provides clear boundaries in text files.

**Benefits of PEM**:
- Safe for email, JSON, configuration files
- Visible in text editors
- Copy-paste friendly
- Line-wrapped at 64 characters for readability

**Usage**:
- TLS/SSL certificates
- SSH keys
- PGP keys
- Configuration files

To decode PEM:
1. Extract lines between header and footer
2. Concatenate them
3. Base64-decode to get DER
4. Parse DER as ASN.1

**Multiple PEM objects** can appear in one file.
A certificate chain might have multiple `BEGIN CERTIFICATE` blocks.

Some files mix PEM with plain text.
Apache configuration might include server configuration and PEM certificates.

The original PEM specification included encryption headers.
Modern use focuses on the encoding format, not the full PEM protocol.

## Links
- [[PEM headers identify content type between markers]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[PEM wraps Base64-encoded DER with header and footer]]
- [[Cryptographic Standards MOC]]
