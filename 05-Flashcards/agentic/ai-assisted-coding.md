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
In Anthropic's 2026 randomized controlled trial (52 engineers learning the Trio library), how did the AI group do on the mastery quiz?
Back: **50%** for the AI group vs **67%** for hand-coders: about **two letter grades lower**.
- The AI group was **not significantly faster**
- The biggest gap was on **debugging** questions
Tags: agentic ai-coding
<!--ID: 1791019513235-->
END

START
Coding Questions
What is the **supervision paradox** in the Anthropic coding-skill trial?
Back: The skill AI erodes fastest, **debugging**, is the skill you most need to catch AI's mistakes.
- Reviewing machine-written code depends on knowing when and why code fails
- Hand-coders build that by failing and fixing; delegators skip it
Tags: agentic ai-coding
<!--ID: 1791019513248-->
END

START
Coding Questions
Anthropic coding trial: which **three** interaction patterns scored **below 40%**?
Back:
- **AI delegation**: the AI writes the code outright (fastest to finish)
- **Progressive AI reliance**: starts with questions, ends handing over all code
- **Iterative AI debugging**: pastes each error back to the AI instead of understanding it
Tags: agentic ai-coding
<!--ID: 1791019513249-->
END

START
Coding Questions
Anthropic coding trial: which **three** interaction patterns scored **65% or more**?
Back:
- **Conceptual inquiry**: only conceptual questions, fixes every error yourself (also the 2nd fastest)
- **Hybrid code-explanation**: code plus an explanation of it
- **Generation-then-comprehension**: generate, then ask follow-ups until you understand

Key: what separated the groups was **who resolved the errors and built the understanding**, not whether AI was used.
Tags: agentic ai-coding
<!--ID: 1791019513253-->
END

START
Coding Questions
METR 2025: how did experienced open-source developers' **felt** speed compare with their **measured** speed with AI?
Back:
- Predicted beforehand: **24% faster**
- Believed afterwards: **20% faster**
- Measured: **19% slower**

Lesson: your **perception** of AI's speedup is unreliable, so measure it.
Tags: agentic ai-coding
<!--ID: 1791019513254-->
END

START
Coding Questions
What did METR's **2026 rerun** (57 developers, 800+ tasks) find, and why is it still inconclusive?
Back: The sign **flipped**: returning devs ~**18% faster**, new devs ~**4% faster**, but both confidence intervals include zero.
- **Selection bias**: many devs refused to work half their tasks without AI, so the most-helped people opted out and the speedup is likely underestimated
- Neither a slowdown nor a speedup is established for current tools
Tags: agentic ai-coding
<!--ID: 1791019513257-->
END

START
Coding Questions
What did Liu et al. (2026, 1,222 people) find after people used an AI assistant and then lost it?
Back: With AI they scored higher; without it they scored **lower than people who never had it** and **gave up sooner**.
- The effect appeared after only **~10 minutes** of AI use
- Tasks: maths reasoning and reading comprehension
Tags: agentic ai-coding
<!--ID: 1791019513258-->
END

START
Coding Questions
Why can ten minutes of AI help reduce **persistence**, when it is far too short to erase knowledge?
Back: **Persistence** (how long you keep working on a hard problem before quitting) is a separate capacity from knowledge.
- An assistant that answers instantly **conditions an expectation of instant answers**
- So being stuck starts to feel like a reason to quit, not a normal stage of solving
Tags: agentic ai-coding
<!--ID: 1791019513259-->
END

START
Coding Questions
What is **deskilling**, and how does it differ from blocked skill formation?
Back: **Deskilling** = losing a skill you **already had** because a tool regularly does that task for you.
- **Blocked formation**: a **learner** never acquires the skill (Anthropic coding trial)
- **Erosion / deskilling**: an **expert** loses part of an existing skill (Lancet colonoscopy study)
Tags: agentic ai-coding
<!--ID: 1791019513260-->
END

START
Coding Questions
Lancet 2025 colonoscopy study: what happened to experienced endoscopists after 3 months of routine AI use, and why?
Back: Their **unassisted** adenoma detection rate (share of colonoscopies finding a precancerous growth) fell from about **28% to 22%**.
- The AI flagged polyps, so the doctors **stopped practising their own visual search**
- Caveat: observational before/after design, not randomized
Tags: agentic ai-coding
<!--ID: 1791019513261-->
END

START
Coding Questions
Microsoft/CMU survey (CHI 2025, 319 knowledge workers): which two kinds of confidence pull critical thinking in **opposite** directions?
Back:
- **Confidence in the AI** → **less** critical thinking
- **Confidence in yourself** → **more** critical thinking (though reported as more effort)

Why: self-confidence gives you a **standard to check the AI's answer against**; without it, accepting the output is the only option.
Tags: agentic ai-coding
<!--ID: 1791019513262-->
END

START
Coding Questions
According to the Microsoft/CMU survey, critical thinking with AI **moved** in which **three** ways?
Back:
- Gathering information → **verifying** it
- Solving the problem → **integrating** the AI's response
- Executing the task → **stewarding** it (overseeing and taking responsibility for work the AI executed)

Trap: stewardship needs judgment, and judgment is built by the execution it removes.
Tags: agentic ai-coding
<!--ID: 1791019513263-->
END

START
Coding Questions
Bastani et al. (PNAS 2025, ~1,000 maths students): what did a plain chatbot vs a hint-only tutor do to **practice** and **exam** grades?
Back:
- **GPT Base** (plain ChatGPT): practice **+48%**, exam without AI **−17%** vs no-AI control
- **GPT Tutor** (hints, no full solutions): practice **+127%**, exam roughly **at control level**

The guardrail **avoided the loss**; it did not produce an exam gain.
Tags: agentic ai-coding
<!--ID: 1791019513264-->
END

START
Coding Questions
Why is a jump in practice scores with AI **not** evidence of learning?
Back: A practice score taken with AI measures **the student plus the tool**; the exam measures **the student alone**.
- The two can move in **opposite** directions (Bastani: +48% practice, −17% exam)
- Rule: when learning, set the AI to **give hints and withhold full solutions** (Claude Learning mode, ChatGPT Study mode)
Tags: agentic ai-coding
<!--ID: 1791019513265-->
END

START
Coding Questions
What is **cognitive debt** (MIT "Your Brain on ChatGPT", 2025)?
Back: **Cognitive debt** = the accumulated cost of letting a tool do the thinking: effort is **saved during the task** and **paid back later** as weaker memory, understanding and ownership.
- Measured with EEG (electrical brain activity): ChatGPT writers showed the **weakest** neural connectivity, search users middle, brain-only the strongest
- Most ChatGPT writers **could not quote** their own essay minutes later
Tags: agentic ai-coding
<!--ID: 1791019513266-->
END

START
Coding Questions
MIT EEG study: which **order** of writing and AI use preserved recall, and what is the desk rule?
Back: **Unaided first, AI afterwards** beat AI first, then unaided: higher connectivity and better recall.
- Thinking first builds the structure, so the AI edits work the brain **already owns**
- Rule: write the draft, sketch the design or state your hypothesis **before** opening the AI
- Caveat: preprint, 54 people, only 18 in the swap session
Tags: agentic ai-coding
<!--ID: 1791019513267-->
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
