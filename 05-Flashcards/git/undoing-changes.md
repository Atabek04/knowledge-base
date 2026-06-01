TARGET DECK: Tech-KB::Git::Undoing Changes
Tags: git history undo
**Chapter:** Undoing Changes
**Related:** [[Git MOC]]

---

START
Coding Questions
What does `git reset <commit>` do?
Back: **Moves the current branch pointer** backward to the target commit.
- Commits after the target become unreachable from the branch
- They survive in the reflog (default 90 days), then are garbage collected
- **Rewrites history** → safe locally, dangerous on shared remotes
- What happens to changes depends on the flag (`--soft` / `--mixed` / `--hard`)
Tags: git reset
<!--ID: 1780311508117-->
END

START
Coding Questions
What do the `--soft`, `--mixed`, and `--hard` flags of `git reset` change?
Back: All three move HEAD. They differ in what else they touch:

| Flag | HEAD | Index | Working tree |
|------|------|-------|--------------|
| `--soft` | move | unchanged | unchanged |
| `--mixed` (default) | move | reset | unchanged |
| `--hard` | move | reset | reset |

- `--soft` → uncommit, keep changes **staged**
- `--mixed` → uncommit, **unstage** (files keep edits)
- `--hard` → wipe everything. **Destructive** — uncommitted work gone
Tags: git reset flags
<!--ID: 1780311508139-->
END

START
Coding Questions
What does `git revert <commit>` do?
Back: Creates a **new commit whose diff is the inverse** of the target.
- Original commit stays in history
- Branch moves **forward**, not backward
- Safe on shared branches — no force-push, no diverged collaborators
- For a merge commit, use `-m <parent>` to pick which side to keep:
```bash
git revert -m 1 <merge-sha>
```
Tags: git revert
<!--ID: 1780311508160-->
END

START
Coding Questions
When use `revert` vs `reset` vs `cherry-pick`?
Back: Decision flow:

1. **Commit already pushed/shared?** → `git revert` (never rewrite published history)
2. **Want commit gone from this branch (local)?** → `git reset` (pick flag based on what to keep)
3. **Want commit on a different branch?** → `git cherry-pick` (original stays, copy lands on target)

| Tool | Rewrites history? |
|------|-------------------|
| revert | no |
| reset | yes |
| cherry-pick | no |
Tags: git undo decision
<!--ID: 1780311508181-->
END

START
Coding Questions
Why is `git reset --hard` dangerous?
Back: It wipes the working tree and index back to the target commit.
- Uncommitted changes are **unrecoverable** (not in reflog — reflog tracks commits, not working-tree state)
- The dropped commits themselves can be recovered from reflog within ~90 days
- On a shared branch → forces collaborators to recover from their reflogs
- Prefer `--soft` or `--mixed` unless you specifically want to discard changes
Tags: git reset danger
<!--ID: 1780311508202-->
END

START
Coding Questions
How does cherry-picking a range work?
Back:
```bash
git cherry-pick A..B    # commits after A up to B (excludes A)
git cherry-pick A^..B   # includes A through B
```
- Each commit is applied in order
- On conflict: `git cherry-pick --continue` after resolving, or `--abort` to cancel
- New commits get new SHAs (different parents, different timestamps)
- Original commits remain untouched on their source branch
Tags: git cherry-pick range
<!--ID: 1780311508224-->
END
