---
created: 2025-12-24
tags: [signatures/xmldsig]
sr-due:
sr-interval:
sr-ease:
---

XPath injection occurs when untrusted input is concatenated into XPath expressions.
Attackers manipulate the query logic to access unintended data or bypass security checks.

**Example vulnerable code**:
```java
String username = request.getParameter("username");
String password = request.getParameter("password");
String xpath = "//user[username='" + username + "' and password='" + password + "']";
```

**Attack**:
Username: `admin' or '1'='1`
Password: `anything`

Resulting XPath: `//user[username='admin' or '1'='1' and password='anything']`

The condition `'1'='1'` is always true, bypassing password check.

**Similar to SQL injection** but for XPath queries.
The attacker closes the string literal and injects their own logic.

**XPath operators** attackers exploit:
- `or`, `and`: Logical operators to alter conditions
- `1=1`: Always-true condition
- `//`: Select from entire document
- Comment syntax to ignore remainder: (varies by implementation)

**XMLDSig context**:
If XPath Filter Transforms use untrusted input, attackers control what gets signed.
They could select different elements than intended.

**Authentication bypass**:
XPath queries for user authentication are vulnerable.
Attackers can authenticate as any user without knowing passwords.

**Data extraction**:
Attackers can modify queries to return sensitive data.
Example: Change `//user[@id='123']` to `//user` to get all users.

The vulnerability exists wherever XPath expressions are dynamically built.
This includes authentication, data queries, and XMLDSig transforms.

## Links
- [[Fixed XPath patterns avoid injection vulnerabilities]]
- [[XPath filter selects specific XML parts to sign]]
- [[XXE attack exploits XML external entity loading]]
- [[Digital Signatures MOC]]
