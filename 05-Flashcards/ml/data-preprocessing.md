TARGET DECK: Tech-KB::Machine Learning::Data Preprocessing
Tags: ml preprocessing
**Chapter:** Data Preprocessing Workflow
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
Why do we split data into training and testing sets?
Back: To evaluate model performance on **unseen data** and prevent overfitting.
- Common ratios: 80/20 or 70/30
- Always split **before** preprocessing to avoid data leakage

**Why does unseen data matter?**
If the model trains on data it will later see, it just memorizes answers instead of learning patterns — like a student given the exam questions before the test. You get 100% accuracy in training but fail in real use.
Tags: ml preprocessing
<!--ID: 1774613880835-->
END

START
Coding Questions
What does `random_state` do and why does the number itself not matter?
Back: `random_state` is a **seed** for the random number generator — same seed always produces the same result.
- Without it, Python picks a new random seed each run
- The actual number (1, 42, 123) is arbitrary — only consistency matters
Tags: ml preprocessing
<!--ID: 1774613880837-->
END

START
Coding Questions
The model works fine without a fixed `random_state` — so why does it matter?
Back: It matters for **the developer, not the model**. Without a fixed seed, you can't tell if a change in results came from your code or just a different data split. You get 85% accuracy, your colleague gets 82% on the same code — is there a bug? You can't tell. A fixed seed gives you three things:
- **Debugging** — if there's a problem, you can reproduce it exactly
- **Fair comparison** — you compare model versions on identical data splits
- **Sharing code** — others can run your code and get your exact results
Tags: ml preprocessing
<!--ID: 1774617459212-->
END

START
Coding Questions
Why can't computers generate truly random numbers, and what do they use instead?
Back: Computers use a **pseudorandom number generator (PRNG)** — a deterministic formula, not true randomness.
- Takes a starting number (seed), runs math on it, produces an output
- That output becomes input for the next number
- Same seed → same math → same sequence every time
- Without an explicit seed, Python uses the **system clock** (nanoseconds) — making it *feel* random
Tags: ml preprocessing
<!--ID: 1774617459217-->
END

START
Coding Questions
Is 42 a special seed number? Why do ML tutorials always use it?
Back: No — 42 has no mathematical advantage.
- Comes from *The Hitchhiker's Guide to the Galaxy* — "the answer to life, the universe, and everything"
- Programmers adopted it as a convention
- Any number (7, 123, 999) works identically — different seeds produce different sequences, but each is equally reproducible
- Pick any number and stick with it
Tags: ml preprocessing
<!--ID: 1774617459220-->
END

START
Coding Questions
Why must missing data be handled before training?
Back: Most ML algorithms **cannot compute with NaN** — they'll crash or produce garbage.
- Missingness often isn't random, causing biased models
- Two strategies:
  - **Delete** rows/columns (when <1-2% missing)
  - **Impute** with a substitute value
Tags: ml preprocessing
<!--ID: 1774613880839-->
END

START
Coding Questions
How does sklearn's SimpleImputer work and what is the fit-transform pattern?
Back:
- **fit(data)** — scans data and learns the statistic (mean, median, or mode)
- **transform(data)** — applies learned statistic to replace NaN
- **fit_transform** — both in one call
- Must fit on **training data only**, then transform both train and test separately to avoid data leakage.
Tags: ml preprocessing
<!--ID: 1774613880840-->
END

START
Coding Questions
Why must categorical data be encoded into numbers?
Back: ML algorithms are math — they multiply, sum, and compare numbers. They can't do math on "France" or "Germany".
- **Label encoding** — assign integer to each category
- **One-hot encoding** — binary column per category
Tags: ml preprocessing
<!--ID: 1774613880842-->
END

START
Coding Questions
How does one-hot encoding work and where does the name come from?
Back: **One-hot encoding** creates a separate binary (0/1) column for each category.
- Name from digital electronics — exactly one bit is "hot" (1), rest are "cold" (0)
- No fake ordering — model treats each category independently
Tags: ml preprocessing
<!--ID: 1774613880844-->
END

START
Coding Questions
When should you use label encoding vs one-hot encoding?
Back:
- **Label encoding** — when category has natural order (Small=0, Medium=1, Large=2) or binary target (No=0, Yes=1)
- **One-hot encoding** — when category has no natural order and 3+ values (France, Germany, Spain)
- Problem with label encoding on unordered data: model thinks Germany(1) < Spain(2)
Tags: ml preprocessing
<!--ID: 1774613880846-->
END

START
Coding Questions
What is "signal" in the context of ML data?
Back: **Signal** is the genuine pattern in your data that actually predicts the target.
- It's the real relationship — e.g. income genuinely correlates with loan repayment
- The model **should** learn this
Tags: ml preprocessing
<!--ID: 1774839911109-->
END

