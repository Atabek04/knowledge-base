---
created: 2026-05-14
tags: [moc]
---

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

## Evaluation & Reliability

- Verifying agent output (trust but verify)
- Detecting hallucinated APIs, files, methods
- When to use plans vs. just execute

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

## The Developer's Evolving Role

*Expert opinion (2025-2026) on what the job becomes and who stays valuable when AI writes the code.*

- [[The software engineer's role is shifting from writing code to specifying reviewing and orchestrating it|Role shifts from writing code to specifying, reviewing, orchestrating]]
- [[The Expert Generalist gains value as AI writes more code because fundamentals decomposition and judgment compound|Expert Generalist — fundamentals + judgment compound as AI writes more]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong|AI code is harder to review — clean-looking even when logic is wrong]]

## Read more

- [[Prompt Engineering MOC]] — the substrate
- [[AI Engineering MOC]] — the producer side (building AI products)
- [[Git worktree checks out multiple branches into separate folders sharing one .git]]
