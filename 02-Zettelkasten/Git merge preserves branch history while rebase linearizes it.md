---
created: 2025-01-04
tags: [git/branching]
sr-due:
sr-interval:
sr-ease:
---

# Git merge preserves branch history while rebase linearizes it

**Merge** and **rebase** are two strategies for integrating changes from one branch into another.

`git merge` creates a new merge commit that combines two branches. The commit history shows exactly when and where branches diverged and came back together. This preserves the complete context of parallel development.

`git rebase` takes commits from your branch and replays them on top of another branch, creating new commits with new hashes. The result is a linear history that looks as if all work happened sequentially. The original branch structure is lost.

**Trade-offs:**
- Merge: accurate history, but cluttered with merge commits
- Rebase: clean linear history, but rewrites commits (new SHAs)

**Decision rule:**
- Use **merge** for shared branches and when history context matters
- Use **rebase** for local feature branches before merging to keep history clean
- Never rebase commits that have been pushed to shared branches

A common workflow: rebase your feature branch onto main, then merge with `--no-ff` to create a single merge commit marking the feature integration.

## Links
- [[Git rebase rewrites history by replaying commits on a new base]]
- [[Git reset removes commits while revert creates inverse commits]]
- [[Git MOC]]
