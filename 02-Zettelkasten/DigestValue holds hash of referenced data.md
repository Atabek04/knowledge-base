---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

DigestValue is an element within a Reference that contains the hash of the signed data.
It's encoded in Base64 for embedding in the XML structure.

The digest is computed over the referenced data after applying any Transforms.
The DigestMethod element specifies which hash algorithm was used.

**Creation process**:
1. Locate the data using the Reference URI
2. Apply Transforms in the specified order
3. Hash the transformed data using DigestMethod
4. Base64-encode the hash bytes
5. Place the encoded value in DigestValue element

**Verification process**:
1. Repeat steps 1-4 from creation
2. Compare the computed DigestValue to the value in the signature
3. If they match, the referenced data is intact

Each Reference has its own DigestValue.
A signature with multiple References has multiple DigestValues to check.

The DigestValue provides integrity but not authenticity by itself.
The SignatureValue over the entire SignedInfo provides authenticity.

An attacker could modify both the data and its DigestValue.
But they cannot update the SignatureValue without the private key.

**Example**:
```xml
<Reference URI="#invoice-data">
  <Transforms>...</Transforms>
  <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
  <DigestValue>j6lwx3rvEPO0vKtMup4NbeVu8nk=</DigestValue>
</Reference>
```

The DigestValue is the bridge between the referenced data and the signature.
It locks the data content into the signed structure.

## Links
- [[Reference element points to data being signed]]
- [[SignedInfo contains what was signed and how]]
- [[Transforms apply operations before hashing]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[Digital Signatures MOC]]
