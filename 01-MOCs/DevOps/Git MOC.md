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

- [[Git reset removes commits while revert creates inverse commits]] — reset vs revert decision

## Branching Strategies

- [[Git merge preserves branch history while rebase linearizes it]] — merge vs rebase decision
- [[Git rebase rewrites history by replaying commits on a new base]] — how rebase works
- [[Fast-forward merge moves branch pointer without creating merge commit]] — fast-forward explained
- [[Cherry-pick applies specific commits to current branch]] — selective commit application

## Workflow Tools

- [[Git stash temporarily shelves changes without committing]] — context switching
- [[Force push with --force-with-lease prevents overwriting others work]] — safe force push

## Automation

- [[Git hooks automate actions at specific points in the workflow]] — pre-commit, pre-push, etc.

## Practice

- [[Git-Flashcards]] — spaced repetition cards

## External Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Documentation](https://git-scm.com/docs)
