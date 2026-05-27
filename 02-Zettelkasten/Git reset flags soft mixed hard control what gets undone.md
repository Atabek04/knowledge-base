---
created: 2026-05-14
tags: [git/history]
aliases: [reset flags, soft mixed hard]
sr-due:
sr-interval:
sr-ease:
---

# Git reset flags soft mixed hard control what gets undone

All three modes move the branch pointer. They differ in **what they touch** beyond that.

| Flag | HEAD moves | Index (staging) | Working tree |
|------|-----------|-----------------|--------------|
| `--soft` | yes | unchanged | unchanged |
| `--mixed` (default) | yes | reset to HEAD | unchanged |
| `--hard` | yes | reset to HEAD | reset to HEAD |

**`--soft`** — undo the commit, keep changes staged. Useful for "I want to redo this commit with different message or split it."

**`--mixed`** — undo the commit and unstage its changes. Files keep edits, just need `git add` again.

**`--hard`** — wipe everything back to the target commit. **Destructive** — uncommitted work is gone.

```bash
git reset --soft HEAD~1   # uncommit, keep staged
git reset HEAD~1          # uncommit, unstage (mixed is default)
git reset --hard HEAD~1   # uncommit, discard all changes
```

Reflog can recover the lost commit for a window (default 90 days), but uncommitted changes wiped by `--hard` are unrecoverable.

### Read more

- [[Git reset moves the branch pointer backward to remove commits]]
- [[Git revert creates a new commit that undoes a previous commit]]
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits]]
- [[Git MOC]]
