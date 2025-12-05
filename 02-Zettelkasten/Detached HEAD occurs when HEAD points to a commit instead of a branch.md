---
created: 2025-01-04
tags: [git/internals]
sr-due:
sr-interval:
sr-ease:
---

# Detached HEAD occurs when HEAD points to a commit instead of a branch

**HEAD** is Git's pointer to your current position in the repository. Normally, HEAD points to a branch name (like `main`), which in turn points to the latest commit on that branch.

A **detached HEAD** state happens when HEAD points directly to a commit rather than a branch. This occurs when you:
- Checkout a specific commit: `git checkout a1b2c3d`
- Checkout a tag: `git checkout v1.0`
- During rebase operations

In detached HEAD state, you can look around, make experimental changes, and even commit. However, these commits don't belong to any branch. If you switch to another branch, those commits become "orphaned" and may eventually be garbage collected.

**To save work done in detached HEAD:**
1. Create a new branch: `git checkout -b new-branch-name`
2. Or cherry-pick commits to an existing branch

The reflog (`git reflog`) can help recover commits if you accidentally leave detached HEAD without saving your work.

## Links
- [[HEAD moves forward with each commit on the current branch]]
- [[Git MOC]]
