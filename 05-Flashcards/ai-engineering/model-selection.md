TARGET DECK: Tech-KB::AI Engineering::Model Selection
Tags: ai-engineering model-selection
**Chapter:** Model Selection
**Related:** [[AI Engineering MOC]]

---

START
Coding Questions
What is a System One model (e.g. TypeSafe's Jev), and how does it differ from an LLM?
Back:
Takes program state plus a **schema of allowed answers**, returns one of those answers with a calibrated probability in a single parallel pass. No tokens generated, so no hallucination or type error is possible; the only failure mode is miscalibration. An LLM composes any string token by token.
Tags: ai-engineering model-selection
<!--ID: 1789918573913-->
END

START
Coding Questions
What are Jev's three question primitives?
Back:
- **Choice**: one option from a set (up to 255)
- **Score**: a position on an ordered scale (2 to 10 levels)
- **Noul**: yes/no as a probability 0 to 1
Tags: ai-engineering model-selection
<!--ID: 1789918573917-->
END

START
Coding Questions
When should you pick a System One model over an LLM, and when not?
Back:
**Rule:** if the acceptable answers can be listed before the call, use System One; if the answer must be composed, use an LLM.
Fits: routing, classification, moderation, scoring, agent step selection. Does not fit: writing, summarising, code gen, chat, open-ended extraction.
Tags: ai-engineering model-selection
<!--ID: 1789918573918-->
END

START
Coding Questions
What does "Jev never hallucinates" actually guarantee?
Back:
Only that the output is always a member of the schema. It says nothing about whether that member is the correct one; wrong-but-valid answers are still possible.
Tags: ai-engineering model-selection
<!--ID: 1789918573919-->
END
