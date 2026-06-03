---
created: 2026-05-14
tags: [moc]
---

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

## Embeddings & Vector Databases

- What are embeddings
- Embedding models (OpenAI, Cohere, Gemini, Jina, sentence-transformers)
- Indexing embeddings
- Semantic search, similarity search
- Vector DBs: Pinecone, Chroma, Weaviate, Qdrant, FAISS, LanceDB, MongoDB Atlas, Supabase, pgvector

## RAG (Retrieval-Augmented Generation)

- What is RAG
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

- What is MCP, purpose and functionality
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
- Text-to-speech
- Video understanding

## Safety, Security, Ethics

- AI safety and ethics
- Prompt injection attacks
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
- [[Machine Learning MOC]] — training models from scratch
