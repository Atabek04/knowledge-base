---
created: 2026-05-14
tags: [git/history, decision]
aliases: [revert vs reset vs cherry-pick, undo decision]
sr-due:
sr-interval:
sr-ease:
---

# Choose revert for shared history reset for local cleanup cherry-pick to port commits

Three operations that all "move commits around" — but each fits a different situation.

| Tool | Rewrites history? | Use when |
|------|-------------------|----------|
| [[Git revert creates a new commit that undoes a previous commit\|revert]] | no | undoing a commit already pushed/shared |
| [[Git reset moves the branch pointer backward to remove commits\|reset]] | yes | cleaning up local commits before push |
| [[Cherry-pick applies specific commits to current branch\|cherry-pick]] | no | copying a commit to another branch |

**Decision flow:**

1. Is the commit already on a shared remote?
   - Yes → [[Git revert creates a new commit that undoes a previous commit|revert]]. Never rewrite published history.
   - No → continue.
2. Do you want the commit **gone** from this branch?
   - Yes → [[Git reset moves the branch pointer backward to remove commits|reset]]. Pick the [[Git reset flags soft mixed hard control what gets undone|flag]] based on whether you want changes kept/staged/wiped.
3. Do you want the commit **on a different branch**?
   - Yes → [[Cherry-pick applies specific commits to current branch|cherry-pick]]. Original stays where it was; a copy lands on the target.

**Common pitfalls:**

- Using `reset --hard` on a shared branch → forces collaborators to recover from reflog.
- Cherry-picking a merge commit without `-m` → fails. Use `git cherry-pick -m 1 <sha>`.
- Reverting a merge then trying to re-merge → the revert blocks the merge; you must revert the revert.

### Read more

- [[Git reset moves the branch pointer backward to remove commits]]
- [[Git reset flags soft mixed hard control what gets undone]]
- [[Git revert creates a new commit that undoes a previous commit]]
- [[Cherry-pick applies specific commits to current branch]]
- [[Git merge preserves branch history while rebase linearizes it]]
- [[Git MOC]]
