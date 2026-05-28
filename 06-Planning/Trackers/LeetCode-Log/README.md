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

### Add a new problem

Click **New** in the Base (top-right) — it creates the note **right here** in this folder with the columns pre-seeded as empty frontmatter. Just fill them in and rename the note (e.g. `1. Two Sum`). **Status = Cheated** drops it into the "Re-solve Queue" view (re-solve after 3 days — Phase 2 gate).

### Views (open `LeetCode Tracker.base`)

- **All Problems** — grouped by status
- **Re-solve Queue** — `status == Cheated`
- **Not Started** — `status == Not started`
- **Solved (mastery)** — solved-count sum