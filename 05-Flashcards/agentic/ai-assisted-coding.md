TARGET DECK: Tech-KB::Agentic Engineering::AI-Assisted Coding
Tags: agentic ai-coding
**Chapter:** Skill & Cognition Effects + The Developer's Evolving Role
**Related:** [[Agentic Engineering MOC]]

---

START
Coding Questions
What is "AI slop" in the context of open-source security?
Back: **AI slop** = AI-generated reports that have the *shape* of expertise with none of the substance — confident, detailed vulnerability reports for bugs that **do not exist**.
- Cite fabricated function names, exploit narratives, even fake GDB sessions for code paths not in the project
- Term popularized by curl maintainer Daniel Stenberg and PSF's Seth Larson
Tags: agentic ai-coding
<!--ID: 1782128729529-->
END

START
Coding Questions
What did the curl AI-slop flood do to its bug-bounty numbers (2025–2026)?
Back:
- ~**20%** of all security submissions became AI slop in 2025
- Valid-report rate **collapsed from >15% to below 5%**
- Each report still burned **3–4 people for 30 min to hours** to disprove
- Stenberg: *"We are effectively being DDoSed"* → curl **ended its bug bounty entirely in Jan 2026**
Tags: agentic ai-coding
<!--ID: 1782128729533-->
END

START
Coding Questions
Why is the curl/Larson slop story the load-bearing example of AI danger?
Back: It isolates the failure cleanly — the AI is **not malicious and not lazy**, it is *fluently, specifically, confidently wrong* about whether a bug exists.
- The only defense is a human expert who can read the real code and say "this function isn't real"
- Larson's root cause: *"these systems today cannot understand code"*
Tags: agentic ai-coding
<!--ID: 1782128729535-->
END

START
Coding Questions
Does telling an LLM to "do chain-of-thought / pros-cons / deep analysis" guarantee a correct answer?
Back: **No.** It mainly produces more *convincing-looking* reasoning, not more correct answers.
- CoT can be **post-hoc rationalization** — model decides first, then justifies (unfaithful to real computation)
- Intermediate steps themselves contain factual errors; longer reasoning ≠ more accurate
Tags: agentic ai-coding
<!--ID: 1782128729537-->
END

START
Coding Questions
What is sycophancy and why does "analyze the trade-offs" backfire?
Back: **Sycophancy** = the model is tuned (by RLHF) to agree with the user's stated beliefs.
- A top predictor of a highly-rated response is simply whether it agreed with the user (Sharma et al. 2023)
- So a leading prompt gets reasoning that **rationalizes the conclusion you signaled** rather than challenging it — "reasoning theater"
Tags: agentic ai-coding
<!--ID: 1782128729540-->
END

