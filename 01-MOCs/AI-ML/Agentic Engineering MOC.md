---
created: 2026-05-14
tags: [moc]
---

# Agentic Engineering MOC

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

- [[Git worktree enables parallel agentic coding with isolated sub-agent workspaces]] — one worktree per sub-agent
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

## Read more

- [[Prompt Engineering MOC]] — the substrate
- [[AI Engineering MOC]] — the producer side (building AI products)
- [[Git worktree checks out multiple branches into separate folders sharing one .git]]
