---
created: 2026-05-14
tags: [moc]
---

# AI Engineering MOC

Building software **powered by** LLMs — apps, agents, RAG pipelines, MCP servers, multimodal systems.

Different from [[Agentic Engineering MOC]], which is about *using* AI tools to write code. This MOC is about *producing* AI-powered products: you are the developer, the LLM is a runtime dependency.

Distinct from ML Engineering — AI Engineers consume pre-trained models via APIs and fine-tuning; ML Engineers train models from scratch.

## Fundamentals

- What is an AI Engineer
- AI Engineer vs ML Engineer
- AI vs AGI
- How LLMs work
- Tokens, training, inference
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

## Read more

- [[Prompt Engineering MOC]] — substrate underneath all LLM apps
- [[Agentic Engineering MOC]] — using AI tools to code (the consumer side)
- [[Machine Learning MOC]] — training models from scratch
