---
created: 2025-12-24
tags: [standards/keys]
sr-due:
sr-interval:
sr-ease:
---

A raw key is the bare mathematical representation of cryptographic key material without any structural information.
It consists only of the numbers used in cryptographic operations — nothing more.

For RSA, the raw key is just two large integers: the modulus (n) and public exponent (e).
For elliptic curves, it's the x and y coordinates of a point.

Raw keys lack critical metadata.
They don't indicate which algorithm they belong to, their size, or how to interpret them.

Software cannot use raw keys directly because it doesn't know what algorithm to apply.
Is this 256-bit number an AES key, an elliptic curve coordinate, or something else?

This is why keys are always wrapped in a structured container.
Containers like ASN.1/DER add algorithm identifiers, parameter information, and proper encoding.

Raw keys exist only conceptually during cryptographic operations.
When generating or using keys, software immediately wraps them in a standard format.

Transmitting or storing raw keys would require out-of-band communication of all metadata.
Both parties would need to separately agree on algorithm, parameters, and interpretation.

## Links
- [[RSA public key contains modulus and exponent integers]]
- [[EC public key contains x y coordinates on elliptic curve]]
- [[ASN.1 defines structure of cryptographic data types]]
- [[SPKI structure holds algorithm identifier and public key bits]]
- [[Cryptographic Standards MOC]]
