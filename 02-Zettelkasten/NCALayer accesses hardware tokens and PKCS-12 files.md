---
created: 2025-12-24
tags: [standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

NCALayer can access private keys stored in two different formats.
It provides unified API regardless of key storage method.

**Hardware tokens** (USB smart cards):
- eToken, JaCarta, and other PKCS-11 compatible devices
- Keys stored in tamper-resistant hardware
- PIN required for each signature operation
- Higher security, harder to steal keys

**PKCS-12 files** (.p12 files):
- Software-based key storage
- Keys encrypted with password
- Stored on local disk
- Convenient but less secure than hardware

The user selects which key to use in NCALayer interface.
Available keys from all sources appear in the selection dialog.

**Key discovery**:
For hardware tokens, NCALayer uses PKCS-11 interface.
It enumerates connected tokens and reads certificates.

For PKCS-12 files, users manually import them into NCALayer.
The import process requires the PKCS-12 password.

**Signature process**:
1. Website requests signature via WebSocket
2. NCALayer shows available certificates to user
3. User selects certificate and enters PIN/password
4. KalkanCrypt performs signature using selected key
5. Signature returned to website

**Certificate validity checking**:
NCALayer verifies certificates before allowing their use.
Expired or revoked certificates are marked as invalid.

**Multiple certificates** on one token are supported.
Users might have personal and organizational certificates.

The abstraction over storage types simplifies application development.
Websites don't need different code for hardware vs software keys.

**Migration path**: Users can start with PKCS-12 files.
Later upgrade to hardware tokens without changing applications.

## Links
- [[NCALayer bridges browsers to local cryptographic hardware]]
- [[NCALayer runs WebSocket server on localhost port 13579]]
- [[PKCS-12 bundles certificate and private key in encrypted archive]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[PKCS-12 password protects sensitive key material]]
- [[Cryptographic Standards MOC]]
