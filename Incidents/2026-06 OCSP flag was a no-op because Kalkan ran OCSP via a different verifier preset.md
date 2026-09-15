---
created: 2026-06-25
tags: [incident]
aliases: [OCSP flag no-op, config flag ignored by library]
severity: high
status: resolved
---

> Certificate login failed in one test cluster for about two months. The documented OCSP kill-switch changed nothing, because the Kalkan library ran OCSP through a verifier preset the flag never touched.

### Symptom

Digital-signature login failed only in the test cluster, intermittently, with `THIS_UPDATE_NOT_SATISFIED` and later `CertPathBuilderException`. Setting the OCSP-disable flag had no effect.

### Root cause

The `AUTH` verifier preset bundles a validity-with-status check that runs OCSP and CRL unconditionally. The flag only gated a separate standalone OCSP verifier that the preset never included, so OCSP always ran. Combined with NTP drift on one node, every check failed there. Decompiling the library (`javap -c`) proved it.

### Where to look next time

- A flag that "does nothing": read the library code path, not the flag's name.
- A theory that survives only by ignoring a contradicting observation (repeated failures versus a one-time warm-up) is wrong. Let the data kill it.
- Log the resolved configuration (which verifiers are active), so a no-op flag is visible.

### Lessons

- [[A config flag does nothing unless the library branches on it]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
