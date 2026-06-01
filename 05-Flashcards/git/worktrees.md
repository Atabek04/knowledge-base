TARGET DECK: Tech-KB::Git::Worktrees
Tags: git worktree devops
**Chapter:** Git Worktrees
**Related:** [[Git MOC]]

---

START
Coding Questions
What is a Git worktree?
Back: An **additional working directory** linked to the same repository.
- One clone normally = one checkout (one branch on disk)
- `git worktree add <path> <branch>` creates a second folder on a different branch
- All worktrees share the same `.git` object database and refs
- Each worktree has its own index, HEAD, and working files
Tags: git worktree
<!--ID: 1780311507889-->
END

START
Coding Questions
What problem does `git worktree` solve?
Back: The cost of **branch switching**:
- `git checkout` rewrites the working directory → must stash uncommitted work
- IDE re-indexes after every switch
- Build caches (`target/`, `node_modules/`) get invalidated
- Dev servers, debuggers, test watchers must be restarted

Worktree removes the switch entirely — each branch lives in its own folder with its own processes and caches. You `cd` instead of `checkout`.
Tags: git worktree
<!--ID: 1780311507909-->
END

START
Coding Questions
How does a Git worktree work internally?
Back: One shared `.git`, many working trees.
- Main repo's `.git/worktrees/<name>/` holds per-worktree metadata (HEAD, index)
- Linked worktree's `.git` is a **file**, not a folder: `gitdir: /path/to/main/.git/worktrees/<name>`
- Objects and refs are shared → commits/fetches visible everywhere instantly
- A branch can be checked out in **only one** worktree at a time
Tags: git worktree internals
<!--ID: 1780311507930-->
END

START
Coding Questions
Why is `git worktree` valuable for agentic coding with multiple sub-agents?
Back: Agents edit files **directly on disk**. Running multiple agents in one working directory causes collisions:
- Two agents edit the same file → last write wins, work lost
- One runs tests while the other refactors → false failures
- Only one branch can be checked out per directory

**Fix:** one worktree per agent, one branch per worktree.
- Each sub-agent gets an isolated filesystem sandbox
- Independent edits, independent test runs, independent commits → independent PRs
- Still one source of truth for history (shared `.git`)
- Beats cloning the repo N times (wastes disk, fetches don't propagate)
Tags: git worktree agentic-coding ai
<!--ID: 1780311507951-->
END

START
Coding Questions
What are the key `git worktree` commands?
Back:
```bash
git worktree add ../feature-x feature-x   # new worktree on existing branch
git worktree add -b new-branch ../wt main # new worktree + new branch from main
git worktree list                         # show all worktrees
git worktree remove ../feature-x          # clean up folder + metadata
git worktree prune                        # remove stale metadata
```
- Cannot check out the same branch in two worktrees
- Cheap to create — no re-clone, no object copy
Tags: git worktree commands
<!--ID: 1780311507971-->
END
