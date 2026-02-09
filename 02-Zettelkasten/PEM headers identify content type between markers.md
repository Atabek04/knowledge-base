---
created: 2025-12-24
tags: [standards/asn1]
sr-due:
sr-interval:
sr-ease:
---

PEM headers and footers use specific text to identify the type of encoded data.
The header tells parsers what structure to expect after Base64 decoding.

**Common PEM labels**:
- **CERTIFICATE**: X.509 certificate (DER-encoded)
- **PRIVATE KEY**: PKCS-8 private key (algorithm-agnostic)
- **RSA PRIVATE KEY**: PKCS-1 RSA private key (RSA-specific)
- **PUBLIC KEY**: SPKI public key (algorithm-agnostic)
- **RSA PUBLIC KEY**: PKCS-1 RSA public key
- **ENCRYPTED PRIVATE KEY**: PKCS-8 encrypted private key
- **CERTIFICATE REQUEST**: PKCS-10 CSR
- **X509 CRL**: Certificate Revocation List

**Format**: `-----BEGIN [label]-----` and `-----END [label]-----`

The label must match between BEGIN and END.
Mismatched labels indicate corrupted data.

Different labels indicate different ASN.1 schemas.
`PRIVATE KEY` uses PKCS-8 structure; `RSA PRIVATE KEY` uses PKCS-1.

**Parser behavior**:
1. Read the header label
2. Determine which ASN.1 schema to use
3. Base64-decode the content
4. Parse DER using the appropriate schema

**Example distinction**:
- `-----BEGIN PUBLIC KEY-----`: Contains SPKI structure (algorithm + key bits)
- `-----BEGIN RSA PUBLIC KEY-----`: Contains just RSA modulus and exponent

Using the wrong parser for a label produces errors.
The ASN.1 structure won't match expectations.

**Tools recognize standard labels**:
OpenSSL, ssh-keygen, and other tools check the label to determine processing.

Custom labels are possible but non-standard.
Stick to recognized labels for interoperability.

Some tools are lenient and try multiple parsers.
Others strictly enforce label-schema matching.

## Links
- [[PEM Base64-encodes DER for text-safe transport]]
- [[PKCS-1 defines RSA key format with modulus and exponent]]
- [[PKCS-8 provides generic private key container for all algorithms]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[Cryptographic Standards MOC]]
