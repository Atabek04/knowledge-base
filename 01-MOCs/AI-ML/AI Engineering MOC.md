---
created: 2026-05-14
tags: [moc]
---

**Roadmaps:** [AI Engineer](https://roadmap.sh/ai-engineer) · [AI Agents](https://roadmap.sh/ai-agents)

Building software **powered by** LLMs — apps, agents, RAG pipelines, MCP servers, multimodal systems.

Different from [[Agentic Engineering MOC]], which is about *using* AI tools to write code. This MOC is about *producing* AI-powered products: you are the developer, the LLM is a runtime dependency.

Distinct from ML Engineering — AI Engineers consume pre-trained models via APIs and fine-tuning; ML Engineers train models from scratch.

## Fundamentals

- What is an AI Engineer
- AI Engineer vs ML Engineer
- AI vs AGI
- [[LLM training uses next-token prediction on existing text to learn statistical patterns|LLM training: next-token prediction on text]]
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation|Autoregressive prediction: one forward pass, no deliberation]]
- [[Tokenization splits text into subword units to balance vocabulary size and meaning|Tokenization: text into subword units]]
- [[BPE builds a tokenizer vocabulary by iteratively merging the most frequent character pairs|BPE merges frequent char pairs into a vocab]]
- [[Each model trains its own tokenizer on its training corpus producing different token splits|Each model trains its own tokenizer]]
- [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context|Word embeddings: tokens → meaning vectors]]
    - [ ] Embedding lookup: a token id selects one row of a learned vocab × d_model table, no dictionary involved
    - [ ] Static embeddings blend all senses of a word into one vector (word2vec), so "bank" is money and river at once
    - [ ] Contextual embeddings: attention rewrites each token's vector using its neighbours, so "bank" ends up meaning bank-in-this-sentence
    - [ ] NLP eras: symbolic pipelines and WordNet → word2vec static vectors → transformer contextual vectors (BERT, GPT)
- [[Attention allows each token to directly reference any other token regardless of distance|Attention: any token references any other]]
- [[Transformers replaced RNNs by processing all tokens in parallel using attention|Transformers parallelize tokens via attention (vs RNNs)]]
- [[Cross-entropy loss measures probability assigned to the correct token|Cross-entropy loss: probability on the correct token]]
- [[Perplexity measures LLM quality as how many words the model effectively considers at each step|Perplexity: effective branching per step]]
- [[Chain-of-thought prompting uses model output as a working memory scratchpad|Chain-of-thought: output as a scratchpad]]
- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output|Thinking tokens: bounded deliberation scratchpad]]
- [[Inference-time compute scaling trades token cost for accuracy on hard reasoning tasks|Inference-time compute: tokens for accuracy]]
- Roles and responsibilities

## Model Selection

- Closed vs open-source models
- Pre-trained models
- Self-hosted models (Ollama, LM Studio, Hugging Face)
- Choosing the right model for the task
- [[Jev is a System One model that returns typed decisions over a schema instead of generating text|Jev: typed decisions from a schema, not generated text]]

## Model Providers & APIs

- OpenAI (GPT/o-series, Response API)
- Anthropic Claude (Messages API, prompt caching)
- Google Gemini
- Cohere, Mistral, DeepSeek, Meta Llama, Qwen, Gemma
- OpenRouter, OpenAI-compatible APIs
- Hugging Face Hub & Inference SDK

## Inference Controls

- Temperature, top-k, top-p
- Sampling parameters, repetition penalties
- Streaming responses
- Structured output (JSON, schemas)
- Constraining inputs and outputs

## Prompt Engineering

- See [[Prompt Engineering MOC]] for techniques (zero/few-shot, CoT, ReAct, system prompts, role, robust prompting)
- Prompt vs context engineering

## Context Engineering

- Context window management
- Chunking strategies
- Context compaction
- Context isolation
- [[Context engineering curates everything in the window and not the wording of one message|Context engineering: choose what enters the window, prompt wording is one part]]
    - [[Small context windows made single prompts insufficient for multi-step tasks and forced the shift to context engineering|Origin: 4k windows could not hold a multi-step task, so the effort moved to the window]]
- [ ] Context rot: quality degrades as the window fills, so less but relevant beats more
- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront|Just-in-time loading: the model fetches context via tools when a step needs it]]
- [ ] Sub-agent isolation: each worker gets a clean window and returns a summary

## Harness Engineering

The harness is everything wrapped around the model call: the loop, tools, permissions, verification and recovery. Same model, different harness, very different agent.

- [[Harness engineering builds the loop and environment around a fixed model so long tasks finish reliably|Harness engineering: agent = model + harness; loops with fresh context replace one degrading window]]
    - [[Ralph runs a coding agent in a bash loop with a fresh context each pass and a PRD on disk as the only memory|Ralph: the minimal harness, while-true loop, PRD and progress file as the only memory]]
