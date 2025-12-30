---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Disabling external entity processing in XML parsers prevents XXE attacks.
Modern secure coding practices disable DTD processing and external entities by default.

**Java parser configuration**:
```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setExpandEntityReferences(false);
```

**The most secure option**: Completely disallow DOCTYPE declarations.
If no DTD is allowed, no entities can be defined.

**Alternative**: Allow DTD but disable external entities.
Internal entities remain functional but cannot reference external resources.

**SAX parser configuration**:
```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature("http://xml.org/sax/features/external-general-entities", false);
spf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
```

**XMLReader configuration**:
```java
XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

Different parser libraries have different configuration methods.
Developers must research the specific library they're using.

**OWASP recommendations**:
- Disable DTDs completely if not needed
- Disable external entities in all parsers
- Keep XML parsing libraries up to date
- Use schema validation instead of DTDs

**XMLDSig verification** should use secured parsers.
Configure security features before parsing signed documents.

Some legitimate XML uses external entities for modular documents.
In those cases, use entity catalogs to map external IDs to local resources.

**Testing**: Attempt to parse malicious XXE payloads in tests.
Verify they're rejected without processing the entity.

## Links
- [[XXE attack exploits XML external entity loading]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Digital Signatures MOC]]
