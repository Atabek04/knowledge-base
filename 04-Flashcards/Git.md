---
created: 2025-01-04
tags: [flashcards, flashcards/git]
---

# Git Flashcards

## Fundamentals

How does a **distributed VCS** differ from a **centralized VCS** like Subversion?
?
In a **centralized VCS**, only the server holds the complete repository and history. Developers must be connected to the server for most operations and there's a single point of failure.
<!--SR:!2026-01-02,3,250-->

In **DVCS** like Git, every developer clones the **entire repository** including full history, enabling offline work, fast operations, and peer-to-peer collaboration.

---

Why can Git developers work offline while Subversion developers cannot?
?
**DVCS** stores the complete repository history locally on each developer's machine. Operations like committing, branching, and viewing history work entirely offline without needing network access to a central server.

---

When you clone a Git repository, what exactly gets copied to your machine?
?
**Cloning** copies the entire **remote repository**, including:
- All commits and branch history
- Complete metadata
- All previous versions of every file

This is why each clone can serve as a **full backup** and why any clone can restore the project if the original is lost.

---

What architectural guarantee does DVCS provide that centralized VCS cannot?
?
**DVCS** eliminates the single point of failure. Since every clone contains the complete history, **no single server failure can lose the project**. Any developer's local copy can become the source of truth for the team.

---

How is "origin" different in Git compared to centralized VCS?
?
In centralized VCS, the server is architecturally required—developers cannot work without it.

In **DVCS**, "origin" is just a **naming convention** for the shared repository. It's not required; you could push and pull between any repositories, making the architecture **peer-to-peer** by default.

---

## History & HEAD

What does **HEAD** represent in a Git repository?
?
**HEAD** is a **symbolic reference** that tells Git which branch or commit you're currently working on.

When you make a new commit, Git uses **HEAD** to determine what the parent of the new commit will be, answering the question: "Where am I right now?"

---

How does **HEAD** move when you make a new commit?
?
When **HEAD** points to a branch (normal state):
1. Git creates a new commit with the **current HEAD commit as parent**
2. The **branch pointer moves forward** to the new commit
3. **HEAD still points to the branch**, effectively moving forward with it

This is why committing on `main` automatically advances the `main` branch pointer.

---

What is a **detached HEAD** and when does it occur?
?
A **detached HEAD** occurs when **HEAD points directly to a commit** instead of pointing to a branch.

This happens when you:
- Checkout a specific commit: `git checkout a1b2c3d`
- Checkout a tag: `git checkout v1.0`
- During rebase operations

---

Why is **detached HEAD** dangerous for preserving work?
?
Commits made in **detached HEAD** state don't belong to any branch. If you switch branches without creating a new branch, those commits become **orphaned** and may eventually be **garbage collected**, losing your work.

---

How do you save work from a **detached HEAD** state?
?
You can:
1. **Create a new branch** at the current commit: `git checkout -b new-branch-name`
2. **Cherry-pick** commits to an existing branch
3. Use **git reflog** to find and recover commits from the detached state

---

How does the **tilde operator** (`~`) navigate Git history?
?
The **tilde operator** (`~n`) moves back **n generations following the first parent line**:
- `HEAD~1` (or `HEAD~`) = parent commit
- `HEAD~2` = grandparent commit
- `HEAD~3` = great-grandparent commit

For non-merge commits, this is the only ancestor path.

---

How does the **caret operator** (`^`) differ from tilde?
?
The **caret operator** (`^n`) selects the **nth parent of a specific commit**:
- `HEAD^1` or `HEAD^` = first parent
- `HEAD^2` = second parent

**Tilde** moves back generations on the first-parent line; **caret** selects among multiple parents of a single commit.

---

Why does the distinction between `^` and `~` only matter for **merge commits**?
?
Non-merge commits have only one parent, so `HEAD~1` and `HEAD^` both refer to the same commit.

