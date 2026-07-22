---
aliases: [Debugging, Troubleshooting, Incident Response]
tags: [moc, debugging, troubleshooting, engineering, mindset]
created: 2026-06-24
---

> The reusable craft of debugging — the mindsets, methods, and heuristics that turn "something is broken" into a found root cause. Specific incidents are logged separately under `Incidents/`; the lessons they teach get promoted up into the atomic notes here.

---

## Mindsets & Mental Models

- [[Read the error message literally before forming any theory|Read the error literally — the message already names the fault]]
- [[Change one variable at a time when debugging to keep cause and effect clear|Change one variable at a time — keep cause and effect clear]]
- [[Bisection isolates a fault by repeatedly halving the search space|Bisection — halve the search space, O(n) becomes O(log n)]]
- [ ] Reproduce the bug reliably before trying to fix it
- [ ] Trust the machine, not your assumptions — the computer is not lying
- [ ] Suspect your own code before the framework, OS, or compiler
- [ ] An HTTP status says *where* a request died, not *why* — anchor on the earliest error in the log, not the final status code
- [ ] A bug's blast radius equals whoever handles its error most aggressively — a global symptom-handler turns a local fault into an outage

---

## Thinking Methods

- [[Debug by the scientific method observe hypothesize test repeat|Scientific method — observe, hypothesize, test, repeat]]
- [[The Five Whys traces a symptom to its root cause by asking why repeatedly|Five Whys — ask why until you hit a fixable root cause]]
- [[Differential debugging asks what changed since the system last worked|Differential debugging — what changed since it last worked]]
- [[Rubber duck debugging surfaces the bug by explaining the code aloud|Rubber duck — explaining it aloud exposes the gap]]
- [ ] git bisect — binary search across commits to find the breaking one
- [ ] Minimal reproducible example — strip the problem to its smallest form
- [ ] Read the source of the library, not just its docs
- [[A config flag does nothing unless the library branches on it|A config flag is a no-op unless the library branches on it — verify in the source]]
- [ ] When an unpushed change "causes" a shared bug, widen the system boundary — the fault predates your branch or lives in a neighbor service or the client
- [ ] Exonerate a component with a diff, not a hunch — `git diff` across branches/services proves "X is fine" instead of assuming it

---

## Heuristics & Shortcuts

- [ ] Check the boring causes first — DNS, auth, config, cache, disk full
- [ ] If it worked yesterday, suspect a change not the code
- [ ] Config says X but behavior says not-X → suspect stale state (caches, compiled output, IDE indices)
- [ ] Multiple symptoms sharing a timestamp → one upstream cause, not many bugs
- [ ] The bug is usually in the last thing you touched
- [ ] When stuck, take a break — fresh eyes beat tired persistence
- [ ] Correlation in logs: line up timestamps across services
- [ ] Absence of an expected log line is evidence — no handler line = it escaped; no auth line = no token was sent
- [ ] An error re-dispatched through another layer surfaces disguised (500 → 401) — look for `/error`, a proxy, or a retry that re-evaluated the request in a stripped context

---

## Incident Practice

- [ ] Write a blameless postmortem after every real incident
- [ ] Separate symptom, impact, root cause, fix, and prevention
- [ ] Promote each incident's lesson into a reusable atomic note above

### Logged Incidents

- [[2026-06 IntelliJ update left a stale final class breaking Spring config|IntelliJ update → stale final .class broke Spring allopen config]]
- [[2026-06 ClickHouse view type desync surfaced as a phantom 401|ClickHouse view type desync → unhandled 500 masked as empty-body 401]]
- [[2026-06 OCSP flag was a no-op because Kalkan ran OCSP via a different verifier preset|OCSP flag no-op → Kalkan ran OCSP via a different verifier preset]]

---

## Related

- [[DevOps - MOC]]
- [[Software Engineering - MOC]]
