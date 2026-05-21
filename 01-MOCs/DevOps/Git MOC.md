---
created: 2025-01-04
tags: [moc]
---

# Git MOC

Distributed version control system for tracking changes in source code.

## Fundamentals

- [[Distributed VCS gives every developer a full repository copy]] — why Git is a DVCS

## History & HEAD

- [[HEAD moves forward with each commit on the current branch]] — what HEAD is
- [[Detached HEAD occurs when HEAD points to a commit instead of a branch]] — detached state
- [[Git tilde selects ancestor depth while caret selects parent number]] — `~` vs `^` notation

## Undoing Changes

- [[Git reset moves the branch pointer backward to remove commits]] — reset basics
- [[Git reset flags soft mixed hard control what gets undone]] — `--soft` / `--mixed` / `--hard`
- [[Git revert creates a new commit that undoes a previous commit]] — safe undo for shared history
- [[Cherry-pick applies specific commits to current branch]] — selective commit application
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits]] — decision guide

## Branching Strategies

- [[Git merge preserves branch history while rebase linearizes it]] — merge vs rebase decision
- [[Git rebase rewrites history by replaying commits on a new base]] — how rebase works
- [[Fast-forward merge moves branch pointer without creating merge commit]] — fast-forward explained

## Branching Models

- [[Gitflow uses long-lived develop and release branches for scheduled releases]] — Gitflow
- [[Trunk-based development keeps a single main branch with short-lived feature branches]] — TBD
- [[Choose Gitflow for versioned releases trunk-based for continuous delivery]] — decision guide
- [[GitLab Flow uses environment branches as sequential deploy stages]] — dev → test → prod model

## Deployment Promotion

- [[Immutable artifact promotion promotes the same build through environments without rebuilding]] — build once, promote artifact (Google/Netflix model)
- [[GitLab Flow uses environment branches as sequential deploy stages]] — merge-based promotion with deploy ledger
- [[Tag-driven promotion deploys by tagging commits rather than merging between environment branches]] — lightweight alternative to environment branches

## History Hygiene

- [[Gitflow propagation produces multiple merge commits per feature across develop release and main]] — why the graph grows noisy
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]] — `--no-ff` rationale and critique
- [[Squash-merge collapses a feature branch into one commit on the target branch]] — squash-merge
- [[First-parent log filters out feature internals to show release-level history]] — `--first-parent` viewing

## Workflow Tools

- [[Git stash temporarily shelves changes without committing]] — context switching
- [[Force push with --force-with-lease prevents overwriting others work]] — safe force push

## Worktrees

- [[Git worktree checks out multiple branches into separate folders sharing one .git]] — what, why, and how
- [[Git worktree enables parallel agentic coding with isolated sub-agent workspaces]] — parallel AI agents

## Automation

- [[Git hooks automate actions at specific points in the workflow]] — pre-commit, pre-push, etc.

## Practice

- [[Git-Flashcards]] — spaced repetition cards

## External Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Documentation](https://git-scm.com/docs)
