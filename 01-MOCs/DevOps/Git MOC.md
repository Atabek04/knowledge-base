---
created: 2025-01-04
tags: [moc]
---

Distributed version control system for tracking changes in source code.

## Fundamentals

- [[Distributed VCS gives every developer a full repository copy|Distributed VCS: everyone has a full repo copy]]

## History & HEAD

- [[HEAD moves forward with each commit on the current branch|HEAD moves forward with each commit]]
- [[Detached HEAD occurs when HEAD points to a commit instead of a branch|Detached HEAD: points to a commit, not a branch]]
- [[Git tilde selects ancestor depth while caret selects parent number|~ selects ancestor depth, ^ selects parent]]

## Undoing Changes

- [[Git reset moves the branch pointer backward to remove commits|reset moves the branch pointer back]]
- [[Git reset flags soft mixed hard control what gets undone|reset --soft / --mixed / --hard: what gets undone]]
- [[Git revert creates a new commit that undoes a previous commit|revert: a new commit that undoes another]]
- [[Cherry-pick applies specific commits to current branch|cherry-pick applies specific commits here]]
- [[Choose revert for shared history reset for local cleanup cherry-pick to port commits|revert (shared) vs reset (local) vs cherry-pick (port)]]

## Branching Strategies

- [[Git merge preserves branch history while rebase linearizes it|merge preserves history; rebase linearizes it]]
- [[Git rebase rewrites history by replaying commits on a new base|rebase replays commits on a new base]]
- [[Fast-forward merge moves branch pointer without creating merge commit|Fast-forward merge: no merge commit]]

## Branching Models

- [[Gitflow uses long-lived develop and release branches for scheduled releases|Gitflow: long-lived develop/release branches]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches|Trunk-based: one main, short-lived branches]]
- [[Choose Gitflow for versioned releases trunk-based for continuous delivery|Gitflow for versioned releases, TBD for CD]]
- [[GitLab Flow uses environment branches as sequential deploy stages|GitLab Flow: environment branches as deploy stages]]

## Deployment Promotion

- [[Immutable artifact promotion promotes the same build through environments without rebuilding|Immutable artifact promotion: build once, promote]]
- [[GitLab Flow uses environment branches as sequential deploy stages|GitLab Flow promotion: merge through env branches]]
- [[Tag-driven promotion deploys by tagging commits rather than merging between environment branches|Tag-driven promotion: deploy by tagging, not merging]]

## History Hygiene

- [[Gitflow propagation produces multiple merge commits per feature across develop release and main|Gitflow propagation: many merge commits per feature]]
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert|Gitflow --no-ff preserves the feature bubble]]
- [[Squash-merge collapses a feature branch into one commit on the target branch|Squash-merge: feature branch → one commit]]
- [[First-parent log filters out feature internals to show release-level history|--first-parent log shows release-level history]]

## Workflow Tools

- [[Git stash temporarily shelves changes without committing|stash shelves changes without committing]]
- [[Force push with --force-with-lease prevents overwriting others work|--force-with-lease: safe force push]]

## Worktrees

- [[Git worktree checks out multiple branches into separate folders sharing one .git|worktree: many branches in separate folders, one .git]]
- [[Git worktree enables parallel agentic coding with isolated sub-agent workspaces|worktree isolates parallel sub-agent workspaces]]

## Automation

- [[Git hooks automate actions at specific points in the workflow|Git hooks: pre-commit, pre-push, etc.]]

## Practice

- [[Git-Flashcards]] — spaced repetition cards

## External Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Documentation](https://git-scm.com/docs)
