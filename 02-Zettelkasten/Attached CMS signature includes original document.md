---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

An attached CMS signature embeds the original document within the SignedData structure.
This creates a single file containing both the data and the signature.

The encapContentInfo field contains the actual content bytes.
Everything needed for verification is in one self-contained package.

**File extension `.p7m`** commonly indicates attached CMS signatures.
Opening the .p7m file requires a tool that can parse CMS and extract the content.

Attached signatures are useful when:
- Distributing signed documents as single files
- Email encryption and signing (S/MIME)
- Ensuring data and signature stay together
- Simplifying file management

The recipient needs only the .p7m file to verify and access the data.
No separate data file is required.

**S/MIME email** uses attached CMS signatures for signed messages.
The email body is wrapped in SignedData and sent as a MIME attachment.

Extracting the original content requires parsing the ASN.1 structure.
Tools like OpenSSL, BouncyCastle, or dedicated viewers can extract and display the content.

File size increases because the CMS structure adds metadata.
The signature, certificates, and ASN.1 encoding overhead are added to the original data size.

Some systems require attached signatures for legal compliance.
The signature and document must be inseparable to prevent accidental separation.

**Kazakhstan's electronic documents** sometimes use attached CMS.
Legal contracts might be distributed as .p7m files ensuring signature cannot be lost.

Verification extracts the content, hashes it, and checks against the signature.
If valid, the verifier can then save or display the extracted original content.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[Detached CMS signature stores data separately from signature]]
- [[CMS signing hashes data then wraps in ASN.1 container]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[DER provides deterministic binary encoding of ASN.1]]
- [[Digital Signatures MOC]]
