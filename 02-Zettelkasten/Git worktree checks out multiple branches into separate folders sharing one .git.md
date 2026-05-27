---
created: 2026-05-14
tags: [git, worktree, devops]
aliases: [worktree, git worktree]
---

A **Git worktree** is an additional working directory linked to the same repository, checked out on a different branch.

One clone gives you one checkout by default — only one branch visible on disk.
`git worktree add` lets you check out another branch into a separate folder, while sharing the same underlying object database and refs.

### Why it exists

`git checkout` rewrites the working directory, which is expensive in practice:

- Uncommitted changes block the switch → forces a stash or junk commit
- IDE re-indexes the whole project
- Build artifacts (`target/`, `node_modules/`, `.gradle/`) get invalidated
- Dev servers, debuggers, test watchers must be restarted

Worktrees remove the switch: each branch lives in its own folder with its own processes and caches. You `cd` instead of `checkout`.

### Layout

```
my-repo/                  ← main worktree
├── .git/                 ← real .git (objects, refs, config)
│   └── worktrees/
│       ├── feature-x/    ← metadata for linked worktree
│       └── bugfix-42/
│
../feature-x/             ← linked worktree
│   └── .git              ← FILE, not folder: "gitdir: …/worktrees/feature-x"
│
../bugfix-42/
    └── .git              ← same — a pointer file
```

Objects and refs are shared → commits, fetches, and new branches are visible from every worktree instantly.

### Rules and commands

```bash
git worktree add ../feature-x feature-x        # existing branch
git worktree add -b new-branch ../wt main      # new branch from main
git worktree list
git worktree remove ../feature-x
git worktree prune                             # drop stale metadata
```

A branch can be checked out in **only one** worktree at a time — Git refuses to check out the same branch twice. Worktrees are cheap: no re-clone, no duplicated objects, just a new index and working tree.

### Read more

- [[Git worktree enables parallel agentic coding with isolated sub-agent workspaces]]
- [[Git stash temporarily shelves changes without committing]]
- [[Git MOC]]