**Merge commits have two parents**, so the distinction becomes crucial:
- `HEAD^1` = the branch you were on when merging
- `HEAD^2` = the branch you merged into your branch
- `HEAD~2` = your grandparent along the first-parent lineage

---

How do you reference the second parent of a **merge commit**?
?
Use the **caret** operator with the parent number: `HEAD^2`

This selects the **second parent** of the merge commit. Trying to use **tilde** (`HEAD~2`) would skip the second parent entirely and go back two generations on the first-parent line.

---

What does `HEAD~2^2` select?
?
Go back **2 generations** using **tilde**, then select the **second parent** of that ancestor commit using **caret**.

This combines both operators to navigate complex merge histories.

---

== HEAD == is a symbolic reference that points to the **current branch or commit** you're working on in your repository.

---

The ==~== operator moves back **n generations** along the first-parent line, while the ==^== operator **selects among multiple parents** of a single commit.

---

## Undoing Changes

How does `git reset` differ from `git revert` in their approach to undoing changes?
?
**Git reset** moves the **branch pointer backward**, removing commits from history (rewrites history).

**Git revert** creates a **new commit that undoes the changes** from a previous commit (preserves history).

This fundamental difference determines when each is safe to use.

---

When should you use `git reset` versus `git revert`?
?
Use **git reset** only for **local commits not yet pushed** to shared branches. Resetting rewrites history, which breaks other developers' clones.

Use **git revert** for commits on **shared/remote branches**. Reverting preserves history and doesn't disrupt collaborators who have already fetched the commit.

---

Why is `git revert` safer than `git reset` for shared branches?
?
**Revert** creates a **new commit** that is automatically shared when you push. Other developers can simply pull it.

**Reset** rewrites history, which causes **merge conflicts** for anyone who already has the original commits. They must rebase their work, causing confusion and potential data loss.

---

How do the three `git reset` modes differ in what they preserve?
?
- **`--soft`**: Removes commits but **keeps changes staged** in the index, ready to re-commit
- **`--mixed`** (default): Removes commits and **keeps changes unstaged** in the working directory
- **`--hard`**: **Discards all changes** — working directory becomes exactly as it was at the target commit

---

What happens to your uncommitted work when you run `git reset --hard`?
?
**All uncommitted changes are permanently discarded**. Both staged and unstaged changes are lost because the working directory is reset to match the target commit.

This is why `--hard` requires caution and is often preceded by `git stash` to save work temporarily.

---

What is the practical difference between `git reset --soft HEAD~1` and `git reset HEAD~1`?
?
- **`--soft`**: Removes the last commit but **stages all changes**, letting you modify and recommit
- **Default (`--mixed`)**: Removes the last commit and **unstages changes**, letting you selectively stage and commit parts

---

## Branching Strategies

How does `git merge` differ from `git rebase` when integrating branches?
?
**Merge** creates a **merge commit** that combines two branches, preserving the **complete history** of parallel development and showing both ancestral lines.

**Rebase** **replays commits** from one branch onto another, creating **new commits** with new SHA hashes and a **linear history** without a merge commit.

---

When should you avoid rebasing?
?
Never rebase commits that have been **pushed to shared/remote branches**. Rebasing rewrites history and changes commit SHAs. Teammates who have already fetched those commits will experience merge conflicts and history divergence.

---