START
Coding Questions
What is automation bias?
Back: **Automation bias** = the tendency to use automation as a *heuristic replacement* for vigilant checking — once a machine recommends, people take it as correct and stop verifying.
- Driver: **least cognitive effort** (accepting is cheaper than cross-checking)
- Two failure types: **commission** (follow a wrong directive) and **omission** (miss what the machine didn't flag)
Tags: agentic ai-coding
<!--ID: 1782128729546-->
END

START
Coding Questions
What condition makes automation bias *strongest* — and why does that matter for AI code?
Back: **High verification complexity** — opaque output, hard to check, under time pressure (Lyell & Coiera 2017).
- AI code stacks every factor: fluent, plausible, expensive to verify
- That is the exact regime where humans rubber-stamp wrong output
Tags: agentic ai-coding
<!--ID: 1782128729552-->
END

START
Coding Questions
Why does "keep a human in the loop" fail for AI-written code?
Back: The loop only works if the human can **actually evaluate** the output.
- You cannot review what you cannot understand → the reviewer becomes a **rubber stamp**, approving whatever looks plausible
- The safeguard was never the loop — it was the **expertise inside it**
Tags: agentic ai-coding
<!--ID: 1782128729558-->
END

START
Coding Questions
What is "vibe coding" (Karpathy) and where does Willison draw the line?
Back: **Vibe coding** (Karpathy, Feb 2025) = "give in to the vibes... forget the code exists" — *"I 'Accept All' always, I don't read the diffs."*
- Willison's line: *"I won't commit any code I couldn't explain exactly to somebody else"*
- The vibe coder approves code they can't explain → can't verify
Tags: agentic ai-coding
<!--ID: 1782128729563-->
END

START
Coding Questions
Why does the same AI tool make a senior safer but a vibe coder dangerous?
Back: The **asymmetry of what they review against**:
- Senior reviews AI output *against their own model of correct*
- Vibe coder reviews it *against nothing* — to them, broken code reads exactly like correct code
Same tool, opposite outcome.
Tags: agentic ai-coding
<!--ID: 1782128729568-->
END

START
Coding Questions
What is the "70% problem" (Addy Osmani)?
Back: **70% problem** = AI gets you ~70% of the way *fast*, but the **last 30%** (edge cases, integration, security, debugging) is diminishing returns and needs real expertise.
- Non-engineers hit a wall there they can't see past
- "Two steps back": each AI fix breaks something else as misunderstandings cascade
Tags: agentic ai-coding
<!--ID: 1782128729574-->
END

START
Coding Questions
What is "house of cards code" and the "knowledge paradox"?
Back:
- **House of cards code** = output that "looks complete but collapses under real-world pressure" when accepted uncritically
- **Knowledge paradox** = AI helps *seniors more than juniors* (opposite of democratization): seniors accelerate what they know; juniors try to learn what to do and accept output they can't judge
Tags: agentic ai-coding
<!--ID: 1782128729579-->
END

START
Coding Questions
What is the core answer to "will AI replace engineers?" (verification asymmetry)
Back: AI makes **generating** code cheap but not **verifying** it correct — and the two don't scale together.
- Value migrates to the part AI can't be trusted with: judgment
- Willison: *"If you haven't seen it run, it's not a working system"* — accountability stays human
Tags: agentic ai-coding
<!--ID: 1782128729582-->
END

START
Coding Questions
What evidence shows the bottleneck moved to review, not disappeared?
Back: Machine-speed generation pours into human-speed review:
- Faros AI (10k+ devs): PR volume **+98%**, PR review time **+91%**
- Cursor CEO: review takes a growing share of dev time as writing shrinks
- Yegge: the job becomes "agent babysitting"; the skill to build is **"validation and verification"**
Tags: agentic ai-coding
<!--ID: 1782128729587-->
END

START
Coding Questions
What makes a team **AI-native** rather than merely AI-assisted (Liguori's frontier teams)?
Back: An **AI-native** team reshapes its codebase, tools and process so the agent can learn on its own **what to build** and **whether it built it correctly**.
- AI-assisted: human reviews and corrects every turn, so speed is capped by one person's review rate
- AI-native: each habit removes a reason the agent would stop and wait for a person
Tags: agentic ai-coding
<!--ID: 1791030297898-->
END

START
Coding Questions
Frontier-team habit 1 (agent context): which **two questions** keep steering files honest?
Back:
- **On every agent mistake**: "What am I missing in my skills files?" Fix the gap once so it never repeats
- **On every new model release**: "Do I still need this in my skills?" Stronger models no longer need many old "do not" rules
Tags: agentic ai-coding
<!--ID: 1791030297903-->
END

START
Coding Questions
Why must a steering file (`CLAUDE.md`, `AGENTS.md`) be **pruned**, not just grown?
Back: Every line is read on **every task**, so a bloated file makes the agent follow the important lines **less reliably** (context rot applied to instructions).
- Anthropic's test per line: would removing it cause mistakes? If not, cut it
- HumanLayer keeps its root file under 60 lines
Tags: agentic ai-coding
<!--ID: 1791030297906-->
END

START
Coding Questions
Frontier-team habit 2: why is improving **error messages** agent work, with an example?
Back: An error is the agent's **only clue** about what to try next.
- `ERROR: TOO_MANY_RESULTS` → the agent guesses
- "Found 847 expenses, narrow the date range or add a category filter" → the agent applies the fix
Tags: agentic ai-coding
<!--ID: 1791030297909-->
END

START
Coding Questions
Why did frontier teams move from Python/JavaScript toward TypeScript, Rust or Go for agent-written code?
Back: A **strict compiler and type checker** give the agent precise feedback on every edit.
- A loose language lets a wrong guess survive until runtime, where the agent cannot see it
Tags: agentic ai-coding
<!--ID: 1791030297913-->
END

START
Coding Questions
"Feed agents, don't **babysit** them": what must you hand the agent before a task?
Back: **A check it can run that proves the task is done**: a test, build, linter or screenshot.
- **Babysitting** = vibe-coding back-and-forth where the human checks every output
- With a check, the agent self-corrects for hours and several can run in parallel worktrees
Tags: agentic ai-coding
<!--ID: 1791030297915-->
END

START
Coding Questions
Frontier-team habit 4 (make intent explicit): why write a spec before code, and when do you skip it?
Back: **Cost of correction**: fixing a paragraph in a spec takes a minute; arguing with 2,000 lines that misread the requirement takes an afternoon.
- Skip it when the diff fits in **one sentence**: the spec becomes overhead (Kiro turned a one-line bug fix into 4 user stories)
- Trap: nothing forces the code to keep matching the spec once implementation starts
Tags: agentic ai-coding
<!--ID: 1791030297917-->
END

START
Coding Questions
What does **shift testing left** mean for agents, and what three properties must the loop have?
Back: **Shifting left** = moving tests earlier on the timeline, from CI or a human reviewer to the agent's own machine while it writes.
- **Fast**, **local**, **deterministic**: a 10-minute or flaky test teaches the agent nothing
- Mock services let integration tests run without real dependencies
Tags: agentic ai-coding
<!--ID: 1791030297921-->
END

START
Coding Questions
How much should you trust the "4.5x median speedup" from Amazon's frontier teams?
Back: Weakly.
- Amazon's **own** figures, measured as deployment/commit velocity, **no control group**; agents inflate commit counts easily
- Only teams that deliberately changed their process got there; about half stayed under 3x
- The controlled METR trial found experienced devs **19% slower** with early-2025 tools
Tags: agentic ai-coding
<!--ID: 1791030297923-->
END
