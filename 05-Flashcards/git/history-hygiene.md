TARGET DECK: Tech-KB::Git::History Hygiene
Tags: git history workflow
**Chapter:** History Hygiene
**Related:** [[Git MOC]]

---

START
Coding Questions
Why does Gitflow produce multiple merge commits per feature?
Back: A feature travels `feature → develop → release → main`, with `release` back-merged into `develop`. Each merge creates a **separate merge commit**.

For one feature:
| Merge | Commit |
|-------|--------|
| `feature/X → develop` | M1 |
| `release/Y → main` | M2 |
| `release/Y → develop` (back-merge) | M3 |

→ **3 merge commits** referencing the same change set.

Content is not duplicated (same trees), but graph topology grows criss-cross merges. Mitigated by squash-merge at `feature → develop` + `--first-parent` viewing.
Tags: gitflow merge-noise
<!--ID: 1780311507993-->
END

START
Coding Questions
Why did Driessen mandate `--no-ff` for feature merges in Gitflow?
Back: From his 2010 post: *"avoids losing information about the historical existence of a feature branch and groups together all commits that together added the feature."*

`--no-ff` forces a merge commit even when fast-forward would work. Benefits:
1. **Revert whole feature in one command** → `git revert -m 1 <merge-sha>`
2. **Visual grouping** → "feature X happened here" bubble in `git log --graph`

**Modern critique:** predates squash-merge UIs. If feature is already squashed to one commit, the bubble is empty noise.
Tags: gitflow no-ff
<!--ID: 1780311508014-->
END

START
Coding Questions
What does squash-merge do?
Back: Combines every commit on the source branch into a **single new commit** on the target.

```bash
git checkout develop
git merge --squash feature/X
git commit -m "Add feature X"
```

- Source's individual commits **don't** join target's history
- New commit has **one parent** (target tip) → linear history, no merge commit
- One commit per feature → clean log, bisect-friendly
- **Loses** per-commit history, breaks `revert -m 1` semantics
- Bad for multi-contributor branches (co-author attribution collapses)
Tags: squash-merge
<!--ID: 1780311508035-->
END

START
Coding Questions
Why are `--no-ff` and squash-merge mutually exclusive in Gitflow?
Back: They optimize for opposite goals.

- `--no-ff` preserves the **feature bubble** → enables `git revert -m 1` and visual grouping
- Squash collapses the bubble to **one commit** with one parent → no bubble exists

Mixing both gives the worst of each: extra merge commit on top of a squash + lost intermediate history.

**Compatibility rule:**
- Want `revert -m 1` semantics → keep `--no-ff`, **don't** squash
- Want one commit per feature → squash, **don't** also `--no-ff`

nvie himself rejected `--squash` in `git flow feature finish` for this reason.
Tags: gitflow no-ff squash-merge
<!--ID: 1780311508056-->
END

START
Coding Questions
What does `git log --first-parent` show?
Back: Follows only the **first parent** of each merge commit, hiding commits merged in from other branches.

```bash
git log --graph --oneline --first-parent main
```

- On `main` → one line per **release marker**
- On `develop` → one line per **feature integration**
- Hides per-commit history of feature branches

**Requires convention:** always merge **into** the long-lived branch, never the other way. Use `--no-ff` for integrations so each is a single first-parent merge commit (not multiple fast-forwarded commits).
Tags: git log first-parent
<!--ID: 1780311508076-->
END

START
Coding Questions
Recommended Gitflow history hygiene policy?
Back: Modern (2022–2026) consensus:

1. **feature → develop**: rebase onto develop, then **squash-merge** → one commit per feature
2. **release → main**: `--no-ff` merge with tag → release marker (semantically meaningful, not noise)
3. **Read** with `git log --graph --first-parent main` → one line per release
4. **Bothered by triple-merge?** → drop `release` branch, stabilize on `develop`, `--ff-only` into `main` at tag

Atlassian, Mergify, DNSimple converge: squash-merge mainstream **even in Gitflow shops**, applied at the `feature → develop` boundary.
Tags: gitflow policy clean-history
<!--ID: 1780311508096-->
END
