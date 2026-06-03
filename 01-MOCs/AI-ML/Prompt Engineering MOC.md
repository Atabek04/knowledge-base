---
created: 2026-05-14
tags: [moc]
---

Designing inputs to LLMs to get reliable, accurate, and useful outputs.

Prompting is the interface to the model — the same model gives wildly different results depending on instruction clarity, context placement, examples, and output format.

## Fundamentals

- *(empty — add notes as you learn)*

## Core Techniques

- *Zero-shot* — direct instruction, no examples
- *Few-shot* — include 2–5 examples of input/output pairs
- *Chain-of-thought (CoT)* — ask the model to reason step-by-step before answering
- *Role prompting* — set the persona/expertise ("You are a senior security engineer…")
- *Output format constraints* — force JSON, XML, specific schema

## Context Engineering

- Context window limits and what to put where
- Cache-friendly prompt structure (static prefix, dynamic suffix)
- Retrieval-augmented generation (RAG) basics

## Evaluation

- Eval-driven prompt iteration
- Measuring prompt regressions when models change

## Anti-Patterns

- Vague instructions, unstated assumptions
- Burying the actual task under context
- Asking for reasoning *after* the answer

## Read more

- [[AI Engineering MOC]] — building AI-powered products
- [[Agentic Engineering MOC]] — using AI tools to code
- [[Machine Learning MOC]]
