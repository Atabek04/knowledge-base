TARGET DECK: Tech-KB::Research Craft::What Research Is
Tags: research-craft research
**Chapter:** 1. What research is
**Related:** [[Research Craft - MOC]]

---

START
Coding Questions
Booth's definition of research, in one sentence (three parts)?
Back: A **written argument** that something **not previously known** is now known, found out in a way **others can check**.

- Booth, Colomb & Williams, *The Craft of Research* (5th ed.)
Tags: research-craft definition
<!--ID: 1789915781236-->
END

START
Coding Questions
Booth's three-part test for research: what does "written argument" require, and what does it rule out?
Back: A **claim, reasons for it, and evidence** behind the reasons.

- Rules out a **description** of what was done: screenshots, architecture, feature list
- A description claims nothing a reader could disagree with
Tags: research-craft definition
<!--ID: 1789915781238-->
END

START
Coding Questions
Booth's three-part test for research: why is "others can check" the part that makes a finding public rather than private?
Back: Protocol, data and analysis are exposed, so a reader can **rerun the reasoning**.

- The reader trusts the **method**, not the author
- Without it the result is a private belief, not a finding
Tags: research-craft definition
<!--ID: 1789915781239-->
END

START
Coding Questions
Two master's students build the same app and run the same 30-user study. A submits the app with screenshots and a feature list; B submits "spaced repetition cut recall errors 18% vs fixed review" with protocol and data. Why does A fail?
Back: A fails all three parts of Booth's test: **no claim, nothing new, nothing to rerun**.

- Same codebase, but the **artifact is never the contribution**
- The **checkable claim about the artifact** is
Tags: research-craft dissertation
<!--ID: 1789915781240-->
END

START
Coding Questions
Pull-request analogy for Booth's definition of research: what maps to the artifact, the claim, and the check?
Back:
- **Diff** = the artifact
- **PR description** = the claim
- **Tests** = what lets a reviewer verify without trusting the author

A diff with no description or tests is the "we built a system" dissertation.
Tags: research-craft analogy
<!--ID: 1789915781241-->
END

START
Coding Questions
Booth's three roles a research writer can cast the reader in, and which two count as research?
Back:
- **Entertained**: "I found something new and interesting" (not research)
- **Helped**: "I found a solution to a practical problem" (applied research)
- **Educated**: "I found an answer to a question worth asking" (conceptual research)

Only **helped** and **educated** are research; an entertained reader has no reason to act or change their understanding.
Tags: research-craft roles
<!--ID: 1789916424465-->
END

START
Coding Questions
"Here is what I built": which of Booth's reader roles does a pure description cast the reader in, and why is it not even the helping role?
Back: **None** (role zero).

- Helping needs a **claim that the solution works** plus evidence
- A description makes **no claim**, so there is nothing to be helped with, educated about, or entertained by
- This is the "we built a system" report that reviewers reject
Tags: research-craft roles
<!--ID: 1789916424469-->
END

START
Coding Questions
A design-science paper goes to an academic venue. Which of Booth's reader roles does it pick, and what happens if it tries to help and educate equally?
Back: **Educated** only: the reviewer will never install the artifact, so the helping role has no audience.

- The artifact appears only as the **instrument that makes the claim testable**
- Trying both equally → reads as a **product description with a hypothesis attached**
Tags: research-craft roles dissertation
<!--ID: 1789916424471-->
END

START
Coding Questions
Why is "nobody has studied X" never enough on its own to justify a research question?
Back: Because **most unstudied things are unstudied for good reason**.

- A gap is **necessary**, never **sufficient**
- e.g. nobody measured tea vs coffee drinkers' Anki retention: real gap, worthless question
Tags: research-craft question
<!--ID: 1789916921729-->
END

START
Coding Questions
Booth's "so what" test: the three-blank sentence and what the last blank must contain?
Back: "I am studying **___**, because I want to find out **___**, in order to help my reader understand **___**."

- Last blank = a **larger question the field already cares about**
- If it cannot be filled, you have a **topic**, not a research question
Tags: research-craft question
<!--ID: 1789916921731-->
END

START
Coding Questions
What does "unsupervised research" mean in Booth's sense, and why does it matter at master's level?
Back: Nobody **supervises the choice of question**; the student picks it.

- Bachelor: task is handed over, graded on execution
- Master's: the **choice itself is graded**, so a bad question fails good work
Tags: research-craft question
<!--ID: 1789916921734-->
END

START
Coding Questions
Medawar, "Is the scientific paper a fraud?" (1963): in what sense is it a fraud?
Back: Its **form misrepresents the process of thought**, not the results.

- IMRaD implies **induction**: facts gathered, conclusion emerged
- Real discovery (Popper): a **guess first**, then observations chosen to test it
- Nothing reported is false; the **sequence** suggests a method nobody uses
Tags: research-craft medawar
<!--ID: 1789917203522-->
END

START
Coding Questions
If a paper is a reconstruction and not a diary of discovery, what is the reader owed instead?
Back: A **checkable argument**: claim, evidence, reasoning, in the order that lets a stranger rerun it.

- The messy path is honest but **not evidence**
- Write for **checking**, not confession; the discovery order stays in the notebook
Tags: research-craft medawar
<!--ID: 1789917203526-->
END

START
Coding Questions
Where does legitimate reconstruction of a paper end and misconduct begin?
Back: Reordering the argument is fine; **inventing the hypothesis after seeing the data** and presenting it as the original prediction is not.

- A hypothesis may precede the evidence in the paper only if it **preceded it in the work**
- This is why **pre-registration** and protocol papers exist: they fix the guess in public before the data can move it
Tags: research-craft medawar
<!--ID: 1789917203527-->
END

START
Coding Questions
Hamming's two-part definition of an "important problem", and which half people forget?
Back: A problem that **matters** AND on which you hold an **attack** (a plausible route to progress).

- People remember "matters" and forget "attack"
- Time travel matters, nobody has an attack: **big, not important**
Tags: research-craft hamming
<!--ID: 1789917417232-->
END

START
Coding Questions
In Hamming's sense, how does an "attack" differ from a solution?
Back: Nobody starts with a solution; an attack is what makes an **attempt possible**.

- A **theory** that names the lever, an **instrument** that can pull it, a method, data or access others lack
- Hamming had a computer when Bell Labs mostly did not; Shannon had information theory
Tags: research-craft hamming
<!--ID: 1789917417234-->
END

START
Coding Questions
A literature documents motivational decay in gamified courses but never fixes it. What is missing, in Hamming's terms, and what would supply it?
Back: The **attack**. Their route can **measure** decay (course + questionnaire), not **intervene** on its cause.

- Needed: a **theory of why** it decays (names the lever) + an **instrument** where that lever is switchable separately
Tags: research-craft hamming
<!--ID: 1789917417236-->
END

START
Coding Questions
Booth's "so what" test vs Hamming's "attack" test: what does each check, and what happens to a question that passes only the first?
Back:
- **So what**: would the answer matter to the field?
- **Attack**: can you actually get to an answer?

Passes so-what, fails attack → a thesis that **matters and cannot be finished**. Choose at the intersection.
Tags: research-craft hamming question
<!--ID: 1789917417238-->
END
