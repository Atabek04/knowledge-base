---
created: 2026-10-14
aliases: [staging drift, environment drift, test in production, testing in production]
tags: [devops, deployment-environments, release, observability]
---

Staging is meant to be production without the users. In practice it never stays that way for long, and a release that passed staging can still fail on its first minute in production.

That gap has split practitioners into two camps: teams that invest in keeping staging faithful, and teams that drop it and make production itself safe to test in.

---

### Why staging drifts

<mark style="background: #FFF3A3A6;">Environment drift is the gradual divergence between staging and production, as manual fixes, config changes, data growth and traffic patterns accumulate on one side and not the other.</mark>

Some differences are fixable: a hotfix applied by hand in production, a config value changed in one place, a data copy that is three months old.

Others are not. <mark style="background: #ABF7F7A6;">Staging has no real users, so it never sees real traffic volume, real concurrency, real geographic spread or the strange inputs real people send, and those are where the hardest failures live.</mark>

---

### The test-in-production position

Charity Majors (Honeycomb) and teams such as Hunter.io argue that staging mostly catches failure modes you already knew to look for, while giving the team the feeling that the release is safe.

Their alternative keeps testing but moves the last check into production, behind guardrails:

- **Feature flags**: new code ships switched off and is turned on for a few users at a time.
- **Canary releases**: the new version takes a small slice of traffic first, named after the canary miners carried to detect gas before it reached them.
- **Observability**: detailed telemetry shows within minutes whether the new version is behaving worse.
- **Fast rollback**: a bad change is reverted in seconds rather than hours.

Google's SRE workbook makes a related point: a canary is the first step of deployment, not the last step of testing.

<mark style="background: #FF5582A6;">Testing in production means testing better, never testing less; without flags, canaries and observability it is just shipping untested code to users.</mark>

---

### Where staging still earns its cost

The debate is about confidence, not about whether staging is useless. Staging stays valuable for rehearsing risky migrations, for manual exploration that automated tests are too clean to cover, and wherever regulation demands a documented pre-production step.

---

### Read more
- [[Staging mirrors production config, data and infrastructure so the deploy itself can be rehearsed]]
- [[Each deployment environment exists to keep one workload from corrupting another's results]]
- [[Ephemeral preview environments give each pull request its own isolated copy instead of a shared queue]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[DevOps - MOC]]
- [[Observability - MOC]]

### External Resources
- [Honeycomb: I test in prod](https://honeycomb.io/blog/i-test-in-prod)
- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [DevOps.com: Dear staging, we're done](https://devops.com/dear-staging-were-done/)
- [Increment: Best practices for staging environments](https://increment.com/development/center-stage-best-practices-for-staging-environments/)
