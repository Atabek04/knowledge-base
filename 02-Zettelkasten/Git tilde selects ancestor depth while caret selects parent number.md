---
created: 2025-01-04
tags: [git/internals]
sr-due:
sr-interval:
sr-ease:
---

# Git tilde selects ancestor depth while caret selects parent number

The `~` (tilde) and `^` (caret) operators navigate commit history differently.

**Tilde (`~n`)** moves back n generations following the first parent:
- `HEAD~1` = parent of HEAD
- `HEAD~2` = grandparent of HEAD
- `HEAD~3` = great-grandparent of HEAD

**Caret (`^n`)** selects the nth parent of a commit:
- `HEAD^1` or `HEAD^` = first parent
- `HEAD^2` = second parent (only meaningful for merge commits)

For non-merge commits, `HEAD~` and `HEAD^` are identical—both reference the single parent.

For merge commits, the distinction matters:
```
A---B---C---E (HEAD)   where E is a merge commit
         \ /
          D
```
- `HEAD^1` = C (the branch you were on when merging)
- `HEAD^2` = D (the branch that was merged in)
- `HEAD~2` = B (grandparent via first-parent path)

You can combine them: `HEAD~2^2` means "go back 2 generations, then select the second parent."

## Links
- [[HEAD moves forward with each commit on the current branch]]
- [[Detached HEAD occurs when HEAD points to a commit instead of a branch]]
- [[Git MOC]]
