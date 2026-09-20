---
aliases: [Ralph, Ralph loop, Ralph Wiggum loop]
created: 2026-09-20
---

Ralph is the smallest possible harness, and the clearest illustration of what harness engineering means. Geoffrey Huntley's original "Ralph Wiggum" idea was a one-liner: run a coding agent in a `while true` loop with the same prompt, and let the filesystem and git carry the state. Ryan Carson's [snarktank/ralph](https://github.com/snarktank/ralph) turns that into a script that runs Amp or Claude Code repeatedly until a product spec is fully implemented.

---

### The loop

1. The harness spawns a **new agent instance with a clean context**.
2. The agent reads `prd.json` (user stories, each with `passes: true/false`), `progress.txt` (an append-only log of learnings from earlier passes) and the git history.
3. It picks one incomplete story, implements it, runs typecheck and tests, commits, marks the story passed, appends what it learned to `progress.txt`.
4. The instance exits. The harness checks: all stories passed? If not, back to step 1.
5. When everything passes, the agent prints `<promise>COMPLETE</promise>` and the loop stops.

<mark style="background: #FFF3A3A6;">The only memory between iterations is on disk: the PRD with its pass flags, the progress log, and the commits. Nothing from one context window survives into the next.</mark>

---

### Why the amnesia is the feature

<mark style="background: #ABF7F7A6;">Because every pass starts fresh, the loop never accumulates a degraded window or a lossy summary; each story gets a model at full quality, and the cost of forgetting is paid by re-reading a few small files.</mark> Quality is enforced by the harness, not the model: a story is not done until the checks pass, and the next pass sees the commits, so a bad implementation gets revisited rather than papered over.

<mark style="background: #FF5582A6;">Ralph is only as good as its PRD and its checks: a vague story or a missing test lets the loop mark broken work as passed and move on.</mark> The engineering effort moves into writing small, verifiable stories and a strict done signal.

---

### Read more

- [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably]]
- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Agentic Engineering MOC]]
- [[AI Engineering MOC]]
