TARGET DECK: Tech-KB::Machine Learning::Model Training
Tags: ml training
**Chapter:** Model Training Concepts
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
What is a parameter in machine learning?
Back: A **parameter** is a value the model **learns from data** during training to make predictions.
- Divided into **weights** (multiply features) and **biases** (add baseline shift)
- Initially random, adjusted during training, saved and used forever after
Tags: ml training
<!--ID: 1774613880816-->
END

START
Coding Questions
What do weights represent in a model?
Back: A **weight** (w) multiplies a feature to define how much that feature affects the prediction.
- Example: in y = w₁ × sqft + w₂ × bedrooms + b
- If w₁=100 → each square foot adds $100 to the prediction
Tags: ml training
<!--ID: 1774613880818-->
END

START
Coding Questions
What does bias do in a model and what happens without it?
Back: **Bias** (b) adds a baseline shift to **every prediction** regardless of features.
- It's the prediction before considering any features
- Without bias, a house with 0 sqft and 0 bedrooms would cost $0 instead of the land value
Tags: ml training
<!--ID: 1774613880820-->
END

START
Coding Questions
What is a loss function and why does it square errors?
Back: A **loss function** is a formula measuring **how wrong** the model is (lower = better).
- Squaring prevents positive/negative errors from canceling out
- Punishes large errors more heavily
- MSE for regression: MSE = 1/n Σ(yᵢ - ŷᵢ)²
Tags: ml training
<!--ID: 1774613880822-->
END

START
Coding Questions
How does the gradient adjust parameters to reduce loss?
Back: The gradient (derivative of loss) tells the **direction** to nudge each parameter:
- Positive gradient → weight too high → decrease it
- Negative gradient → weight too low → increase it
- Zero gradient → minimum loss — stop
- Update rule: **w_new = w_old - (learning_rate × gradient)**
- Minus sign moves opposite the gradient (toward lower loss)
Tags: ml training
<!--ID: 1774613880824-->
END

START
Coding Questions
What does `.fit()` do in scikit-learn, and what does it learn for LinearRegression vs SimpleImputer vs StandardScaler?
Back:
`.fit()` tells the object: "look at this data and learn what you need."
- **LinearRegression** → learns best weight (slope) and bias (intercept)
- **SimpleImputer** → learns the mean/median of each column
- **StandardScaler** → learns the mean and std of each column
Always fit on **training data only** to prevent data leakage.
Tags: ml training
<!--ID: 1774613880825-->
END

START
Coding Questions
What does `.predict()` do in scikit-learn and what do you pass to it?
Back: `.predict(X_test)` **predicts** targets using the weight and bias learned during `.fit()`.
- You pass **features only** — no targets
- Does **not** return accuracy — compare `y_pred` vs `y_test` using evaluation metrics separately
Tags: ml training
<!--ID: 1774613880827-->
END

START
Coding Questions
Why do neural networks need multiple layers instead of one?
Back: Complex outputs require **hierarchical understanding** — each step depends on the previous one.
- Example: detecting sarcasm requires word meaning → phrase structure → sentence meaning → tone
- No single layer can jump from raw input to high-level output
- Early layers learn concrete patterns (words, syntax); later layers learn abstract ones (intent, tone)
- These divisions emerge automatically from backpropagation — nobody programs them
Tags: ml deep-learning
<!--ID: 1782128730405-->
END

START
Coding Questions
What is a word embedding and how does it encode meaning?
Back: An **embedding** maps each token to a high-dimensional vector (hundreds–thousands of numbers) that encodes meaning.
- Not hand-crafted — learned automatically during training via backpropagation
- Words appearing in similar contexts → similar vectors
- Famous example: `king - man + woman ≈ queen`
- Context changes the vector: `"bank"` near `"river"` ≠ `"bank"` near `"money"` — attention refines it per layer
Tags: ml nlp embeddings
<!--ID: 1782128730408-->
END

START
Coding Questions
What problem did attention solve and how does it work?
Back: **Attention** lets each token directly reference any other token regardless of distance — solving RNN's vanishing memory problem.
- RNNs: sequential, hidden state fades → long-range dependencies lost
- Attention: every token assigns relevance scores to all other tokens simultaneously
- High-score tokens contribute more to updating the current token's embedding
- Example: `"it"` in "The animal was tired" → high score to `"animal"`, low to `"street"`
Tags: ml nlp attention transformer
<!--ID: 1782128730410-->
END

