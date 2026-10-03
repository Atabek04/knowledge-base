---
aliases: [five habits of frontier teams, frontier development team, AI-native development habits]
created: 2026-10-03
---

Most teams that adopt a coding agent use it as a faster autocomplete: prompt, read the output, correct it, prompt again. The human stays in every turn, so the team can only go as fast as one person can review.

Clare Liguori (Senior Principal Engineer at AWS, working on Kiro) studied the Amazon teams that broke out of that ceiling and presented the result as five habits at the AI Engineer World's Fair 2026. <mark style="background: #FFF3A3A6;">An AI-native team changes its codebase, tools and process so that the agent can find out on its own what to build and whether it built it correctly, instead of asking a human at every step.</mark>

The five habits are context, investment, autonomy, intent and testing. Each one removes a reason the agent would otherwise stop and wait for a person.

---

### Habit 1: invest in agent context

Knowledge that lives only in an engineer's head (coding standards, why a module is shaped the way it is, which library the team avoids) is invisible to the agent. It gets written into **steering files**: `CLAUDE.md`, `AGENTS.md`, Kiro's `.kiro/steering/`, or on-demand skill files.

Two questions keep the files honest:

- **Every time the agent makes a mistake**: "What am I missing in my skills files?" The mistake is treated as a gap in the context, fixed once, so it never repeats. Mitchell Hashimoto describes the same move as [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably|engineering the harness]].
- **Every time a new model is released**: "Do I still need this in my skills?" A stronger model no longer needs many of the "do not" rules a weaker one did.

<mark style="background: #FF5582A6;">Pruning matters as much as adding, because every line in a steering file is read on every task, and a bloated file makes the agent follow the important lines less reliably.</mark> That is [[Context rot degrades LLM output quality as input length grows, long before the window is full|context rot]] applied to instructions. Anthropic's test for each line: would removing it cause the agent to make mistakes? If not, cut it. HumanLayer keeps its root file under 60 lines.

---

### Habit 2: slow down to speed up

Velocity drops at first, because the team spends time on work that makes the codebase easier for an agent to operate in:

- **Build agent context**: the steering files from Habit 1.
- **Improve error messages**: an error is the agent's only clue about what to try next. `ERROR: TOO_MANY_RESULTS` leads to guessing; "Found 847 expenses, narrow the date range or add a category filter" leads to the fix (Anthropic's example).
- **Build tools and MCP servers**: give the agent a command for anything a human currently does by hand, through [[MCP is an open standard for plugging tools and data sources into any model|MCP]] or a plain CLI.
- **Restructure the codebase**: clear module boundaries and conventions the agent can copy.
- **Change programming language**: <mark style="background: #ABF7F7A6;">a strict compiler and type checker give the agent precise feedback on every edit, while a loose language lets a wrong guess survive until runtime.</mark> Liguori's teams moved from Python and JavaScript toward TypeScript and Rust; Armin Ronacher argues for Go for the same reason.

---

### Habit 3: feed agents, don't babysit them

Babysitting is the back-and-forth vibe-coding loop: the agent writes, the human checks, the human says what is wrong. Feeding means giving the agent what it needs to check itself: a command to compile, run the tests, run the linter, take a screenshot.

<mark style="background: #ADCCFFA6;">Before handing over a task, give the agent a check it can run that proves the task is done.</mark> Anthropic calls this the difference between a session you watch and one you walk away from. With a check in place the agent can run for hours, and several can run in parallel in separate worktrees.

---

### Habit 4: make intent explicit

Before large amounts of code are generated, the design is written as a document the agent works from. The template on Liguori's slide:

```markdown
## Objective
What is the main objective or purpose of the project

## Use Cases
Who are the users and how will they use the feature

## Key Functionality
What are the key elements, style, and design approach required

## Technical Requirements and Design
What specific technical or quality requirements must be met and how
should the feature be implemented
```

The reason is cost: correcting a paragraph in a spec takes a minute, while arguing with 2,000 lines of code that misread the requirement takes an afternoon. Kiro turns this into requirements, a design and a task list; Anthropic's variant has the agent interview you, write `SPEC.md`, and implement it in a fresh session.

A spec is overhead for a small change: if the diff can be described in one sentence, skip it. Critics report Kiro turning a one-line bug fix into four user stories, and nothing forces the code to keep matching the spec once implementation starts.

---

### Habit 5: shift testing left

**Shift left** means moving testing earlier on the timeline, from CI or a human reviewer at the end to the agent's own machine while it is still writing. The checks Liguori lists:

- linters
- mock services, so integration tests run without real dependencies
- unit and integration tests
- performance and security tests

The feedback loop must be fast, local and deterministic: a test that takes ten minutes or fails at random teaches the agent nothing. Writing tests used to be the cost that made teams skip them; with an agent writing them, the return is finally high enough.

---

### What the 4.5x number does and does not show

Across 50+ Amazon Stores teams on existing codebases, the median gain was 4.5x, and some teams went past 10x. Only the teams that deliberately changed how they worked got there; about half the group stayed under 3x.

<mark style="background: #FF5582A6;">The figures are Amazon's own, measured as deployment and commit velocity with no control group, and agents inflate commit counts easily.</mark> The controlled METR study found [[Experienced developers were measured 19 percent slower with AI while believing they were faster|experienced developers 19 percent slower]] with early-2025 tools. And faster code moves the bottleneck rather than removing it: review, decisions and launch approval become the critical path, which is why [[Verification becomes the scarce engineering skill as AI makes generating code cheap|verification becomes the scarce skill]].

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably]]
- [[Context rot degrades LLM output quality as input length grows, long before the window is full]]
- [[MCP is an open standard for plugging tools and data sources into any model]]
- [[Experienced developers were measured 19 percent slower with AI while believing they were faster]]
- [[Verification becomes the scarce engineering skill as AI makes generating code cheap]]
- [[The software engineer's role is shifting from writing code to specifying reviewing and orchestrating it]]
- [[Agentic Engineering MOC]]
- Sources:
    - [Clare Liguori, From AI-Assisted to AI-Native: Building a Frontier Development Team](https://www.youtube.com/watch?v=pqlWNihgdjI)
    - [AWS, How frontier teams are reinventing AI-native development](https://aws.amazon.com/blogs/machine-learning/how-frontier-teams-are-reinventing-ai-native-development/)
    - [Anthropic, Claude Code best practices](https://code.claude.com/docs/en/best-practices)
    - [Anthropic, Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
    - [HumanLayer, Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
    - [Armin Ronacher, Agentic coding recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)
    - [Birgitta Böckeler, Understanding spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
    - [Marmelab, Spec-driven development: the waterfall strikes back](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)
