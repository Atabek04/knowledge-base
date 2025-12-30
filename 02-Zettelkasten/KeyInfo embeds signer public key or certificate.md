---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

KeyInfo is an optional XMLDSig element that provides information about the signing key.
It enables verifiers to locate the public key or certificate needed for verification.

**KeyInfo can contain**:
- **X509Data**: X.509 certificate chain
- **KeyValue**: raw public key values (RSA modulus/exponent or EC point coordinates)
- **KeyName**: a name that identifies which key to use
- **RetrievalMethod**: URL where the key can be retrieved

The **X509Certificate** element contains the Base64-encoded DER certificate.
This provides the complete certificate including public key, identity, and CA signature.

Example:
```xml
<KeyInfo>
  <X509Data>
    <X509Certificate>
      MIIDXTCCAkWgAwIBAgIJAKWPZcXEfhP3MA0GCS...
    </X509Certificate>
  </X509Data>
</KeyInfo>
```

Including the certificate enables standalone verification.
Verifiers don't need external certificate lookup.

**KeyValue** is simpler but less secure.
It provides the public key without CA verification of identity.

```xml
<KeyInfo>
  <KeyValue>
    <RSAKeyValue>
      <Modulus>xA7SE...</Modulus>
      <Exponent>AQAB</Exponent>
    </RSAKeyValue>
  </KeyValue>
</KeyInfo>
```

**Security consideration**: KeyInfo is not covered by the signature.
Attackers could theoretically replace KeyInfo with their own key and signature.

Applications must verify the KeyInfo matches expected values.
Check the certificate issuer, subject, or validate against a trusted CA.

**Kazakhstan ИС ЭСФ** requires X509Data with the complete certificate chain.
The signing certificate must be issued by the National Certification Authority.

KeyInfo is optional; applications might obtain keys through other means.
Pre-shared keys or key distribution protocols can provide the public key externally.

## Links
- [[XMLDSig signs XML documents with embedded signatures]]
- [[SignatureValue contains actual signature bytes]]
- [[Certificate binds public key to verified identity]]
- [[RSA public key contains modulus and exponent integers]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[Base64 converts binary to printable ASCII for text channels]]
- [[Digital Signatures MOC]]
