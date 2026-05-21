---
created: 2026-05-14
tags: [git/history]
aliases: [git reset, reset]
sr-due:
sr-interval:
sr-ease:
---

# Git reset moves the branch pointer backward to remove commits

`git reset <commit>` moves the current branch pointer to the target commit.

Commits that came after are no longer reachable from the branch — they survive in the reflog for a while, then get garbage collected.

This **rewrites history**. Safe for local commits. Dangerous for commits already pushed to a shared remote — collaborators end up with diverged history.

```bash
git reset HEAD~1        # drop last commit, keep changes in working tree
git reset --hard HEAD~1 # drop last commit AND its changes
```

What "drop changes" means depends on the flag — see [[Git reset flags soft mixed hard control what gets undone|reset flags]].

For undoing commits that are already shared, use [[Git revert creates a new commit that undoes a previous commit|revert]] instead.

### Read more

- [[Git reset flags soft mixed hard control what gets undone]]
- [[Git revert creates a new commit that undoes a previous commit]]
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits]]
- [[Git MOC]]
