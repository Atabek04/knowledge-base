---
created: 2026-10-14
tags: [moc]
aliases: [LLMs from scratch, Raschka LLM book]
---

**Book:** Sebastian Raschka, *Build a Large Language Model (From Scratch)*, Manning, 2024. Russian edition: *Строим LLM с нуля*.
**Code:** [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)

Roadmap for building a GPT-style model in PyTorch: text to tokens, attention, the transformer block, pretraining, then fine-tuning for classification and for following instructions.

Each bullet is one teaching topic for the `teach` skill, in the book's prerequisite order.
Start with Appendix A if PyTorch tensors and autograd are new.

**Teaching Progress:** not started.

## 1. Understanding large language models

- [ ] What an LLM is
- [ ] Applications of LLMs
- [ ] Stages of building and using LLMs: pretraining, then fine-tuning
- [ ] The transformer architecture at a glance
- [ ] Why large datasets matter
- [ ] The GPT architecture up close
- [ ] The three-stage plan for building an LLM

## 2. Working with text data

- [ ] Word embeddings: why text must become vectors
- [ ] Tokenizing text
- [ ] Converting tokens into token IDs
- [ ] Special context tokens (unknown word, end of text)
- [ ] Byte pair encoding
- [ ] Data sampling with a sliding window: input and target pairs
- [ ] Token embeddings
- [ ] Encoding word positions: positional embeddings

## 3. Coding attention mechanisms

- [ ] The problem with modeling long sequences
- [ ] Capturing data dependencies with attention
- [ ] Self-attention: attending to different parts of the input
    - [ ] A simple self-attention mechanism without trainable weights
    - [ ] Attention weights for all input tokens
- [ ] Self-attention with trainable weights: query, key and value
    - [ ] Computing attention weights step by step
    - [ ] A compact self-attention class
- [ ] Causal attention: hiding future words
    - [ ] Applying a causal attention mask
    - [ ] Dropout on attention weights
    - [ ] A compact causal attention class
- [ ] Multi-head attention
    - [ ] Stacking single-head attention layers
    - [ ] Multi-head attention with weight splits

## 4. Implementing a GPT model

- [ ] The LLM architecture skeleton
- [ ] Layer normalization
- [ ] Feed forward network with GELU activations
- [ ] Shortcut (residual) connections
- [ ] The transformer block: attention plus linear layers
- [ ] The full GPT model
- [ ] Generating text one token at a time

## 5. Pretraining on unlabeled data

- [ ] Evaluating generative text models
    - [ ] Using GPT to generate text
    - [ ] Text generation loss: cross-entropy and perplexity
    - [ ] Training and validation set losses
- [ ] The training loop
- [ ] Decoding strategies to control randomness
    - [ ] Temperature scaling
    - [ ] Top-k sampling
    - [ ] Modifying the generation function
- [ ] Saving and loading model weights in PyTorch
- [ ] Loading OpenAI's pretrained GPT-2 weights

## 6. Fine-tuning for classification

- [ ] Categories of fine-tuning: classification versus instruction
- [ ] Preparing the dataset
- [ ] Creating data loaders
- [ ] Initializing a model with pretrained weights
- [ ] Adding a classification head
- [ ] Classification loss and accuracy
- [ ] Fine-tuning on supervised data
- [ ] Using the LLM as a spam classifier

## 7. Fine-tuning to follow instructions

- [ ] Instruction fine-tuning
- [ ] Preparing a supervised instruction dataset
- [ ] Organizing data into training batches
- [ ] Data loaders for an instruction dataset
- [ ] Loading a pretrained LLM
- [ ] Fine-tuning on instruction data
- [ ] Extracting and saving responses
- [ ] Evaluating the fine-tuned LLM with another LLM
- [ ] What comes next and how to stay current

## Appendix A. Introduction to PyTorch

- [ ] What PyTorch is: its three core components
- [ ] Defining deep learning
- [ ] Tensors: scalars, vectors, matrices and higher ranks
    - [ ] Tensor data types
    - [ ] Common tensor operations
- [ ] Models as computation graphs
- [ ] Automatic differentiation
- [ ] Multilayer neural networks
- [ ] Efficient data loaders
- [ ] A typical training loop
- [ ] Saving and loading models
- [ ] Training on GPUs
    - [ ] Computations on GPU devices
    - [ ] Single-GPU training
    - [ ] Multi-GPU training

## Appendix D. Training loop extras

- [ ] Learning rate warmup
- [ ] Cosine decay
- [ ] Gradient clipping
- [ ] The modified training function

## Appendix E. Parameter-efficient fine-tuning with LoRA

- [ ] What LoRA is
- [ ] Preparing the dataset
- [ ] Initializing the model
- [ ] Fine-tuning with LoRA

## Bonus material (repo only)

- [ ] BPE tokenizer from scratch
- [ ] Embedding layers versus linear layers
- [ ] Efficient multi-head attention implementations
- [ ] KV cache
- [ ] Attention variants: grouped-query, multi-head latent, sliding window
- [ ] Mixture-of-Experts
- [ ] Converting GPT to Llama
- [ ] Preference tuning with DPO

## Read more

- [[Machine Learning MOC]]
- [[Linear Algebra MOC]]
- [[Math for ML MOC]]
- [[Prompt Engineering for LLMs MOC]]
- [[AI Engineering MOC]]
