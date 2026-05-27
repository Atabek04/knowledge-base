---
created: 2026-05-14
tags: [git, worktree, agentic-coding, ai]
aliases: [worktree for agents, parallel agents]
---

Agentic coding tools (Claude Code, Cursor, etc.) edit files directly on disk.

If two agents run in the **same** working directory at the same time, they collide:

- Both edit `UserService.kt` → last write wins, the other agent's work is silently lost
- One agent runs tests while the other is mid-refactor → false failures
- Both try to check out different branches → impossible, only one branch per checkout

<mark style="background: cyan">Git worktree is the clean fix: one worktree per agent, one branch per worktree.</mark>

### Pattern

```bash
git worktree add ../agent-auth     feat/auth-refactor
git worktree add ../agent-payments feat/payments-api
git worktree add ../agent-docs     chore/docs-pass
```

Then launch three agents, each pointed at its own folder. They:

- Edit independent files — no merge conflicts mid-flight
- Run independent test suites in parallel
- Produce independent commits on independent branches
- Open independent PRs

When done, `git worktree remove ../agent-auth` cleans up.

### Why this beats alternatives

- **Cloning the repo three times** → wastes disk, fetches don't propagate, branches don't sync
- **One repo, agents take turns** → serial, defeats the point of running multiple agents
- **Branches without worktrees** → same working directory, same collision problem

<mark style="background: yellow">Worktree gives each sub-agent an isolated filesystem sandbox while keeping one source of truth for history.</mark>

### Read more

- [[Git worktree checks out multiple branches into separate folders sharing one .git]]
- [[Git MOC]]
- [[Agentic Engineering MOC]]
