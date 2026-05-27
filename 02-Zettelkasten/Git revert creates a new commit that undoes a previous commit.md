---
created: 2026-05-14
tags: [git/history]
aliases: [git revert, revert]
sr-due:
sr-interval:
sr-ease:
---

# Git revert creates a new commit that undoes a previous commit

`git revert <commit>` produces a new commit whose diff is the inverse of the target commit.

The original commit stays in history. The branch moves **forward**, not backward.

Because history is preserved, revert is safe on shared branches — no force-push, no diverged collaborators.

```bash
git revert a1b2c3d           # create inverse commit interactively
git revert --no-edit a1b2c3d # accept default message
git revert HEAD~3..HEAD      # revert a range
```

**Reverting a merge commit** needs `-m <parent-number>` to pick which side of the merge to keep:

```bash
git revert -m 1 <merge-sha>  # keep mainline (parent 1), undo merged branch
```

For local-only commits where rewriting history is fine, [[Git reset moves the branch pointer backward to remove commits|reset]] is cleaner — it leaves no trace.

### Read more

- [[Git reset moves the branch pointer backward to remove commits]]
- [[Git reset flags soft mixed hard control what gets undone]]
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits]]
- [[Git MOC]]
