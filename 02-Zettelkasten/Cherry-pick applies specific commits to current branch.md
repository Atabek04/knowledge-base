---
created: 2025-01-04
tags: [git/workflow]
aliases: [cherry-pick, git cherry-pick]
sr-due:
sr-interval:
sr-ease:
---

# Cherry-pick applies specific commits to current branch

**Cherry-picking** copies a commit from one branch and applies it to another, creating a new commit with the same changes but a different SHA.

```bash
git checkout main
git cherry-pick a1b2c3d    # apply commit a1b2c3d to main
```

**Use cases:**
- Backporting a bugfix from development to a release branch
- Pulling a specific feature commit without merging the whole branch
- Recovering a commit from an abandoned branch

**What happens:**
1. Git extracts the diff introduced by the target commit
2. Applies that diff to your current branch
3. Creates a new commit with the same message (editable with `-e`)

The new commit has a different SHA because it has different parents and timestamp, even though the content changes are identical.

**Cherry-picking ranges:**
```bash
git cherry-pick A..B      # commits after A up to B (excludes A)
git cherry-pick A^..B     # includes A through B
```

**Conflicts:** If the cherry-picked changes conflict with your branch, Git pauses for manual resolution. Use `--continue` after resolving or `--abort` to cancel.

Cherry-picking duplicates commits rather than moving them. The original commit remains on its branch.

If instead you want to **remove** a commit, see [[Git reset moves the branch pointer backward to remove commits|reset]] (local) or [[Git revert creates a new commit that undoes a previous commit|revert]] (shared).

### Read more

- [[Git reset moves the branch pointer backward to remove commits]]
- [[Git revert creates a new commit that undoes a previous commit]]
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits]]
- [[Git rebase rewrites history by replaying commits on a new base]]
- [[Git MOC]]
