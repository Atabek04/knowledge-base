---
created: 2026-05-14
tags: [git/history]
aliases: [first-parent, --first-parent]
sr-due:
sr-interval:
sr-ease:
---

# First-parent log filters out feature internals to show release-level history

`git log --first-parent <branch>` follows only the **first parent** of each merge commit, hiding the commits that came in from the merged-in branches.

```bash
git log --graph --oneline --first-parent main
```

On `main` or `develop`, this collapses each feature merge to a single line — the merge commit itself — and skips the per-commit history of the feature branch.

**Why it matters in Gitflow:**

[[Gitflow propagation produces multiple merge commits per feature across develop release and main|Gitflow's propagation noise]] makes the full graph dense. `--first-parent main` reduces it to one line per release marker. `--first-parent develop` reduces it to one line per feature integration. Reading becomes tractable.

**Convention required:** `--first-parent` only works as a release view if you always merge **into** the long-lived branch, never the other way. That means:
- Long-lived branches (`main`, `develop`) are never the source of a merge into a topic branch.
- Topic branches rebase or [[Squash-merge collapses a feature branch into one commit on the target branch|squash-merge]] back, so the long-lived branch's first-parent chain stays clean.

If you fast-forward feature branches into `main`, those commits become first parents directly — no merge to skip over. To avoid this, use `--no-ff` for feature integrations (the [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert|Driessen convention]]) so each integration is a single first-parent merge commit.

**Useful variants:**

```bash
git log --first-parent --pretty=format:"%h %s" main   # release log
git log master..HEAD --first-parent                   # what's new since master
git rev-list --count --first-parent main              # release count
```

### Read more

- [[Gitflow propagation produces multiple merge commits per feature across develop release and main]]
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]]
- [[Squash-merge collapses a feature branch into one commit on the target branch]]
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Git MOC]]