- [ ] The agent loop as a harness: observe → think → act, with the harness deciding what comes back into the window each turn
- [ ] Tool design: descriptions, schemas and error messages are prompt engineering the model reads on every call
- [ ] Verification inside the loop: tests, linters, type checks and hooks give the model ground truth instead of self-judgement
- [ ] Guardrails and permission modes: what the harness refuses or gates regardless of what the model asks
- [ ] Recovery: retries, compaction, checkpoints and hand-off summaries when a run goes long or wrong
- [ ] Skills and instruction files (CLAUDE.md, SKILL.md) as harness-level context loaded on demand
- [ ] Evals of the harness, not the model: same model, A/B the loop and tools

## Embeddings & Vector Databases

- What are embeddings
- Embedding models (OpenAI, Cohere, Gemini, Jina, sentence-transformers)
- Indexing embeddings
- Semantic search, similarity search
- Vector DBs: Pinecone, Chroma, Weaviate, Qdrant, FAISS, LanceDB, MongoDB Atlas, Supabase, pgvector

## RAG (Retrieval-Augmented Generation)

- [[RAG retrieves the documents a question needs at query time so the model reads only those|RAG: index, retrieve the nearest chunks, generate from them]]
- Retrieval process, generation step
- RAG use cases
- RAG with dynamic filters
- RAG vs fine-tuning
- RAGFlow, manual implementation
- [[LLM wiki pattern replaces vector RAG with a maintained markdown knowledge graph|LLM wiki pattern replaces vector RAG with markdown]]

## Fine-Tuning

- When to fine-tune vs RAG vs prompt engineering
- Training basics for AI engineers

## Tool Use & Function Calling

- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront|Tool calling: model requests a function, harness runs it, result re-enters the window]]
- Function calling schemas
- Structured output enforcement
- Constraining tool inputs/outputs

## Agents (as Product)

- AI agents — what and why
- Agent use cases
- Multi-agent systems
- Agent SDKs: Claude Agent SDK, OpenAI AgentKit, Google ADK, Vertex AI Agent Builder
- ReAct pattern, ReAct prompting

## MCP (Model Context Protocol)

- [[MCP is an open standard for plugging tools and data sources into any model|MCP: one open protocol so any host can use any tool server, N + M not N × M]]
- MCP host, client, server
- Transport layer (local vs remote)
- Building an MCP server
- Building an MCP client
- Connecting to local/remote servers

## Frameworks

- LangChain (and LangChain for multimodal)
- LlamaIndex (and LlamaIndex for multimodal)
- Haystack
- transformers.js

## Multimodal

- Multimodal AI overview, use cases
- Image understanding (OpenAI Vision API)
- Image generation (DALL·E API, Nanobanana, Gemini)
- Audio processing
- Speech-to-text (Whisper API)
  - [[HMM-GMM STT models speech as a sequence of hidden phoneme states over acoustic features]] — classical pre-AI pipeline
  - [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours]] — how Whisper works
  - [[Fine-tuning adapts a pretrained Whisper checkpoint to a new domain without training from scratch]] — why fine-tuned beats base
  - [[Hugging Face hosts community fine-tuned Whisper variants for domain-specific transcription]] — where to find better models
- Text-to-speech
- Video understanding

## Safety, Security, Ethics

- AI safety and ethics
- Prompt injection attacks
- [[Jailbreaking crafts prompts that bypass an LLM's safety guardrails|Jailbreaking — prompts that bypass safety guardrails]]
- [[Jailbreak defense layers because input and output filters run outside the model|Jailbreak defense — layer filters outside the model]]
- Adversarial testing
- Bias and fairness
- Content moderation APIs
- Security and privacy concerns
- End-user IDs in prompts
- Data classification
- Know-your-customer use cases
- [[Unfaithful chain-of-thought means visible reasoning traces may not reflect actual model computation|Unfaithful CoT: traces may not reflect computation]]
- [[Black-box AI has caused measurable harm in healthcare, criminal justice, and finance|Black-box AI has caused real-world harm]]
- [[The alignment problem is ensuring AI optimization targets remain consistent with human values as capability scales|Alignment problem: targets stay aligned as capability scales]]
- [[Instrumental convergence means sufficiently capable goal-seeking systems develop self-preservation sub-goals regardless of their original objective|Instrumental convergence: self-preservation sub-goals emerge]]

## Read more

- [[Prompt Engineering MOC]] — substrate underneath all LLM apps
- [[Agentic Engineering MOC]] — using AI tools to code (the consumer side)
- [[Claude Certifications MOC]] — exam-shaped view over API, MCP, agents
- [[Machine Learning MOC]] — training models from scratch
