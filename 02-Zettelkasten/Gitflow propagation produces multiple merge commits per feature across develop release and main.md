---
created: 2026-05-14
tags: [git/workflow, branching-strategy]
aliases: [Gitflow merge pollution, Gitflow propagation noise]
sr-due:
sr-interval:
sr-ease:
---

# Gitflow propagation produces multiple merge commits per feature across develop release and main

A feature in Gitflow travels `feature → develop → release → main`, with `release` also back-merged into `develop`. Each merge creates a **separate merge commit** with different parents.

For one feature, the typical count:

| Merge | Commit |
|-------|--------|
| `feature/X → develop` | M1 |
| `develop → release/Y` (implicit, via branching) | — |
| `release/Y → main` | M2 |
| `release/Y → develop` (back-merge) | M3 |

So **3 merge commits** all referencing the same change set, plus the original feature commits. The content is not duplicated — the commits point to the same trees — but the graph topology grows criss-cross merges that are hard to read.

Mergify, Toptal and others describe Gitflow's resulting log as *"a maze"*. The cost is real but not catastrophic — these merges are also **release markers** (M2 is "this is what shipped in v1.4"), which has navigation value if you read with [[First-parent log filters out feature internals to show release-level history|first-parent log]].

**Mitigations:**
- Squash at the `feature → develop` boundary → fewer commits inside each release marker. See [[Squash-merge collapses a feature branch into one commit on the target branch|squash-merge]].
- Drop the `release` branch — stabilize on `develop`, `--ff-only` into `main` at tag. Removes M2 *or* M3 depending on direction.
- Use [[First-parent log filters out feature internals to show release-level history|`--first-parent`]] views to hide feature internals.

This noise is inherent to Gitflow's two-permanent-branch model. Teams that can't tolerate it generally move to [[Trunk-based development keeps a single main branch with short-lived feature branches|trunk-based]].

### Read more

- [[Gitflow uses long-lived develop and release branches for scheduled releases]]
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]]
- [[Squash-merge collapses a feature branch into one commit on the target branch]]
- [[First-parent log filters out feature internals to show release-level history]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[Git MOC]]
