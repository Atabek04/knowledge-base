---
created: 2025-01-04
tags:
  - flashcards/git
---
# Git Flashcards

## Single-Line Q&A (Commands)

What command undoes a commit but keeps changes staged?::`git reset --soft HEAD~1`

What command undoes a commit and unstages the changes?::`git reset HEAD~1` (--mixed)

What command undoes a commit and discards all changes?::`git reset --hard HEAD~1`

What command safely undoes a pushed commit?::`git revert <hash>` creates an inverse commit

What command temporarily saves uncommitted changes?::`git stash`

What command restores and removes stashed changes?::`git stash pop`

What command applies a specific commit from another branch?::`git cherry-pick <hash>`

What command replays commits on top of another branch?::`git rebase <branch>`

What command forces a merge commit when fast-forward is possible?::`git merge --no-ff <branch>`

What command force pushes safely?::`git push --force-with-lease`

## Bidirectional Cards (Terms)

DVCS:::Distributed Version Control System

HEAD:::pointer to current branch/commit

staging area:::index where changes wait before commit

fast-forward:::merge that moves pointer without merge commit

## Multi-Line Q&A (Concepts)

What is the difference between **reset** and **revert**?
?
**Reset** moves branch pointer backward (rewrites history).
**Revert** creates inverse commit (preserves history).
Use reset for local, revert for pushed commits.

When should you use **merge** vs **rebase**?
?
**Merge**: shared branches, preserves complete history
**Rebase**: local feature branches, creates linear history
Never rebase pushed commits.

What is a **detached HEAD** state?
?
HEAD points directly to a **commit** instead of a **branch**.
Commits made here are orphaned unless you create a branch.
Happens when you checkout a commit or tag directly.

What is the difference between **~** and **^** in Git?
?
**~n** moves back n generations via first parent.
**^n** selects the nth parent of a merge commit.
Example: `HEAD~2` = grandparent, `HEAD^2` = second parent of merge.

Why is **--force-with-lease** safer than **--force**?
?
Checks that remote matches your last fetch before overwriting.
If someone pushed after your fetch, the push fails.
Prevents accidental loss of teammates' commits.

Why shouldn't you rebase commits that have been pushed?
?
Rebase creates new commits with different SHAs.
Others who pulled original commits will have diverged history.
Results in duplicate commits and merge conflicts.

## Cloze Cards

Git **reset** moves the branch pointer ==backward==, while **revert** creates an ==inverse commit==.

`git reset --soft` keeps changes ==staged==, `--mixed` keeps them ==unstaged==, `--hard` ==discards== them.

In **detached HEAD**, HEAD points to a ==commit== instead of a ==branch==.

**HEAD~2** means ==grandparent== commit, **HEAD^2** means ==second parent== of a merge commit.

**Rebase** creates commits with ==new SHAs== because they have ==different parents==.

`git push --force-with-lease` only succeeds if remote matches your ==last fetch==.

**Fast-forward** merge is possible when branches haven't ==diverged==.

**Stash** stores changes in a ==stack== (LIFO) structure.