How does `git rebase` mechanically rewrite history?
?
1. Find the **common ancestor** of the two branches
2. **Save feature commits as patches** (not yet applied)
3. **Reset the feature branch** to point at the target base (e.g., main's tip)
4. **Replay each patch sequentially**, creating **new commits** with new SHAs but the same changes

---

Why does rebasing create **new commit SHAs** even though the code changes are identical?
?
Because a commit's SHA is a **hash of its entire content**, including the **parent pointer**. Rebasing changes the parent pointer (to a different base commit), so even identical code changes produce different SHA hashes.

---

What is a **fast-forward merge** and when is it possible?
?
A **fast-forward merge** occurs when the target branch has **no new commits** since the source branch diverged. Git simply **moves the target branch pointer forward** along the existing commit chain without creating a merge commit.

Fast-forward is only possible when there's a **direct linear path** from the current branch tip to the source branch tip.

---

When is a **fast-forward merge** impossible?
?
When the target branch has **received new commits** after the source branch diverged, creating **parallel histories**. Git must create a **merge commit** to explicitly combine the two branches.

---

Why use the `--no-ff` flag even when fast-forward is possible?
?
Using `git merge --no-ff` **forces a merge commit** to be created, preserving the **branch topology** in history. This shows that a feature was developed as a coherent unit and makes it easier to identify and revert complete features.

Without `--no-ff`, fast-forward merges obscure the branch structure.

---

How does `git cherry-pick` differ from `git merge`?
?
**Cherry-pick** takes a **single commit** from one branch and **applies its changes** to another, creating a **new commit** with the same changes but a new SHA.

**Merge** combines **entire branches** with all commits intact.

Cherry-pick is selective; merge is comprehensive.

---

When would you use `git cherry-pick` instead of `git merge`?
?
- **Backporting bugfixes** from development to release branches
- **Pulling specific features** without merging the entire branch
- **Recovering commits** from abandoned branches
- **Applying only relevant commits** when you don't want everything from a branch

---

What happens to the original commit after `git cherry-pick`?
?
The **original commit remains unchanged** on its branch. **Cherry-pick creates a new commit** with the same changes but a different SHA. It copies, not moves.

Both commits exist in the repository; neither is deleted.

---

Cherry-pick ==applies specific commits== to the current branch by extracting the diff and creating new commits with the same changes but different SHAs.

---

A **fast-forward merge** moves the branch pointer forward without creating a **merge commit**, which only works when the target branch has no new commits.

---

## Workflow Tools

What problem does `git stash` solve?
?
**Stash** solves the problem of needing to switch branches when you have **uncommitted changes** that don't form a complete commit yet.

You can't switch branches with conflicting local changes, but you don't want to commit half-done work. **Stash saves the work temporarily** without committing.

---

How does stashing differ from committing?
?
**Commits** create permanent history with a message and are shared when you push.

**Stashes** are local, temporary storage in a stack with no message required. They're meant for short-term work-in-progress and aren't pushed to remotes.

---

When should you use `git stash` versus creating a **WIP branch**?
?
**Stash** for truly temporary work (minutes to hours) — context switching to fix a bug, then returning.

Create a **WIP (work-in-progress) branch** for longer-term storage (days or more) — a more durable record of work that can be shared and referenced.

---

How do you view all your stashes?
?
`git stash list` shows all stashes in LIFO (last-in-first-out) order with labels like `stash@{0}`, `stash@{1}`, etc.

---

What is the difference between `git stash pop` and `git stash apply`?
?
- **`pop`**: Restores the stash **and removes it** from the stack
- **`apply`**: Restores the stash **without removing** it, allowing re-application

---

How do you restore a specific stash instead of the most recent?
?
`git stash apply stash@{n}` applies the stash at position n (e.g., `git stash apply stash@{2}`).

---

How does `--force-with-lease` differ from `--force` when pushing?
?
**`--force`** blindly overwrites the remote branch with your local version, **destroying any commits** pushed by teammates since your last fetch.

**`--force-with-lease`** only succeeds if the remote branch matches your **local tracking reference**, catching most cases where teammates have pushed since you last fetched.

---

Why is `--force-with-lease` safer than `--force`?
?
**`--force-with-lease` adds a safety check**: it aborts if the remote branch has changed since your last fetch, preventing you from accidentally destroying a teammate's commits.

**`--force`** has no safety check—it always overwrites, making accidental data loss much more likely.

---

When is a force push necessary?
?
After **rebasing a previously pushed branch** or **amending commits**. These operations rewrite commit history, so a normal push will be rejected. Force push is required to update the remote.

---

What does `--force-with-lease` actually check before pushing?
?
It compares the **remote branch** against your **local tracking reference** (what you last fetched from remote). If they match, push proceeds. If different (teammate pushed since your last fetch), push is rejected.

---

What workflow prevents most force-push conflicts?
?
1. **Fetch from remote** to update your local tracking references
2. **Rebase** your branch onto the latest
3. **Force push** with `--force-with-lease`

This ensures your tracking references are current before pushing.

---

Force push with ==--force-with-lease== checks if the remote branch matches your tracking reference before pushing, preventing accidental overwrite of teammates' commits.

---

**Stashing** saves uncommitted changes to a **temporary stack** without committing, allowing you to switch branches without losing work.

---

## Automation

What are **Git hooks** and what do they enable?
?
**Git hooks** are **scripts that run automatically** at specific points in your Git workflow. They enable automation of tasks like:
- **Pre-commit**: Linting, formatting, running tests before committing
- **Pre-push**: Final validation before pushing to remote
- **Post-receive**: Deployment, notifications on server

---

Where are Git hooks stored and how are they enabled?
?
Hooks are executable scripts stored in the **`.git/hooks/` directory**, named after the event (e.g., `pre-commit`, `pre-push`).

To enable: `chmod +x .git/hooks/pre-commit`

---

What is the key limitation of Git hooks in teams?
?
Hooks in `.git/hooks/` are **not version controlled**—they only exist in your local repository. Each developer must manually set up hooks, so team-wide policy enforcement is inconsistent and cumbersome.

---

How do you version control Git hooks across a team?
?
Use tools like **Husky** (Node.js) or **pre-commit** (Python) that store hook configuration in **version-controlled files** (e.g., `.husky/`, `.pre-commit-config.yaml`).

When developers clone the repository, hooks are automatically set up from the configuration.

---

How does a **pre-commit hook** differ from a **pre-push hook**?
?
- **`pre-commit`**: Runs before commits are created — good for code quality checks (lint, format, basic tests)
- **`pre-push`**: Runs before pushing to remote — good for expensive checks (full test suite, integration tests)

Pre-push prevents bad commits from reaching the remote; pre-commit prevents bad commits locally.

---

What is the difference between **client-side** and **server-side** hooks?
?
**Client-side** hooks run on developers' machines (pre-commit, commit-msg, pre-push) — fast feedback but can be bypassed.

**Server-side** hooks run on the server (pre-receive, post-receive) — enforce policy at the repository level, can't be bypassed.

---

Can you bypass Git hooks if necessary?
?
Yes, using the **`--no-verify`** flag skips hooks:
- `git commit --no-verify`
- `git push --no-verify`

This should be **rare and justified** — document why you're bypassing.

---

Why would a team want to use **server-side hooks** in addition to client-side hooks?
?
**Client-side hooks** provide developer feedback and prevent most mistakes but can be bypassed.

**Server-side hooks** enforce policy at the repository level, preventing anyone (even with `--no-verify`) from violating team standards. This is critical for shared branches and production safety.

---

What is a typical pre-commit hook workflow?
?
1. Developer stages changes
2. Runs `git commit`
3. Pre-commit hook **automatically lints and formats** files
4. If checks fail: commit is **aborted** and errors are shown
5. Developer fixes issues and retries

---

Git hooks are **executable scripts** that run automatically at specific workflow points, enabling automation of ==linting==, ==testing==, and ==policy enforcement==.

---

## Command Reference

### Setup

To configure your Git identity globally: ==git config --global user.name "Name"== and ==git config --global user.email "email@example.com"==

---

To initialize a new Git repository: ==git init==

---

To create a bare repository (for shared server use): ==git init --bare repo.git==

---

### Staging

What command stages a specific file for commit?
?
`git add {file}`

This moves the file from unstaged to staged (ready to commit).

---

To stage all changes: ==git add .==

---

To unstage a specific file (remove from staging): ==git reset HEAD {file}==

---

To unstage all staged files: ==git reset HEAD==

---

How do you view what files are staged before committing?
?
`git status`

Shows which files are staged, unstaged, and untracked.

---

### Commits

To commit staged changes with a message: ==git commit -m "message"==

---

To stage all tracked files and commit in one command: ==git commit -am "message"==

---

To modify the last commit (amend message or add files): ==git commit --amend==

---

What's the difference between `git commit -m` and `git commit --amend`?
?
- **`-m`**: Creates a **new commit** with message
- **`--amend`**: Modifies the **last commit** — adds files or changes message without creating a new commit

---

When should you use `git commit --amend`?
?
Use **`--amend`** when you:
- Forgot to include a file in the last commit
- Made a typo in the commit message
- Want to keep your local history clean

Only amend **before pushing** — amending shared commits breaks other developers' clones.

---

### Undo Commits

To undo the last commit but keep changes staged: ==git reset --soft HEAD~1==

---

To undo the last commit but keep changes unstaged: ==git reset HEAD~1==

---

To undo the last commit and permanently discard changes: ==git reset --hard HEAD~1==

---

What do the three `git reset` modes do?
?
- **`--soft`**: Keeps changes **staged**, ready to recommit
- **`--mixed`** (default): Keeps changes **unstaged** in working directory
- **`--hard`**: **Discards all changes** permanently

Remember: only use `--hard` when certain you want to lose the work.

---

To undo a commit on a shared branch without rewriting history: ==git revert {hash}==

---

### Branches

To create a new branch: ==git branch {name}==

---

To list all local branches: ==git branch==

---

To list remote branches: ==git branch -r==

---

To delete a branch (safe): ==git branch -d {name}==

---

To force-delete a branch: ==git branch -D {name}==

---

To switch to a different branch: ==git checkout {branch}==

---

To create a new branch and switch to it (legacy): ==git checkout -b {branch}==

---

To switch to a branch (modern syntax): ==git switch {branch}==

---

To create and switch to a new branch (modern): ==git switch -c {branch}==

---

What's the difference between `git checkout -b` and `git switch -c`?
?
Both commands do the same thing: **create a branch and switch to it**.

**`git switch -c`** is the **modern, cleaner syntax** (Git 2.23+).

**`git checkout -b`** is the **legacy syntax** (still works, widely used).

Prefer `git switch -c` for new projects.

---

To rename the current branch: ==git branch -m {new}==

---

### Merging

To merge a branch into the current branch: ==git merge {branch}==

---

To force a merge commit even when fast-forward is possible: ==git merge --no-ff {branch}==

---

When should you use `git merge --no-ff`?
?
Use **`--no-ff`** to create a merge commit, which:
- Preserves the **branch topology** in history
- Makes it clear that a **feature was developed together**
- Simplifies reverting entire features with `git revert`

For feature branches, use `--no-ff` to maintain clean history.

---

To cancel a merge in progress: ==git merge --abort==

---

### Rebasing

To rebase the current branch onto another branch: ==git rebase {branch}==

---

To interactively rebase (edit, reorder, squash commits): ==git rebase -i {branch}==

---

To interactively rebase the last 3 commits: ==git rebase -i HEAD~3==

---

What can you do in interactive rebase (`git rebase -i`)?
?
You can:
- **Reorder** commits
- **Squash** commits together
- **Edit** commit messages
- **Drop** commits entirely

Interactive rebase is powerful for cleaning up messy history before merging.

---

To continue after resolving rebase conflicts: ==git rebase --continue==

---

To cancel a rebase in progress: ==git rebase --abort==

---

### Stashing

To save uncommitted changes temporarily: ==git stash==

---

To list all stashes: ==git stash list==

---

To restore the latest stash without removing it: ==git stash apply==

---

To restore and remove the latest stash: ==git stash pop==

---

To restore a specific stash: ==git stash apply stash@{2}==

---

To delete a specific stash: ==git stash drop stash@{2}==

---

What's the difference between `git stash apply` and `git stash pop`?
?
- **`apply`**: Restores the stash but **keeps it** in the stack (can re-apply)
- **`pop`**: Restores the stash and **removes it** from the stack

Use `apply` if you might need the stash again; use `pop` when you're done.

---

### Remote

To list all remote repositories: ==git remote -v==

---

To add a new remote: ==git remote add {name} {url}==

---

To rename a remote: ==git remote rename {old} {new}==

---

To remove a remote: ==git remote remove {name}==

---

To download changes from remote without merging: ==git fetch==

---

To fetch and remove deleted remote branches: ==git fetch -p==

---

To fetch and merge changes from remote: ==git pull origin {branch}==

---

To fetch and rebase (instead of merge) changes: ==git pull --rebase==

---

To push changes to remote: ==git push origin {branch}==

---

To push and set upstream tracking: ==git push -u origin {branch}==

---

To force push (overwrite remote): ==git push --force==

---

To force push safely (only if remote hasn't changed): ==git push --force-with-lease==

---

What's the safest way to force push after rebasing?
?
**Use `git push --force-with-lease`** instead of `--force`.

`--force-with-lease` checks if the remote branch matches your tracking reference. If a teammate pushed since your last fetch, the push is rejected, protecting their work.

Always communicate with your team before force pushing to shared branches.

---

### Tags

To create a lightweight tag: ==git tag {name}==

---

To create an annotated tag with message: ==git tag -a {name} -m "msg"==

---

To tag a specific commit: ==git tag {name} {hash}==

---

To list all tags: ==git tag==

---

To filter tags by pattern: ==git tag -l "v2*"==

---

To list tags with their messages: ==git tag -n==

---

To delete a local tag: ==git tag -d {name}==

---

To push a single tag to remote: ==git push origin <tag>==

---

To push all tags to remote: ==git push origin --tags==

---

What's the difference between lightweight and annotated tags?
?
- **Lightweight tag**: Just a reference to a commit (no metadata)
- **Annotated tag**: Full object with author, date, message (good for releases)

Use **annotated** for version releases; use **lightweight** for quick marks.

---

### History

To view commit history: ==git log==

---

To view commit history in compact form: ==git log --oneline==

---

To view commit history with diffs: ==git log -p==

---

To view history of a specific file: ==git log {file}==

---

To view history of specific line range: ==git log -L 100,150:{file}==

---

To view all HEAD movements (reflog): ==git reflog==

---

When should you use `git reflog`?
?
**`git reflog`** shows all movements of HEAD, not just commits. Use it to:
- **Recover deleted commits** from detached HEAD
- **Find a commit** you lost after a reset
- **Undo a rebase** you regret

It's a safety net for undoing mistakes at the ref level.

---

### Diff

To view unstaged changes: ==git diff==

---

To view staged changes: ==git diff --staged==

---

To view differences between branches: ==git diff <branch1>..<branch2>==

---

To view differences between commits: ==git diff <hash1>..<hash2>==

---

### Inspection

To show repository status: ==git status==

---

To show detailed information about a commit: ==git show {hash}==

---

To show which lines were changed by whom: ==git blame {file}==

---

To show blame for specific line range: ==git blame -L 100,150 {file}==

---

### Cherry-pick

To apply a specific commit to current branch: ==git cherry-pick {hash}==

---

To cherry-pick a range of commits (excludes start): ==git cherry-pick <start>..<end>==

---

To continue cherry-pick after resolving conflicts: ==git cherry-pick --continue==

---

To cancel a cherry-pick in progress: ==git cherry-pick --abort==

---

### Restore

To discard changes in working directory: ==git restore {file}==

---

To restore a file from a specific commit: ==git restore --source={hash} {file}==

---

To discard changes (older syntax): ==git checkout -- {file}==

---

### Interactive Operations

To interactively stage parts of files: ==git add -i==

---

To stage specific changes (patch mode): ==git add -p==

---

To stash specific changes (patch mode): ==git stash -p==

---

To selectively unstage changes: ==git reset -p==

---
