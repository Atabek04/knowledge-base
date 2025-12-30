---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

Root certificates are distributed pre-installed in operating systems and browsers during software installation or device manufacturing.
This establishes the initial trust anchors without requiring users to manually configure anything.

Windows, macOS, iOS, Android, and Linux distributions all ship with trust stores containing root certificates.
These stores are carefully curated — only CAs that meet strict security and operational requirements are included.

The trust store typically contains 100-200 root certificates from CAs worldwide.
Examples include DigiCert, Let's Encrypt, GlobalSign, and national CAs like Kazakhstan's NCA.

Browser vendors (Mozilla, Google, Microsoft, Apple) maintain their own trust store programs.
CAs must apply and demonstrate compliance with baseline requirements before inclusion.

The OS trust store is usually located in a protected system directory.
On Windows: Certificate Manager (certmgr.msc), on macOS: Keychain Access, on Linux: /etc/ssl/certs/.

Updates to the trust store happen through OS updates.
When a CA is compromised or fails audit, it can be removed via software updates.

Users can manually add or remove root certificates, but this is risky.
Adding untrusted roots enables man-in-the-middle attacks; removing legitimate roots breaks website access.

The pre-installation solves the bootstrapping problem — how do you trust the first certificate?
You trust what the OS vendor trusts, shifting the trust decision to a party you already trust.

## Links
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Trust store contains database of trusted root certificates]]
- [[Browser builds chain from server certificate to trusted root]]
- [[Compromised root CA requires global trust store updates]]
- [[PKI MOC]]
