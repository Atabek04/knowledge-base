---
created: 2025-12-24
tags: [signatures/cms, standards/kazakhstan]
sr-due:
sr-interval:
sr-ease:
---

NCALayer is Kazakhstan's middleware that enables browser-based digital signatures using CMS format.
It creates PKCS#7/CMS signatures with GOST algorithms for qualified electronic signatures (ЭЦП).

The system runs a **WebSocket server** on localhost port 13579.
Websites communicate with NCALayer through JavaScript to request signature operations.

When a user signs a document through their browser:
1. Website sends data to NCALayer via WebSocket
2. NCALayer accesses the user's hardware token or PKCS-12 file
3. KalkanCrypt library performs GOST signature creation
4. NCALayer returns CMS SignedData structure to the website
5. Website submits the signed CMS to the server

All signatures use **detached CMS format** by default.
The original document remains unchanged; the signature is returned as Base64-encoded .p7s data.

The CMS structure includes:
- GOST R 34.11-2012 (Streebog-512) as the hash algorithm
- GOST R 34.10-2015 as the signature algorithm
- The signer's certificate with IIN or BIN
- Signed attributes including signing time

**Government electronic services** require NCALayer for document signing.
Tax filing, business registration, and electronic invoicing all use NCALayer-generated signatures.

The **Electronic Invoicing System (ИС ЭСФ)** requires XMLDSig signatures created through NCALayer.
The XML is first canonicalized, then signed using CMS internally, and wrapped in XMLDSig format.

NCALayer handles the complexity of GOST algorithms and hardware token access.
Web developers only need to call JavaScript APIs without understanding cryptographic details.

The signatures have legal force in Kazakhstan courts.
CMS format with GOST algorithms meets the requirements for qualified electronic signatures.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[Kazakhstan uses ST RK GOST R 34.10-2015 with 512-bit keys]]
- [[BouncyCastle and KalkanCrypt provide GOST algorithm implementations]]
- [[Detached CMS signature stores data separately from signature]]
- [[serialNumber attribute holds IIN or BIN in Kazakhstan]]
- [[Digital Signatures MOC]]
- [[Cryptographic Standards MOC]]
