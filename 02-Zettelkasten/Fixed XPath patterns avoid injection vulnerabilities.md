---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

Using fixed XPath patterns eliminates XPath injection vulnerabilities.
Never concatenate untrusted input into XPath expressions.

**Safe approach #1: Use XPath variables**
```java
XPath xpath = XPathFactory.newInstance().newXPath();
xpath.setXPathVariableResolver(new SimpleVariableResolver(
    "username", username,
    "password", password
));
String expression = "//user[username=$username and password=$password]";
```

Variables are properly escaped and typed.
Attackers cannot break out of the variable context.

**Safe approach #2: Use fixed patterns with programmatic filtering**
```java
// Fixed XPath to get all users
String expression = "//user";
NodeList users = (NodeList) xpath.evaluate(expression, doc, XPathConstants.NODESET);

// Filter in code
for (int i = 0; i < users.getLength(); i++) {
    Element user = (Element) users.item(i);
    if (username.equals(user.getAttribute("username")) &&
        password.equals(user.getAttribute("password"))) {
        return user;
    }
}
```

This avoids dynamic XPath entirely.
All data handling happens in type-safe code.

**Safe approach #3: Use XML schema + DOM**
Don't use XPath for authentication.
Load data into strongly-typed objects and use normal programming logic.

**XMLDSig context**:
XPath Filter Transforms should use fixed patterns.
```xml
<Transform Algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116">
  <XPath>//invoice:items</XPath>
</Transform>
```

Never build the XPath element from user input.

**Input validation** is NOT sufficient.
Blacklisting special characters is error-prone.
Use parameterized queries or fixed patterns instead.

**Code review checklist**:
- No string concatenation with XPath
- No `String.format()` or similar with XPath
- XPath expressions are string literals only
- User input passed through variables or validated separately

## Links
- [[XPath injection manipulates queries from unsanitized input]]
- [[XPath filter selects specific XML parts to sign]]
- [[XMLDSig signs XML documents with embedded signatures]]
- [[Transforms apply operations before hashing]]
- [[Digital Signatures MOC]]
