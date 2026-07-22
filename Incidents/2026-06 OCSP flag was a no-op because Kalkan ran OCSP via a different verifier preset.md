---
created: 2026-06-25
tags: [incident]
aliases: [auth OCSP flag no-op, PKI_OCSP_ENABLED ignored]
severity: high
status: resolved
---

> Auth-service login failed in test K8s for ~2 months; `PKI_OCSP_ENABLED=false` did nothing because the Kalkan library still ran OCSP through a different verifier preset.

---

### Symptom

ЭЦП login failed in **test K8s only** (dev VM, prod, localhost all passed). Errors shifted over time: `THIS_UPDATE_NOT_SATISFIED`, then `CertPathBuilderException`. Setting `PKI_OCSP_ENABLED=false` — the documented kill-switch — changed nothing.

### Impact

Test environment login unusable, intermittent (~70%), blocking QA. No prod impact (prod NTP correct, so OCSP passed there).

### Timeline

- `2026-04` — first failures; chased clock skew, cert chain, network egress
- `2026-05` — NTP drift on `worker1` confirmed; "warmup / cold-path" theory adopted
- `2026-06-25` — decompiled Kalkan, found the flag was a no-op; fixed + deployed; login green on worker1 first try

### Investigation

Two months of plausible-but-wrong theories: NTP drift, cert-chain cold start, a "1st-call-fails / 2nd-succeeds" warmup hypothesis. The warmup theory was killed by one observation — **it kept failing across attempts**, but a warmed process cache would pass forever after the first request. Repeated failure pointed at a per-request cause, not a one-time cold path. Then: why does disabling OCSP not help? Read the bytecode instead of the field name.

### Root cause

`VerifierFlags(VerifierFlags.AUTH)` bundles `X509CERTIFICATE_VALIDITY_WITH_STATUS`, which runs OCSP+CRL via `PKIXUtil.withOCSP().withCRL()` — **unconditionally**. Our `ocspEnabled` flag only gated a *separate*, standalone `OCSP_STATUS` verifier the AUTH preset never even included. So OCSP always ran; the flag controlled a path that did nothing. (`javap -c` on `knca_provider_util` proved it.)

Five Whys → the systemic cause: we configured a flag without verifying the library actually branches on it. See [[A config flag does nothing unless the library branches on it]].

### Fix

In `SignatureValidationService.buildVerifierFlags`: when `ocspEnabled=false`, `removeVerifyerType(VALIDITY_WITH_STATUS)` + `addVerifyerType(VALIDITY)` → plain chain build, no network, no OCSP. Confirmed in logs: `Active verifier types: [..._AUTHENTICATION, ..._KNCA_USER, X509CERTIFICATE_VALIDITY]`, first call validated on worker1.

### Prevention

- INFO log of OCSP enabled/skipped per cert + DEBUG of the resolved verifier types — the no-op is now visible.
- Unit test asserts the verifier flag list per branch, so the flag can't silently regress.

---

### Lessons

- [[A config flag does nothing unless the library branches on it]] — verify a flag in the library source, not its name.
- A theory that survives only by ignoring a contradicting observation (continued failures vs. one-time warmup) is wrong — let the data kill it.

### Read more
- [[Debugging & Troubleshooting - MOC]]
