---
created: 2026-05-14
tags: [moc]
---

**Roadmaps:** [Vibe Coding](https://roadmap.sh/vibe-coding) · [Claude Code](https://roadmap.sh/claude-code)

Using autonomous LLM agents to write, refactor, and ship code — the **consumer** side of AI in software engineering.

Distinct from [[AI Engineering MOC]], which is about *building* AI-powered products. Here the LLM is your collaborator, not your product.

Different from chat-style prompting: coding agents have a **loop** (observe → think → act → observe), access to **tools** (filesystem, shell, web), and operate over many turns with persistent context.

## Fundamentals

- Agent loop — observe / think / act / repeat
- Tool use — function calling, structured tool schemas
- Context window management — what to include, when to compact
- Permission modes — interactive vs autonomous execution

## Coding Agents & IDEs

- Claude Code
- Cursor
- Windsurf
- Codex
- Replit Agent
- Aider
- Comparison: in-IDE vs CLI vs hybrid

## Project Configuration

- `CLAUDE.md`, `.cursorrules`, `AGENTS.md`
- Skills, hooks, slash commands
- Custom permissions and allowlists
- MCP servers for agent tool extension

## Parallelism & Isolation

- [[Git worktree enables parallel agentic coding with isolated sub-agent workspaces|Git worktree isolates parallel sub-agent workspaces]]
- Sub-agents for research vs. coding (cost trade-offs)
- When parallelism helps vs. when it just burns tokens

## Cost & Efficiency

- Model selection (Opus vs Sonnet vs Haiku)
- Prompt caching, KV cache TTL
- Batching independent tool calls
- Avoiding speculative reads/searches

## Workflow Patterns

- Plan mode vs execute mode
- Code review with agents
- Spec-driven / TDD with agents
- Long-running tasks, background agents
- [[Ralph runs a coding agent in a bash loop with a fresh context each pass and a PRD on disk as the only memory|Ralph loop: fresh agent per pass, PRD pass flags and progress log as memory, stop on COMPLETE]]
    - [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably|Why: compaction breaks long tasks, so the harness loops fresh windows over state on disk]]

## Evaluation & Reliability

- Verifying agent output (trust but verify)
- Detecting hallucinated APIs, files, methods
- When to use plans vs. just execute
- [[AI confidently reports software vulnerabilities that do not exist burying maintainers in slop|AI slop — confident fake vuln reports flooded curl until it killed its bounty]]
- [[Telling an LLM to reason harder can rationalize a wrong answer instead of correcting it|CoT and pros-cons can rationalize a wrong answer, not fix it]]

## Anti-Patterns

- Letting agents amend published commits, force-push, or skip hooks
- Delegating coding to parallel sub-agents without isolation (4–7× cost, no shared context)
- Treating LLM memory as ground truth
- Letting agents run destructive commands without confirmation

## Skill & Cognition Effects

*What heavy AI-assisted coding does to the developer's own skill — the measured evidence, not the hype.*

- [[AI-assisted learners score about two letter grades lower with debugging the most degraded skill|AI-assisted learners score two grades lower — debugging hit worst]]
- [[Experienced developers were measured 19 percent slower with AI while believing they were faster|Devs measured 19% slower with AI yet felt 20% faster]]
- [[AI-native juniors miss the foundational knowledge that came from struggling through problems manually|AI-native juniors miss the foundations the struggle used to build]]
- [[Automation bias makes people accept a machine's recommendation without verifying it|Automation bias — people accept a machine's answer without checking it]]
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|Can't review what you can't understand — oversight becomes rubber-stamping]]

## The Developer's Evolving Role

*Expert opinion (2025-2026) on what the job becomes and who stays valuable when AI writes the code.*

- [[The software engineer's role is shifting from writing code to specifying reviewing and orchestrating it|Role shifts from writing code to specifying, reviewing, orchestrating]]
- [[The Expert Generalist gains value as AI writes more code because fundamentals decomposition and judgment compound|Expert Generalist — fundamentals + judgment compound as AI writes more]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong|AI code is harder to review — clean-looking even when logic is wrong]]
- [[The 70 percent problem means AI delivers the first 70 percent fast but the last 30 percent needs expertise|The 70% problem — AI nails the first 70%, the last 30% needs expertise]]
- [[Verification becomes the scarce engineering skill as AI makes generating code cheap|Verification is the moat — generation is cheap, judging it correct is scarce]]

## Read more

- [[Prompt Engineering MOC]] — the substrate
- [[AI Engineering MOC]] — the producer side (building AI products)
- [[Claude Certifications MOC]] — exam-shaped view over Claude Code and agents
- [[Git worktree checks out multiple branches into separate folders sharing one .git]]
