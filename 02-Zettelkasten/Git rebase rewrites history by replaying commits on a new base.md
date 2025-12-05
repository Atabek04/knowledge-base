---
created: 2025-01-04
tags: [git/branching]
sr-due:
sr-interval:
sr-ease:
---

# Git rebase rewrites history by replaying commits on a new base

Rebasing takes a series of commits and re-applies them on top of a different base commit. Git essentially "replays" each commit, creating new commits with the same changes but different parent pointers and therefore different SHA hashes.

When you run `git rebase main` from a feature branch, Git:
1. Finds the common ancestor of feature and main
2. Saves your feature commits as patches
3. Resets feature to point at main's tip
4. Applies each patch sequentially, creating new commits

Because commits get new SHAs, rebasing rewrites history. This is safe for local branches but dangerous for branches others are working on—their history will diverge from yours.

**Interactive rebase** (`git rebase -i`) lets you modify commits during replay: reorder, squash, edit messages, or drop commits entirely. This is powerful for cleaning up messy commit history before merging.

After rebasing a branch that was already pushed, you must force push (`--force-with-lease`) to update the remote.

## Links
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Force push with --force-with-lease prevents overwriting others work]]
- [[Git MOC]]
