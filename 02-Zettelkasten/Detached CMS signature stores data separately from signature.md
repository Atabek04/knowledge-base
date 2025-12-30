---
created: 2025-12-24
tags: [signatures/cms]
sr-due:
sr-interval:
sr-ease:
---

A detached CMS signature stores only the signature metadata, not the original data.
The signed content remains in its original file, with the signature in a separate file.

The CMS SignedData structure includes the hash of the content but not the content itself.
The encapContentInfo field contains a content type identifier but empty content bytes.

**File organization** typically places signature and data side by side.
Example: `document.pdf` and `document.pdf.p7s` (detached signature).

Detached signatures are useful when:
- The signed data is large (videos, disk images, software packages)
- Multiple signatures need to be applied to the same data
- The original format must be preserved (signed PDFs, images)

Verification requires both files: the signature and the original data.
The verifier reads the data, hashes it, and compares to the hash referenced in the signature.

**Software distribution** commonly uses detached signatures.
A signature file accompanies a download without modifying the original binary.

The signature file contains:
- Hash algorithm identifier
- Signature algorithm identifier
- Signer certificate (optional)
- Signature value
- Signed attributes (like signing time)

The original data file remains unchanged and usable even without the signature.
Users can verify authenticity or use the file directly if they don't need verification.

Detached signatures enable post-signing without modifying the original.
Multiple parties can add signatures without altering each other's signature files.

## Links
- [[CMS wraps data with signature and signer certificate]]
- [[Attached CMS signature includes original document]]
- [[CMS signing hashes data then wraps in ASN.1 container]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[CMS supports multiple signers on same document]]
- [[Digital Signatures MOC]]
