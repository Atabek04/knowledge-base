---
created: 2026-05-14
tags: [git/workflow]
aliases: [squash-merge, squash and merge]
sr-due:
sr-interval:
sr-ease:
---

# Squash-merge collapses a feature branch into one commit on the target branch

`git merge --squash <branch>` (or "Squash and merge" in GitHub/GitLab UIs) takes every commit on the source branch and combines them into a **single new commit** on the target.

```bash
git checkout develop
git merge --squash feature/X
git commit -m "Add feature X"
```

The source branch's individual commits do **not** become part of the target's history. The merge is not recorded as a merge commit either — the new commit has one parent (the target tip), making the target's history linear.

**Strengths:**
- One commit per feature → clean, readable log.
- Bisect-friendly: each commit on `develop` represents a full, working feature.
- Hides "WIP", "fix typo", "oops" commits from the permanent record.

**Weaknesses:**
- Loses per-commit history (authorship of individual commits, intermediate diffs).
- Breaks `git revert -m 1` semantics — there is no merge commit and no "bubble" to revert. To undo the feature, revert the single squash commit (which works fine, just different).
- Bad fit for **multi-contributor feature branches** — co-author attribution collapses to one commit.

**Squash vs `--no-ff` in Gitflow:** mutually exclusive choices. See [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert|--no-ff rationale]]. Modern practice (2022–2026): squash at the `feature → develop` boundary is mainstream even in Gitflow shops; `--no-ff` is kept only at release boundaries (`release → main`).

**Recommended hybrid:**
- `feature → develop`: rebase onto develop, then squash-merge.
- `release → main`: `--no-ff` merge with tag (release marker).

### Read more

- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]]
- [[Gitflow propagation produces multiple merge commits per feature across develop release and main]]
- [[Fast-forward merge moves branch pointer without creating merge commit]]
- [[Git rebase rewrites history by replaying commits on a new base]]
- [[First-parent log filters out feature internals to show release-level history]]
- [[Git MOC]]
