---
created: 2026-05-14
tags: [git/workflow, branching-strategy]
aliases: [trunk-based, TBD, trunk-based development]
sr-due:
sr-interval:
sr-ease:
---

# Trunk-based development keeps a single main branch with short-lived feature branches

**Trunk-based development (TBD)** has one long-lived branch — `main` (the "trunk"). All developers integrate to it continuously.

**Two flavors:**
- **Direct commit to trunk** — small teams, every commit goes straight to `main` behind CI.
- **Short-lived feature branches** — branch from `main`, merge back within **1–2 days**, never longer. PR review + CI gate the merge.

```
main ──●──●──●──●──●──●──●──●──●──● (deployed continuously)
        \    /  \    /  \    /
         ●──●    ●──●    ●──●     (feature branches, < 2 days)
```

**Key practices:**
- **Feature flags** — merge unfinished code dark, toggle on later. Decouples deploy from release.
- **CI on every push** — broken trunk blocks everyone, so tests must be fast and reliable.
- **No release branches** — `main` is always releasable. Tag commits for releases if needed.
- **Hotfix = forward fix** — fix on trunk, redeploy. No back-porting.

**Strengths:** fits CI/CD. Minimal merge conflicts (branches too short to diverge). Fast feedback. Standard at Google, Facebook, Netflix.

**Weaknesses:** requires strong test automation and feature-flag discipline. Hard for teams that can't deploy frequently or maintain multiple released versions in parallel.

For software with versioned releases and parallel maintenance (mobile apps, libraries), [[Gitflow uses long-lived develop and release branches for scheduled releases|Gitflow]] fits better. See [[Choose Gitflow for versioned releases trunk-based for continuous delivery|decision guide]].

### Read more

- [[Gitflow uses long-lived develop and release branches for scheduled releases]]
- [[Choose Gitflow for versioned releases trunk-based for continuous delivery]]
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Git MOC]]
