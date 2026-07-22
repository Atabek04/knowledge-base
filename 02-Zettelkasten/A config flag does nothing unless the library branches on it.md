---
created: 2026-06-25
tags: [debugging/heuristic, libraries]
aliases: [no-op config flag, flag the library ignores, verify the flag in the source]
---

A config flag is a promise *your* code makes. It only comes true if the library actually branches on the value you pass. If the library reaches the same behavior through a different path, your flag is <mark style="background: #FF5582A6; font-weight: bold;">a no-op that looks like a control</mark> — and you'll waste days "disabling" something that was never wired off.

The trap: `ocspEnabled=false` only skipped adding an *extra* OCSP verifier. The library's `VerifierFlags(AUTH)` preset already performed OCSP through a *different* member (`VALIDITY_WITH_STATUS → PKIXUtil.withOCSP()`). The flag touched a path that wasn't the one doing the work.

---

### The check

Before trusting a flag, read the library source and answer: **does the code actually branch on this value, on the path that does the thing I want to stop?** Docs and field names lie; bytecode doesn't. `javap -c` / a decompiler is faster than another deploy-and-pray cycle.

The real fix is usually to find the lever the library *does* read — here, swap `VALIDITY_WITH_STATUS` for plain `VALIDITY` — not to add yet another flag on top.

### Smell

You set a flag to disable X, X still happens, and **no log line confirms the branch you expected ran**. Absence of that line is the evidence: the flag isn't on the active path. Add a log of the *resolved* setting so the no-op is visible next time.

---

### Read more
- [[Read the error message literally before forming any theory]]
- [[2026-06 OCSP flag was a no-op because Kalkan ran OCSP via a different verifier preset]]
- [[Debugging & Troubleshooting - MOC]]
