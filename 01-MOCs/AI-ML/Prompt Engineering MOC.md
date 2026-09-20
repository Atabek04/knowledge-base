---
created: 2026-05-14
tags: [moc]
---

**Roadmap:** [Prompt Engineering](https://roadmap.sh/prompt-engineering)

Designing inputs to LLMs to get reliable, accurate, and useful outputs.

Prompting is the interface to the model — the same model gives wildly different results depending on instruction clarity, context placement, examples, and output format.

## Fundamentals

- [ ] Three layers of leverage: prompt engineering (the words) → context engineering (what is in the window) → harness engineering (the loop, tools and checks around the model)
- [[Small context windows made single prompts insufficient for multi-step tasks and forced the shift to context engineering|Why prompts stopped being enough: 4k windows could not hold a multi-step task's state]]
- [[Context engineering curates everything in the window and not the wording of one message|Context engineering: choose what enters the window, prompt wording is one part]]
- [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably|Harness engineering: the loop and checks around the model, prompt and context become its parts]]

## Core Techniques

- *Zero-shot* — direct instruction, no examples
- *Few-shot* — include 2–5 examples of input/output pairs
- *Chain-of-thought (CoT)* — ask the model to reason step-by-step before answering
- *Role prompting* — set the persona/expertise ("You are a senior security engineer…")
- *Output format constraints* — force JSON, XML, specific schema

## Context Engineering

- Context window limits and what to put where
- Cache-friendly prompt structure (static prefix, dynamic suffix)
- [[RAG retrieves the documents a question needs at query time so the model reads only those|RAG: retrieve the relevant slice per question, generate from it]]

## Evaluation

- Eval-driven prompt iteration
- Measuring prompt regressions when models change

## Anti-Patterns

- Vague instructions, unstated assumptions
- Burying the actual task under context
- Asking for reasoning *after* the answer

## Adversarial Prompting

- [[Jailbreaking crafts prompts that bypass an LLM's safety guardrails|Jailbreaking — instruction-following turned against the rules]]
- [[Jailbreak defense layers because input and output filters run outside the model|Jailbreak defense — out-of-model filters survive the bypass]]

## Read more

- [[AI Engineering MOC]] — building AI-powered products
- [[Agentic Engineering MOC]] — using AI tools to code
- [[Machine Learning MOC]]
