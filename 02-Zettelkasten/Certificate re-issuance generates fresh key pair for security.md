---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Certificate re-issuance (or re-keying) involves generating a completely new key pair and obtaining a new certificate.
Both the private and public keys change, providing a fresh cryptographic foundation.

Re-keying is more secure than simple renewal because it eliminates any risk from prolonged key exposure.
If your key was compromised but you didn't know, re-keying renders the old key useless.

The process mirrors initial issuance: generate new keys, create CSR with new public key, submit for verification.
The CA performs identity verification and issues a certificate for the new public key.

Re-keying requires updating the private key everywhere it's deployed.
Servers, load balancers, and applications must all receive the new key and certificate.

Best practice recommends re-keying every 2-3 certificate renewals.
Some security-conscious organizations re-key with every certificate refresh.

The deployment complexity is why many opt for simple renewal instead.
Updating keys across distributed infrastructure can be operationally challenging.

Configuration management tools help automate re-keying.
Ansible, Puppet, and Kubernetes can distribute new keys and certificates programmatically.

After deploying new keys, securely delete old private keys.
Keeping old keys around creates unnecessary security risk.

Some compliance frameworks mandate periodic re-keying.
PCI-DSS and other standards may require key rotation on specific schedules.

## Links
- [[Certificate renewal reuses existing key pair with new dates]]
- [[Certificate issuance begins with key pair generation]]
- [[Certificate expiration automatically invalidates after validity period]]
- [[PKI MOC]]
