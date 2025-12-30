---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Organization Validation (OV) certificates verify that the requesting organization legally exists and that the requester is authorized to represent it.
This provides more assurance than DV but less than Extended Validation (EV).

The CA checks business registration with government databases.
They verify the organization name, address, phone number, and legal incorporation status.

The CA contacts the organization via verified phone numbers or email addresses.
They confirm that an authorized representative requested the certificate.

Some CAs require supporting documentation like business licenses or tax registration.
The exact requirements vary by CA and jurisdiction.

Processing time is longer than DV — typically 1-3 business days for verification.
Human review is required, preventing instant automated issuance.

OV certificates display the organization name in the certificate details.
Modern browsers show this when clicking the padlock icon, though not prominently in the address bar.

OV strikes a balance between cost, assurance, and convenience.
It's popular for corporate websites, e-commerce, and SaaS platforms.

Certificate costs are higher than DV but lower than EV.
Prices range from tens to hundreds of dollars annually.

The verification must be repeated for each certificate renewal.
CAs may streamline the process for existing customers but still perform checks.

## Links
- [[CA verification confirms identity through various methods]]
- [[DV certificates verify domain ownership via DNS or email]]
- [[Certificate binds public key to verified identity]]
- [[PKI MOC]]
