---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

The `.p12` file extension indicates a PKCS#12 encoded file.
It signals that the file contains an encrypted bundle of certificates and private keys.

**Alternative extension**: `.pfx` (Personal Information Exchange)
Both `.p12` and `.pfx` refer to the same PKCS#12 format.

The `.pfx` extension originated from Microsoft implementations.
`.p12` is the more standards-compliant naming.

Modern systems accept both extensions interchangeably.
The actual file format is identical regardless of extension.

**File identification** doesn't rely solely on extension.
The file content starts with ASN.1 DER encoding of PFX structure.

**Common file operations**:
- Double-click to import into Windows certificate store
- Import into browser certificate manager
- Convert to separate PEM files using OpenSSL
- View contents with certificate viewer tools

**OpenSSL commands**:
```bash
# View contents
openssl pkcs12 -in file.p12 -info

# Extract certificate
openssl pkcs12 -in file.p12 -clcerts -nokeys -out cert.pem

# Extract private key
openssl pkcs12 -in file.p12 -nocerts -out key.pem
```

All operations require the PKCS#12 password.

**Kazakhstan digital signatures** distribute as `.p12` files.
Users download their certificate and key bundle from NCA as a password-protected P12 file.

**Email clients** export S/MIME certificates as .p12 files.
This enables transferring email signing certificates between devices.

The file is binary (DER-encoded ASN.1).
Opening in a text editor shows gibberish.

**MIME type**: `application/x-pkcs12`
Web servers and email systems use this content type.

## Links
- [[PKCS#12 bundles certificate and private key in encrypted archive]]
- [[PKCS#12 password protects sensitive key material]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[PEM Base64-encodes DER for text-safe transport]]
- [[Cryptographic Standards MOC]]