START
Coding Questions
What did the "Attention Is All You Need" paper change?
Back: Introduced the **Transformer** — replaced RNNs entirely with pure attention.
- RNN: sequential (one token at a time), slow, bad long-range memory
- Transformer: parallel (all tokens at once), fast on GPU, direct access to all tokens
- Each layer = self-attention + feed-forward network, stacked N times
- All major LLMs (GPT, Claude, Gemini, Llama) are Transformers
Tags: ml nlp transformer
<!--ID: 1782128730412-->
END

START
Coding Questions
What is a token and why not use whole words?
Back: A **token** is a subword unit — the smallest piece of text an LLM processes.
- Whole words → millions of unrelated tokens, unknown words break the model
- Subwords capture shared meaning: `"un-"`, `"-ing"`, `"-able"` learned once, applied everywhere
- GPT-4 uses ~100k tokens covering English, code, multiple languages efficiently
- Example: `"unbelievable"` → `["un", "believ", "able"]` — 3 tokens
Tags: ml nlp tokenization
<!--ID: 1782128730418-->
END

START
Coding Questions
What is BPE and how does it build a tokenizer vocabulary?
Back: **Byte Pair Encoding (BPE)** builds vocabulary by iteratively merging the most frequent character pairs.
1. Start with individual characters
2. Count all adjacent pairs across training corpus
3. Merge most frequent pair into a new token
4. Repeat until target vocabulary size reached (~100k)
- Common words → single tokens; rare words → split into pieces
- Trained on the model's own corpus → each model tokenizes differently
Tags: ml nlp tokenization
<!--ID: 1782128730420-->
END

START
Coding Questions
Why does GPT-4 tokenize the same sentence differently from Llama 3?
Back: Each model **trains its own tokenizer** on its own corpus using BPE — the tokenizer is not shared.
- Different training data → different frequent pairs → different merges → different splits
- GPT-4: ~100k tokens · Llama 3: ~32k tokens
- Affects: API cost (charged per token), context window usage, generation speed
Tags: ml nlp tokenization
<!--ID: 1782128730423-->
END

START
Coding Questions
What is the core task an LLM learns during training?
Back: **Next-token prediction** — given all tokens before the blank, predict the token that actually came next in the original text.
- Correct answer = whatever word was already there in the training data
- Nobody labels it manually; the text itself provides the targets
- After training, weights are frozen — no training happens during inference
Tags: ml training nlp
<!--ID: 1782128730425-->
END

START
Coding Questions
What does softmax do and why is it needed?
Back: **Softmax** converts raw model scores (logits) into a probability distribution that sums to 100%.
- Raw scores can be any number — softmax makes them all positive and forces sum = 1
- Higher raw score → disproportionately higher probability (amplifies differences)
- Required before cross-entropy loss can be computed
Tags: ml training
<!--ID: 1782128730428-->
END

START
Coding Questions
What is cross-entropy loss and what is its formula?
Back: **Cross-entropy loss** measures how much probability the model assigned to the correct token.
- Formula: `Loss = -log( probability of correct token )`
- High probability for correct token → low loss (good)
- Low probability for correct token → high loss (bad)
- Same gradient descent underneath as regression — just a different loss formula
Tags: ml training nlp
<!--ID: 1782128730430-->
END

START
Coding Questions
What is backpropagation and why does it go "backward"?
Back: **Backpropagation** computes gradients for every weight in a neural network by applying the chain rule backward from the loss.
- Forward pass: input → layer 1 → ... → layer N → loss
- Backprop: loss → layer N → ... → layer 1 (reverse order)
- Goes backward because you must know how later layers contributed before computing earlier layers' gradients
- Same math as gradient descent — just applied through many layers via chain rule
Tags: ml training deep-learning
<!--ID: 1782128730432-->
END

START
Coding Questions
What is perplexity and what values indicate a good LLM?
Back: **Perplexity** (PPL) = `e^(average cross-entropy loss)` — measures how many words the model effectively considers at each prediction step.
- Untrained/random model: PPL ≈ 50,000 (full vocabulary size)
- Poor model: PPL ≈ 33
- GPT-4 level: PPL ≈ 5–15
- Perfect: PPL = 1
- Lower = better: model is more confident in the right answer
Tags: ml nlp
<!--ID: 1782128730434-->
END
