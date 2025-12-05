---
created: 2025-01-04
tags: [git/history]
sr-due:
sr-interval:
sr-ease:
---

# Git reset removes commits while revert creates inverse commits

**Reset** and **revert** both undo changes, but they work fundamentally differently.

`git reset` moves the branch pointer backward, effectively removing commits from history. The commits still exist in the reflog temporarily but are no longer part of the branch. This rewrites history, which causes problems if the commits were already pushed to a shared remote.

`git revert` creates a new commit that undoes the changes of a previous commit. The original commit remains in history, and a new "inverse" commit is added on top. This is safe for shared branches because it doesn't rewrite history.

**Decision rule:**
- Use **reset** for local commits that haven't been pushed
- Use **revert** for commits that exist on shared/remote branches

Reset has three modes: `--soft` (keeps changes staged), `--mixed` (keeps changes unstaged), and `--hard` (discards changes entirely).

## Links
- [[Git rebase rewrites history by replaying commits on a new base]]
- [[Git MOC]]
