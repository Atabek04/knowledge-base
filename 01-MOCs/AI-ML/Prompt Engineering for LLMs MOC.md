---
created: 2026-10-14
tags: [moc]
aliases: [Berryman Ziegler prompt engineering]
---

**Book:** John Berryman and Albert Ziegler, *Prompt Engineering for LLMs*, O'Reilly, 2024. Russian edition: *Промт инжиниринг для LLM*.

Roadmap for building applications on LLMs: how the model sees text, how to fill and assemble a prompt, how to shape the completion, then agents, workflows and evaluation.

Each bullet is one teaching topic for the `teach` skill, in the book's order.

**Teaching Progress:** not started.

## 1. Introduction to prompt engineering

- [ ] Early language models
- [ ] GPT enters the scene
- [ ] What prompt engineering is

## 2. Understanding LLMs

- [ ] An LLM completes a document
- [ ] Human thought versus LLM processing
- [ ] Hallucinations
- [ ] How LLMs see the world: tokens
    - [ ] Tokenizers are deterministic
    - [ ] LLMs cannot slow down and examine letters
    - [ ] Counting tokens
- [ ] One token at a time: auto-regressive models
- [ ] Patterns and repetitions
- [ ] Temperature and probabilities
- [ ] The transformer architecture

## 3. Moving to chat

- [ ] Reinforcement learning from human feedback (RLHF)
    - [ ] Building an RLHF model
    - [ ] Keeping LLMs honest
    - [ ] The alignment tax
- [ ] From instruct models to chat models
- [ ] The chat completion API versus plain completion
- [ ] Moving beyond chat to tools
- [ ] Prompt engineering as playwriting

## 4. Designing LLM applications

- [ ] The loop: user problem, model domain, completion, back to user domain
- [ ] The basic feedforward pass
- [ ] Complexity of the loop
- [ ] Offline versus online evaluation

## 5. Prompt content

- [ ] Sources of content: static versus dynamic
- [ ] Clarifying your question
- [ ] Few-shot prompting
- [ ] Finding dynamic context
- [ ] Retrieval-augmented generation
- [ ] Summarization

## 6. Assembling the prompt

- [ ] Anatomy of the ideal prompt
- [ ] Choosing the document type
    - [ ] The advice conversation
    - [ ] The analytic report
    - [ ] The structured document
- [ ] Formatting snippets and inertness
- [ ] Formatting few-shot examples
- [ ] Elastic snippets
- [ ] Relationships among prompt elements: position, importance, dependency
- [ ] Putting the prompt together

## 7. Taming the model

- [ ] Anatomy of the ideal completion
    - [ ] The preamble
    - [ ] A recognizable start and end
    - [ ] The postscript
- [ ] Logprobs: how good is the completion
- [ ] LLMs for classification
- [ ] Critical points in the prompt
- [ ] Choosing the model

## 8. Conversational agency

- [ ] Tool usage
    - [ ] LLMs trained for tool usage
    - [ ] Guidelines for tool definitions
- [ ] Chain of thought
- [ ] ReAct: iterative reasoning and action
- [ ] Beyond ReAct
- [ ] Context for task-based interactions: sources, selection, organization
- [ ] Building a conversational agent
    - [ ] Managing conversations
    - [ ] User experience

## 9. LLM workflows

- [ ] Would a conversational agent suffice
- [ ] Basic workflows: tasks and assembling them
- [ ] Letting an LLM agent drive the workflow
- [ ] Stateful task agents
- [ ] Roles and delegation

## 10. Evaluating LLM applications

- [ ] What are we even testing
- [ ] Offline evaluation
    - [ ] Example suites
    - [ ] Finding samples
    - [ ] Evaluating solutions
    - [ ] SOMA assessment
- [ ] Online evaluation: A/B testing and metrics

## 11. Looking ahead

- [ ] Multimodality
- [ ] User experience and user interface
- [ ] Intelligence

## Read more

- [[Prompt Engineering MOC]]
- [[Build a Large Language Model From Scratch MOC]]
- [[AI Engineering MOC]]
- [[Agentic Engineering MOC]]
