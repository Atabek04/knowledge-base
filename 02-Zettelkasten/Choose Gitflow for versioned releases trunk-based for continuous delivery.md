---
created: 2026-05-14
tags: [git/workflow, branching-strategy, decision]
aliases: [Gitflow vs trunk-based, branching strategy decision]
sr-due:
sr-interval:
sr-ease:
---

# Choose Gitflow for versioned releases trunk-based for continuous delivery

| Dimension | [[Gitflow uses long-lived develop and release branches for scheduled releases\|Gitflow]] | [[Trunk-based development keeps a single main branch with short-lived feature branches\|Trunk-based]] |
|-----------|---------|-------------|
| Long-lived branches | `main` + `develop` (+ release/hotfix) | `main` only |
| Branch lifetime | days–weeks | hours–2 days |
| Release cadence | scheduled (weeks/months) | continuous (multiple/day) |
| Unfinished code on main | no (kept on `develop`) | yes, behind feature flags |
| Parallel version support | yes (hotfix branches) | no (forward-fix only) |
| Required tooling | merge tooling | strong CI + feature flags |

**Pick Gitflow when:**
- You ship **versioned releases** (mobile apps, desktop apps, libraries, on-prem software).
- You must support **multiple released versions** in parallel (e.g. v1.4 still in production while v2.0 ships).
- Release cadence is **weeks or months**, not hours.

**Pick trunk-based when:**
- You run a **continuously deployed service** (web app, API, SaaS backend).
- You have **fast, reliable CI** and can adopt **feature flags**.
- You want to minimize merge pain — short branches don't diverge.

**Hybrid reality:** many teams run "GitHub Flow" — single `main`, PR-reviewed feature branches, deploy from `main`. That's trunk-based with PR gating. The choice is rarely pure Gitflow vs pure direct-commit trunk.

**Anti-patterns:**
- Gitflow on a deployed-daily service → release branches become a bottleneck.
- Trunk-based without feature flags → half-built features ship to prod.
- Long-lived `develop` that diverges from `main` for months → merge nightmare regardless of which strategy you claim to use.

### Read more

- [[Gitflow uses long-lived develop and release branches for scheduled releases]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Force push with --force-with-lease prevents overwriting others work]]
- [[Git MOC]]
