TARGET DECK: Tech-KB::Learning::First Principles
Tags: learning first-principles
**Chapter:** Thinking Methods
**Related:** [[Learning Strategies MOC]]

---

START
Coding Questions
What is **first principles thinking**?
Back: **Breaking** a problem down to its most fundamental, irreducible truths — facts that can't be deduced from anything more basic — then **reasoning upward** from those truths to a solution.
- Aristotle: a first principle is "the first basis from which a thing is known"
- The opposite of copying an existing solution
Tags: learning first-principles
<!--ID: 1782128730177-->
END

START
Coding Questions
How does **reasoning by analogy** differ from first principles thinking?
Back: **Analogy** copies what already works — *"X works for others, so I'll do a version of X."*
- Fast and good enough for routine problems
- But it **inherits every hidden assumption** baked into the thing you copy
- First principles ignores precedent and rebuilds from verifiable facts
Tags: learning first-principles
<!--ID: 1782128730179-->
END

START
Coding Questions
Why can **reasoning by analogy** lead you astray?
Back: Because you adopt the conclusion **without checking the assumptions** behind it.
- You inherit constraints that may not actually apply to your problem
- The "everyone does it this way" answer may rest on outdated or unverified premises
Tags: learning first-principles
<!--ID: 1782128730181-->
END

START
Coding Questions
How does the **SpaceX rocket-cost** example illustrate first principles thinking?
Back: Musk asked what a rocket's **raw materials actually cost** — not what finished rockets sell for.
- The market price was an **analogy**; the material cost was a **first principle**
- Result: rockets could be built at a fraction of market price
- The leverage came from questioning the assumption everyone accepted without checking
Tags: learning first-principles
<!--ID: 1782128730183-->
END

START
Coding Questions
What is the main **cost** of first principles thinking, and when should you use it?
Back: It is **slow** — decomposing a problem to bedrock takes far more effort than copying a working pattern.
- Reserve it for **foundations you'll build on for years**, not every decision
- For routine problems, analogy is the right tool
Tags: learning first-principles
<!--ID: 1782128730186-->
END

START
Coding Questions
What does **Feynman's** "first principle" warn against?
Back: *"You must not fool yourself — and you are the easiest person to fool."*
- Reasoning from fundamentals only works if you're honest about what you've actually verified
- Unchecked assumptions disguised as facts defeat the whole method
Tags: learning first-principles
<!--ID: 1782128730188-->
END

START
Coding Questions
What should you do **before** reaching for a solution, according to the "play with the variables" method?
Back: **Manipulate** the objects in the problem — the variables, inputs, and structures.
- Manipulating them teaches you their **properties**
- The properties point to the solution — you *discover* the method instead of memorizing it
Tags: learning first-principles
<!--ID: 1782128730191-->
END

START
Coding Questions
How can you **discover binary search** from first principles instead of memorizing it?
Back: Start with a sorted array and a target, then **play with the structure**:
- Check the middle element — if it's larger than the target, the target is on the left; if smaller, on the right
- Half the array becomes irrelevant in one step
- Repeating that reconstructs binary search from the array's own property: **sortedness**
Tags: learning first-principles
<!--ID: 1782128730193-->
END

START
Coding Questions
Why is searching **seven days of security footage** the same problem as binary search?
Back: The footage is a **sorted array in disguise**.
- Before the event appears, every frame is a `0`; after it, every frame is a `1`
- So you binary-search the footage: jump to the middle, check which half holds the event, halve again
- Owning the *property* (sortedness) lets you recognize a solved problem wearing a different costume
Tags: learning first-principles
<!--ID: 1782128730196-->
END

START
Coding Questions
Why does a **discovered** solution beat a **memorized** one?
Back: A memorized solution is **brittle** — change the problem slightly and it breaks.
- A discovered solution comes with understanding of *why* it works
- That understanding lets you **adapt** it to variations
Tags: learning first-principles
<!--ID: 1782128730198-->
END

START
Coding Questions
What is the core claim about **first-principles foundations** and learning frameworks?
Back: Time spent mastering fundamentals from first principles is **repaid** every time you learn something built on top of them.
- Once you understand the base layer, frameworks and libraries become "just" specific arrangements of things you already know
- Deep foundations make every higher-level tool easier to learn
Tags: learning first-principles
<!--ID: 1782128730200-->
END

START
Coding Questions
Which **foundations** give the best return when studied from first principles?
Back: The ones that **rarely change**:
- **Formal math** — the language underneath algorithms and ML
- **Algorithms & data structures** — what every framework is built from
- **System design** — how components fit together

Frameworks change constantly; fundamentals don't, so investment there compounds.
Tags: learning first-principles
<!--ID: 1782128730202-->
END

START
Coding Questions
How does the **cooking analogy** explain first-principles learning?
Back: **Ingredients** are the first principles; **recipes** are the frameworks.
- Following recipes one by one teaches only those recipes
- Learning how ingredients taste alone and in combination lets you reconstruct a whole *class* of dishes — and discover new ones
- Master the ingredients and every recipe gets easier
Tags: learning first-principles
<!--ID: 1782128730205-->
END

START
Coding Questions
What is the **career payoff** of building things from scratch?
Back: Engineers who build from scratch **stand out** to hiring managers.
- Writing an emulator or compiler by hand proves you understand the machine, not just an API
- Deep foundations become **long-term confidence** — you trust you can figure out anything new
Tags: learning first-principles
<!--ID: 1782128730208-->
END

START
Coding Questions
What is the **trade-off** of the first-principles, depth-first learning path?
Back: There's **no shortcut** to deep understanding.
- Slower up front, pays off later — the opposite of tutorial-hopping
- Same bet as finishing one resource over switching: **depth over breadth**
Tags: learning first-principles
<!--ID: 1782128730210-->
END
