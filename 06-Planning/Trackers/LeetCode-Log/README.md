---
tags: [tracker-docs]
---

### What this is

Personal LeetCode solve-log — the Obsidian replacement for the Notion DB. One note per problem; the table is rendered by `../LeetCode Tracker.base`. Progress is shared with the study buddy **in chat**, not by syncing this folder.

### Schema (frontmatter properties)

The Base shows **every note in this folder** (except this README) — no tag needed.

| Property | Values |
|---|---|
| `link` | LeetCode URL |
| `difficulty` | Easy / Medium / Hard |
| `status` | Solved / Cheated / Piece of cake / Not started |
| `topic` | list, e.g. `[Arrays, Two Pointers]` |
| `solved` | number — how many times solved blind |
| `time_spent` | minutes (optional) |
| `last_solved` | date `YYYY-MM-DD` |

Note body: `### Insight` (one-line key idea) + `### Code` (your Java solution).

### Template

Use `Templates/LeetCode Problem.md` for new notes — problem description, constraints, examples, approach order, and empty Java + Python functions with test cases pre-wired.

### Claude workflow — logging a solved problem

When given a problem to log, Claude should:

1. Accept either a local Educative HTML path (`file:///D:/...`) or a NeetCode/LeetCode URL
2. Read the source to extract: problem name, description, constraints, examples, difficulty, topic(s)
3. Create a note in this folder using `Templates/LeetCode Problem.md` — fill in all extracted fields, write realistic test cases in both Java and Python
4. If `status` was not specified — **ask before creating the note**

### Add a new problem

Click **New** in the Base (top-right) — it creates the note **right here** in this folder with the columns pre-seeded as empty frontmatter. Just fill them in and rename the note (e.g. `1. Two Sum`). **Status = Cheated** drops it into the "Re-solve Queue" view (re-solve after 3 days — Phase 2 gate).

### Views (open `LeetCode Tracker.base`)

- **All Problems** — grouped by status
- **Re-solve Queue** — `status == Cheated`
- **Not Started** — `status == Not started`
- **Solved (mastery)** — solved-count sum