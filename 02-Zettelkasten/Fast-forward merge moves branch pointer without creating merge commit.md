---
created: 2025-01-04
tags: [git/branching]
sr-due:
sr-interval:
sr-ease:
---

# Fast-forward merge moves branch pointer without creating merge commit

A **fast-forward merge** occurs when the target branch has no new commits since the source branch diverged. Git can simply move the branch pointer forward—no merge commit needed.

```
Before:
A---B (main)
     \
      C---D (feature)

After fast-forward merge:
A---B---C---D (main, feature)
```

Git performs fast-forward by default when possible. The branch pointer "slides forward" along the existing commit chain.

**When fast-forward is NOT possible:**
If main has new commits since feature branched, the histories have diverged and Git must create a merge commit to combine them.

**Forcing a merge commit with `--no-ff`:**
Sometimes you want a merge commit even when fast-forward is possible—it marks the integration point and preserves the context that a feature branch existed.

```bash
git merge --no-ff feature
```

This creates a merge commit even if fast-forward was possible, preserving branch topology in the history.

**Decision:** Use `--no-ff` for feature branches to maintain clear history of what was developed together. Allow fast-forward for trivial updates.

## Links
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Git MOC]]