START
Coding Questions
What is "noise" in ML data and why is it dangerous?
Back: **Noise** is random variation that has no real predictive power.
- Looks like a pattern in training data, but doesn't hold in new data
- It's statistical accident, not truth
- A model that learns noise instead of signal is **overfitting**
Tags: ml preprocessing
<!--ID: 1774839911111-->
END

START
Coding Questions
How can a mostly-empty column become a source of noise?
Back: The non-empty rows aren't missing randomly — they share some hidden trait (e.g. older customers, enterprise clients).
- The model "learns" that having a value predicts something
- But it's learning **who filled the field**, not the field itself
- This is **spurious correlation** — appears meaningful but won't generalize
Tags: ml preprocessing
<!--ID: 1774839911113-->
END

START
Coding Questions
Why should irrelevant or unique columns be dropped before training?
Back: They inject **noise, not signal** — the model memorizes row-level artifacts instead of learning generalizable patterns.
- **Unique columns** (names, IDs, ticket numbers) — one value per row, no pattern to learn
- **Mostly-empty columns** — non-empty rows aren't random, creating spurious correlations
- **Irrelevant columns** — no causal relationship with target, just statistical accidents
Tags: ml preprocessing
END

START
Coding Questions
What is a dummy variable and what is the dummy variable trap?
Back:
- **Dummy variable** — binary (0/1) column created by one-hot encoding
- **Dummy variable trap** — keeping all dummy columns causes **multicollinearity** (one column perfectly predictable from others)
- Example: if Emb_C=0 and Emb_Q=0, you already know Emb_S=1
- Fix: `OneHotEncoder(drop='first')` to drop one column
Tags: ml preprocessing
<!--ID: 1774613880850-->
END

START
Coding Questions
Why does feature scaling matter for model training?
Back: Features have different scales (Age: 18-65, Income: $20k-$200k).
- Gradient descent uses **one learning rate for all features**
- Same rate is too fast for large features, too slow for small ones
- **Scaling** makes all gradients comparable so one learning rate works
Tags: ml preprocessing
<!--ID: 1774613880851-->
END

START
Coding Questions
What is oscillation in gradient descent and what causes it?
Back: The model **oscillates** — bouncing above and below the correct answer (like pushing a swing too hard).
- Caused by large gradients making weight changes too big
- Each overshoot is ~60% of previous; converges but wastes iterations
- With even larger learning rate, oscillations can **diverge**
Tags: ml preprocessing
<!--ID: 1774613880853-->
END

START
Coding Questions
What are the two main feature scaling techniques?
Back: **Normalization** and **Standardization** — both rescale features so no single feature dominates the model.
- **Normalization** — squeezes values into a fixed [0, 1] range
- **Standardization** — recenters values around 0 with a spread of 1
Tags: ml preprocessing
<!--ID: 1774839911116-->
END

START
Coding Questions
What does the standardization formula (x - μ) / σ actually do, step by step?
Back:
- **μ (mu)** = the **mean** (average) of the feature
- **σ (sigma)** = the **standard deviation** — how spread out the values are from the mean
- **Step 1: (x - μ)** — shifts the data so the mean becomes 0 (centering)
- **Step 2: ÷ σ** — shrinks or stretches so most values fall between -1 and 1
- Result: every feature has mean=0, std=1 — they're on the same scale
Tags: ml preprocessing
<!--ID: 1774839911117-->
END

START
Coding Questions
Why does standardization handle outliers better than normalization?
Back: Normalization uses **min and max**, so one extreme value controls the entire scale.
- Example: ages 20-60, but one person is 120 → range becomes 0-120
- Normal ages (20-60) get compressed into a tiny band (0.17-0.50), losing all detail between them
- **Standardization** uses mean and std — an outlier shifts the mean slightly but doesn't crush the rest into a narrow band
Tags: ml preprocessing
<!--ID: 1774839911119-->
END

START
Coding Questions
What is the difference between normalization and standardization?
Back:
- **Normalization** — scales to [0, 1] range. Formula: (x - x_min) / (x_max - x_min)
- **Standardization** — centers around mean=0 with std=1. Formula: (x - μ) / σ
- Use **normalization** when data has no significant outliers and you want a bounded range
- Use **standardization** when data has **outliers** — it won't let one extreme value crush all other values into a narrow band
Tags: ml preprocessing
END

START
Coding Questions
Why must feature scaling happen after the train-test split?
Back: To prevent **data leakage**.
- Fit scaler on training data only, then transform both sets
- If you scale before splitting, the scaler uses test data statistics — in production you won't have future data
- Correct order: split → fit(X_train) → transform(X_train) → transform(X_test)
Tags: ml preprocessing
<!--ID: 1774613880857-->
END
