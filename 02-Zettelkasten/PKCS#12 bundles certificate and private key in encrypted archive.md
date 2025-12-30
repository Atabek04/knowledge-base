---
created: 2025-12-24
tags: [standards/pkcs]
sr-due:
sr-interval:
sr-ease:
---

PKCS#12 is a container format that bundles a private key, its corresponding certificate, and optionally the certificate chain into a single encrypted file.
It's designed for transporting complete identity credentials securely.

The entire bundle is encrypted with a password-derived key.
This protects both the private key and certificates from unauthorized access.

Common file extensions are `.p12` and `.pfx` (Personal Information Exchange).
Both extensions refer to the same PKCS#12 format.

The container can include multiple items: private key, end-entity certificate, intermediate certificates, and root certificates.
This makes it a complete package for client authentication or code signing.

PKCS#12 uses password-based encryption.
The security depends entirely on password strength — weak passwords make the encryption worthless.

It's widely used for importing/exporting certificates with private keys.
Browsers, email clients, and servers use PKCS#12 for credential management.

The format is complex with multiple layers of encryption and integrity protection.
Different items can use different encryption algorithms within the same file.

Modern alternatives like encrypted PKCS#8 exist, but PKCS#12 remains standard for interoperability.
Nearly every system that handles certificates supports PKCS#12.

Never store PKCS#12 files unprotected — they contain private keys.
Treat them like passwords: use strong encryption passwords and secure storage.

## Links
- [[PKCS#8 provides generic private key container for all algorithms]]
- [[PKCS#12 password protects sensitive key material]]
- [[P12 file extension indicates PKCS#12 format]]
- [[Certificate binds public key to verified identity]]
- [[Cryptographic Standards MOC]]
