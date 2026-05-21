---
created: 2026-05-14
tags: [git/workflow, branching-strategy]
aliases: [Gitflow, git-flow]
sr-due:
sr-interval:
sr-ease:
---

# Gitflow uses long-lived develop and release branches for scheduled releases

**Gitflow** (Vincent Driessen, 2010) organizes work around two permanent branches and three supporting types.

**Permanent branches:**
- `main` — production. Every commit is a released version, tagged with a version number.
- `develop` — integration branch. Holds the next release in progress.

**Supporting branches:**
- `feature/*` — branched from `develop`, merged back into `develop`. One per feature.
- `release/*` — branched from `develop` when ready to ship. Only bugfixes and version bumps land here. Merged into **both** `main` (tagged) and `develop`.
- `hotfix/*` — branched from `main` to patch production. Merged into both `main` (new tag) and `develop`.

```
main      ─────●──────────────●────────●──── (tags: v1.0, v1.1, v1.1.1)
                \              \      /
release          \              ●────●
                  \            /      \
develop  ──●──●──●●──●──●──●──●────────●──●──
            \    /     \    /
feature      ●──●       ●──●
```

**Strengths:** clear release model for **versioned software** (mobile apps, desktop, libraries with semver). Parallel maintenance of old versions via hotfix.

**Weaknesses:** heavy. Long-lived branches diverge → painful merges. Slow to deploy. Bad fit for continuous delivery. Multi-stage propagation also creates [[Gitflow propagation produces multiple merge commits per feature across develop release and main|merge-commit noise]] in the graph.

**Keeping history clean** — recommended modern policy:
- `feature → develop`: rebase on develop, then [[Squash-merge collapses a feature branch into one commit on the target branch|squash-merge]] (one commit per feature).
- `release → main`: [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert|`--no-ff`]] merge with tag (release marker).
- Read history with [[First-parent log filters out feature internals to show release-level history|`git log --first-parent main`]] to see one line per release.

For services deployed multiple times per day, prefer [[Trunk-based development keeps a single main branch with short-lived feature branches|trunk-based development]]. See [[Choose Gitflow for versioned releases trunk-based for continuous delivery|decision guide]].

### Read more

- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[Choose Gitflow for versioned releases trunk-based for continuous delivery]]
- [[Gitflow propagation produces multiple merge commits per feature across develop release and main]]
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]]
- [[Squash-merge collapses a feature branch into one commit on the target branch]]
- [[First-parent log filters out feature internals to show release-level history]]
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Git MOC]]
