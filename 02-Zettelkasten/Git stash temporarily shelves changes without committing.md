---
created: 2025-01-04
tags: [git/workflow]
sr-due:
sr-interval:
sr-ease:
---

# Git stash temporarily shelves changes without committing

**Stashing** saves your uncommitted changes (both staged and unstaged) to a stack, reverting your working directory to the last commit. This lets you switch contexts without committing incomplete work.

**Common scenario:** You're working on a feature but need to fix an urgent bug on another branch. You can't switch branches with uncommitted changes that conflict, and you don't want to commit half-done work.

```bash
git stash              # save changes to stack
git checkout hotfix    # switch branches freely
# ... fix bug ...
git checkout feature
git stash pop          # restore changes and remove from stack
```

Stashes are stored in a stack (LIFO):
- `git stash list` — view all stashes
- `git stash apply` — restore latest without removing
- `git stash pop` — restore and remove from stack
- `git stash drop stash@{n}` — delete specific stash
- `git stash apply stash@{2}` — apply specific stash

Stashes are local—they're not pushed to remotes. They're meant for short-term storage. For longer-term work-in-progress, create a WIP branch instead.

`git stash -p` lets you selectively stash specific changes (patch mode).

## Links
- [[Git MOC]]
