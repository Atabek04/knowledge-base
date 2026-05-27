---
created: 2026-05-14
tags: [git/workflow, branching-strategy]
aliases: [no-ff, --no-ff, feature bubble]
sr-due:
sr-interval:
sr-ease:
---

# Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert

Vincent Driessen's [2010 Gitflow post](https://nvie.com/posts/a-successful-git-branching-model/) requires `git merge --no-ff` for every feature into `develop`:

> *"It avoids losing information about the historical existence of a feature branch and groups together all commits that together added the feature."*

`--no-ff` forces a merge commit even when [[Fast-forward merge moves branch pointer without creating merge commit|fast-forward]] would work. The resulting topology — a "bubble" off `develop` — has two practical benefits:

1. **Revert a whole feature in one command**: `git revert -m 1 <merge-sha>` undoes every commit on the bubble, since the merge commit has two parents.
2. **Visual grouping**: in `git log --graph`, you see "feature X happened here," not a flat stream of commits.

**Modern critique** ([Stocker, 2020](https://georgestocker.com/2020/03/04/please-stop-recommending-git-flow/)): the `--no-ff` argument predates [[Squash-merge collapses a feature branch into one commit on the target branch|squash-merge]] UIs and CI/CD. If a feature is already squashed to one commit, there is no bubble to preserve — `--no-ff` adds an empty-looking merge commit on top of a squash, which is pure noise.

**Compatibility rule:**
- Want `revert -m 1` semantics → keep `--no-ff`, **don't** squash.
- Want one commit per feature → squash, **don't** also `--no-ff`.
- Mixing both gives the worst of each (extra merge commit *and* lost intermediate history).

nvie himself rejected adding a `--squash` flag to `git flow feature finish` for this reason ([issue #14](https://github.com/nvie/gitflow/issues/14)).

### Read more

- [[Gitflow uses long-lived develop and release branches for scheduled releases]]
- [[Gitflow propagation produces multiple merge commits per feature across develop release and main]]
- [[Squash-merge collapses a feature branch into one commit on the target branch]]
- [[Fast-forward merge moves branch pointer without creating merge commit]]
- [[Git revert creates a new commit that undoes a previous commit]]
- [[Git MOC]]
