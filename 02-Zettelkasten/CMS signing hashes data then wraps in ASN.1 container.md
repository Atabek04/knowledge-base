---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

Creating a CMS signature involves multiple steps that build the complete SignedData structure.
The process ensures compatibility and verifiability across different implementations.

**Step 1: Hash the content** using the chosen hash algorithm.
For GOST signatures, this uses GOST R 34.11-2012 (Streebog).
The hash is computed over the actual bytes of the data.

**Step 2: Create signed attributes** (optional but common).
Signed attributes include metadata like content type and signing time.
These attributes get included in the signature computation for additional security.

**Step 3: Hash the signed attributes** if present.
The signature is created over the attributes, which reference the content hash.
This provides both content integrity and attribute authenticity.

**Step 4: Generate the signature** using the private key.
The signature algorithm (RSA, ECDSA, GOST) operates on the hash from step 3.

**Step 5: Build the SignerInfo structure**.
This contains the signer identifier, algorithm identifiers, attributes, and signature value.

**Step 6: Assemble the complete SignedData structure**.
Includes content (or reference), certificates, algorithm identifiers, and SignerInfo structures.

**Step 7: Encode as DER** (Distinguished Encoding Rules).
The ASN.1 structure is serialized to binary format.

The result is a self-contained package with everything needed for verification.
Recipients can verify without accessing external resources if certificates are included.

Libraries like BouncyCastle and KalkanCrypt handle this complexity automatically.
Application code provides the data and key; the library produces the complete CMS structure.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[CMS structure includes content signature algorithm and certificates]]
- [[SignerInfo identifies signer and holds signature value]]
- [[Signing hashes message then encrypts hash with private key]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Digital Signatures MOC]]
