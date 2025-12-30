---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Domain Validation (DV) certificates verify only that the requester controls the domain name.
No identity verification of the person or organization occurs — only domain control is checked.

Common verification methods include DNS TXT record, HTTP file upload, and email to admin addresses.
For DNS: add a specific TXT record; for HTTP: upload a file to /.well-known/; for email: click a link sent to admin@domain.com.

These methods can be fully automated, enabling instant certificate issuance.
Let's Encrypt revolutionized TLS by providing free DV certificates issued in seconds via ACME protocol.

DV certificates show only the domain name in the browser address bar.
There's no company name or verified identity displayed — just the padlock and domain.

The low assurance level makes DV unsuitable for high-value transactions.
You know you're connected to the domain, but not who operates it.

DV is perfect for blogs, personal websites, and internal services.
The encryption is just as strong as EV certificates — only the identity assurance differs.

Automated certificate management tools like certbot handle DV certificate renewal automatically.
Certificates expire every 90 days but renew without human intervention.

DV certificates cost nothing (Let's Encrypt) to minimal amounts compared to OV/EV.
The free availability has enabled HTTPS everywhere movement.

## Links
- [[CA verification confirms identity through various methods]]
- [[OV certificates verify organization through business registration]]
- [[Certificate binds public key to verified identity]]
- [[PKI MOC]]
