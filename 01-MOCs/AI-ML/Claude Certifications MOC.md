---
created: 2026-09-15
tags: [moc]
---

**Official:** [Anthropic Academy](https://anthropic.skilljar.com/) (free courses) · [Prep courses per cert](https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses) · [Pearson VUE registration](https://www.pearsonvue.com/us/en/anthropic.html)

Anthropic's four proctored credentials, the free Academy courses that feed them, and the exam domains each one tests.

Courses are free and give completion badges. Exams are paid, 120 min, 60–63 questions, pass at 720/1000, valid 12 months (on-time renewal free, retake costs full fee).

Consumes [[Agentic Engineering MOC]] (Claude Code, agents) and [[AI Engineering MOC]] (API, RAG, MCP) — this MOC is the exam-shaped view over both.

## Certification ladder

| Cert | Code | Price | Questions | Take it after |
|---|---|---|---|---|
| Associate – Foundations | CCAO-F | $99 | 60 | Associate course block (no coding) |
| Developer – Foundations | CCDV-F | $125 | 60 | Developer course block + one shipped API/MCP project |
| Architect – Foundations | CCAR-F | $125 | 60 (4 of 6 scenarios) | Developer block + Claude Code in Action + Subagents/Skills |
| Architect – Professional | CCAR-P | $175 | 63 | Architect Foundations + a production Claude system end to end |

No cert is a hard prerequisite for another. Recommended order for a backend engineer: **Developer → Architect Foundations → Architect Professional**; Associate is optional (business-user track, best signal-per-dollar is Developer).

## Study resources

- Free exam-shaped curriculum + mock exams: [claudecertificationguide.com](https://claudecertificationguide.com/) (Architect track live; Developer/Associate in progress)
- Community study guide (11 areas, cheat sheet, PDF/EPUB): [daronyondem/claude-architect-exam-guide](https://github.com/daronyondem/claude-architect-exam-guide)
- All four exams, notes per domain: [Amey-Thakur/CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS)
- freeCodeCamp 13 h video prep (Andrew Brown): [article + YouTube link](https://www.freecodecamp.org/news/claude-certified-architect-foundations-prep-for-anthropic-s-new-certification-exam/)
- Study guides with practice tests: [Tutorials Dojo CCAR-F](https://tutorialsdojo.com/ccar-f-claude-certified-architect-foundations-study-guide/) · [CCDV-F](https://tutorialsdojo.com/ccdv-f-claude-certified-developer-foundations-study-guide/) · [CCAO-F](https://tutorialsdojo.com/ccao-f-claude-certified-associate-foundations-study-guide/) · [CCAR-P](https://tutorialsdojo.com/ccar-p-claude-certified-architect-professional-study-guide/)
- Pass report: [How I passed CCA-F (Medium, Jul 2026)](https://medium.com/@kbdhunga/how-i-passed-the-claude-certified-architect-foundations-cca-f-exam-my-experience-and-66bc455aaf23)
- Full prep guide, courses mapped per cert: [cloud-authority.com](https://cloud-authority.com/the-complete-prep-guide-to-anthropic-s-claude-certifications-2026)
- Primary sources the exams are written from: [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) · [MCP spec](https://modelcontextprotocol.io/specification) · [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code) · [Anthropic cookbook](https://github.com/anthropics/anthropic-cookbook)
- No dedicated Discord/Reddit for the certs yet — the MCP GitHub org and r/ClaudeAI are the closest

Study rules from pass reports: take a mock first to find weak domains; build two real projects (an MCP server with structured errors, a Claude Code project with hooks + commands + skills); the exam favours the simplest fix that works.

## Course tracker

Tick when the Academy badge is earned. Order is the reading order — each block assumes the ones above it.

**Associate block (no code)**
- [ ] AI Fluency: Framework & Foundations
- [ ] AI Capabilities and Limitations
- [ ] Claude 101
- [ ] Introduction to Claude Cowork
- [ ] Claude Code 101 (skim)

**Developer block**
- [ ] Claude Platform 101
- [ ] Building with the Claude API (8 h, the spine)
- [ ] Introduction to Model Context Protocol
- [ ] Model Context Protocol: Advanced Topics
- [ ] Introduction to agent skills
- [ ] Introduction to subagents
- [ ] Claude Code 101
- [ ] Claude with Amazon Bedrock *or* Claude on Google Cloud

**Architect Foundations block**
- [ ] Claude Code in Action
- [ ] AI Fluency for Builders

**Architect Professional block**
- [ ] Claude with Amazon Bedrock *and* Claude on Google Cloud
- [ ] Deploying Claude Enterprise with Confidence
- [ ] Partner Basecamp Prework (Claude Partner Network login only)

## Exam progress

- [ ] CCDV-F — Developer Foundations
- [ ] CCAR-F — Architect Foundations
- [ ] CCAR-P — Architect Professional
- [ ] CCAO-F — Associate Foundations (optional)

---

## AI Fluency: Framework & Foundations

- The 4D framework — Delegation, Description, Discernment, Diligence
- Delegation — deciding what to hand to AI vs keep human
- Description — stating product, process and performance expectations
- Discernment — evaluating output, process and the model's behaviour
- Diligence — responsible, transparent, accountable use
- Automation vs augmentation vs agency modes of collaboration

## AI Capabilities and Limitations

- What LLMs are reliably good at vs unreliable at
- Hallucination — why fluent output is not verified output
- Knowledge cutoff and recency gaps
- Reasoning vs retrieval — when the model computes vs recalls
- Non-determinism and why the same prompt varies

## Claude 101

- Claude.ai surfaces — chat, Projects, Artifacts, Cowork, Code
- Model family and when to pick each (Opus / Sonnet / Haiku)
- Projects — knowledge sources and custom instructions
- Extended thinking toggle and what it changes
- Data handling and privacy settings

## Introduction to Claude Cowork

- What Cowork is — Claude acting inside desktop files and apps
- Delegating multi-step office tasks
- Reviewing and approving Cowork's actions

## Claude Platform 101

- Console, workspaces, API keys, usage and rate limits
- Messages API request anatomy — system, messages, max_tokens
- Stateless requests — the client owns conversation history
- Pricing model — input vs output vs cached tokens
- Workbench for prompt iteration

## Building with the Claude API

- Message roles and multi-turn structure
- Stop reasons — end_turn, max_tokens, tool_use, stop_sequence
- Temperature, top-p, top-k and when to touch them
- Streaming responses — server-sent events
- System prompt structure — role, rules, examples, output format
- Few-shot examples and XML tags for structure
- Prefilling the assistant turn to force a format
- Structured output — JSON schema and validation
- Prompt caching — cache breakpoints, TTL, cost math
- Extended thinking — budget tokens, when it helps
- Tool use — defining tool schemas, tool_choice auto/any/named
- Tool result loop — returning results, handling errors
- Files API and document / PDF / image inputs
- RAG — chunking, embeddings, retrieval, contextual retrieval
- Message Batches API — cost and latency trade-off
- Evaluations — building eval sets, model-graded vs code-graded
- Agentic patterns — prompt chaining, routing, parallelisation, orchestrator–worker, evaluator–optimiser
- Workflow vs agent — the taxonomy from Building Effective Agents

## Introduction to Model Context Protocol

- Why MCP exists — the N×M integration problem
- Host / client / server roles
- Tools, resources, prompts — three primitives and who calls them
- Transports — stdio vs streamable HTTP
- Tool descriptions as the model's only interface
- Trust model — what a server can and cannot do

## Model Context Protocol: Advanced Topics

- Sampling — server asking the client's model for completions
- Roots and elicitation
- OAuth authorisation for remote servers
- Sandboxing and permission boundaries
- Building an MCP server with structured error responses

## Introduction to agent skills

- What a skill is — a folder of instructions + scripts loaded on demand
- SKILL.md frontmatter and progressive disclosure
- Skills vs slash commands vs CLAUDE.md
- When to package a workflow as a skill

## Introduction to subagents

- Subagent — separate context window with its own system prompt and tools
- Explicit context passing — the parent must hand over what the child needs
- Cost model — parallel agents multiply tokens
- Research vs coding subagents

## Claude Code 101

- Install, auth, first session
- Permission modes — default, auto-accept, plan
- `~/.claude/` (personal) vs `<project>/.claude/` (team, version-controlled)
- CLAUDE.md as project memory
- Slash commands, `/compact`, `/clear`

## Claude Code in Action

- Hooks — PreToolUse, PostToolUse, Stop; blocking vs advisory
- Custom slash commands
- MCP servers wired into Claude Code
- Headless mode and CI/CD pipelines
- Git worktrees for parallel agents
- Agent SDK — the same loop as a library; sessions, memory, built-in tools
- Multi-agent orchestration with the SDK

## Claude with Amazon Bedrock

- Model IDs and regions on Bedrock
- Converse API vs invoke with the Anthropic SDK
- IAM auth instead of API keys
- Bedrock-specific limits and pricing

## Claude on Google Cloud

- Vertex AI model garden and endpoints
- Auth via service accounts / ADC
- Vertex-specific request shape
- When to pick Bedrock vs Vertex vs direct API

## AI Fluency for Builders

- Applying the 4Ds when the AI is a component, not a chat partner
- Describing tasks for tools and agents, not humans
- Discernment at scale — evals instead of eyeballing

## Deploying Claude Enterprise with Confidence

- The five rollout decisions
- Identity, SSO and data residency
- Usage governance and audit

---

## CCAO-F — Associate Foundations domains

- Prompting and task execution (14%)
- Output evaluation and validation (21%)
- Product and model selection (12%)
- Workflow integration and solution design (16%)
- Configuration and knowledge management (12%)
- Governance, risk and responsible use (15%)
- Troubleshooting and optimisation (10%)

## CCDV-F — Developer Foundations domains

- Agents and workflows (15%)
- Applications and integration (33%) — requirements, life cycle, API mechanics
- Claude Code (3%)
- Eval, testing and debugging (3%)
- Model selection and optimisation (17%) — token and cost management
- Prompt and context engineering (11%)
- Security and safety (8%) — guardrails, hooks, secrets
- Tools and MCPs (11%)

## CCAR-F — Architect Foundations domains

- Agentic architecture and orchestration (27%)
- Claude Code configuration and workflows (20%)
- Prompt engineering and structured output (20%)
- Tool design and MCP integration (18%)
- Context management and reliability (15%)
- The six scenarios — customer support agent, code generation, multi-agent research, developer productivity, Claude Code in CI, structured data extraction

## CCAR-P — Architect Professional domains

- Solution design and architecture (17%)
- Models, prompting and context engineering at scale (13%)
- Integration with enterprise systems and data (19%)
- Evaluation, testing and optimisation (16%)
- Governance, safety and risk management (14%)
- Stakeholder communication and lifecycle management (14%)
- Developer productivity and operational enablement (7%)

## Read more

- [[Agentic Engineering MOC]] — Claude Code, agents, cost, anti-patterns
- [[AI Engineering MOC]] — API, RAG, MCP, evals
- [[Prompt Engineering MOC]]
