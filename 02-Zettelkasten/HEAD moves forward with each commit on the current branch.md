---
created: 2025-01-04
tags: [git/internals]
sr-due:
sr-interval:
sr-ease:
---
# HEAD moves forward with each commit on the current branch

**HEAD** is a symbolic reference that tells Git which branch or commit you're currently working on. It answers the question: "Where am I in the repository?"

When HEAD points to a branch (the normal state), it's a symbolic reference to that branch. The branch pointer in turn points to the latest commit. When you make a new commit:
1. Git creates the commit with the current HEAD commit as its parent
2. The branch pointer moves forward to the new commit
3. HEAD still points to the branch, so it effectively moves forward too

You can reference HEAD in commands:
- `HEAD~1` or `HEAD~` — the parent commit
- `HEAD~2` — the grandparent commit
- `HEAD^` — the first parent (same as `HEAD~` for non-merge commits)
- `HEAD^2` — the second parent of a merge commit

The distinction between `~` and `^` matters for merge commits: `~` follows the first parent lineage, while `^n` selects the nth parent of a specific commit.

## Links
- [[Detached HEAD occurs when HEAD points to a commit instead of a branch]]
- [[Git tilde selects ancestor depth while caret selects parent number]]
- [[Git MOC]]
