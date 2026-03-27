TARGET DECK: Tech-KB::Machine Learning::Data Preprocessing
Tags: ml preprocessing
**Chapter:** Data Preprocessing Workflow
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
Why do we split data into training and testing sets?
Back: To evaluate model performance on **unseen data** and prevent overfitting. Common ratios: 80/20 or 70/30. Always split **before** preprocessing to avoid data leakage.
Tags: ml preprocessing
<!--ID: 1774613880835-->
END

START
Coding Questions
What does `random_state` do and why does the number itself not matter?
Back: It's a seed for the random number generator — same seed always produces the same result. Without it, Python picks a new random seed each run. The actual number (1, 42, 123) is arbitrary — only consistency matters.
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
END

START
Coding Questions
Why can't computers generate truly random numbers, and what do they use instead?
Back: Computers use a **pseudorandom number generator (PRNG)** — a deterministic formula. It takes a starting number (seed), runs math on it, and produces an output. That output becomes input for the next number. Same seed → same math → same sequence every time. Without an explicit seed, Python uses the **system clock** (nanoseconds), which changes constantly — making it *feel* random.
Tags: ml preprocessing
END

START
Coding Questions
Is 42 a special seed number? Why do ML tutorials always use it?
Back: No — 42 has no mathematical advantage. It comes from *The Hitchhiker's Guide to the Galaxy* where it's "the answer to life, the universe, and everything." Programmers adopted it as a convention. Any number (7, 123, 999) works identically — different seeds produce different sequences, but each is equally valid and reproducible. Pick any number and stick with it.
Tags: ml preprocessing
END

START
Coding Questions
Why must missing data be handled before training?
Back: Most ML algorithms **cannot compute with NaN** (will crash or produce garbage). Also, missingness often isn't random, causing biased models. Two strategies: **Delete** rows/columns (when <1-2% missing) or **Impute** with a substitute value.
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
Back: ML algorithms are math — they multiply, sum, and compare numbers. They can't do math on "France" or "Germany". Two methods: **Label encoding** (assign integer) and **One-hot encoding** (binary column per category).
Tags: ml preprocessing
<!--ID: 1774613880842-->
END

START
Coding Questions
How does one-hot encoding work and where does the name come from?
Back: Creates a separate binary (0/1) column for each category. Name from digital electronics — exactly one bit is "hot" (1), rest are "cold" (0). No fake ordering — model treats each category independently.
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
Why should irrelevant or unique columns be dropped before training?
Back: Columns with unique values per row (names, IDs, ticket numbers) **don't generalize** — they memorize individual rows instead of learning patterns. Columns with too many missing values add noise, not signal.
Tags: ml preprocessing
<!--ID: 1774613880848-->
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
Back: Features have different scales (Age: 18-65, Income: $20k-$200k). Gradient descent uses **one learning rate for all features** — same rate is too fast for large features, too slow for small features. Scaling makes all gradients comparable so one learning rate works.
Tags: ml preprocessing
<!--ID: 1774613880851-->
END

START
Coding Questions
What is oscillation in gradient descent and what causes it?
Back: The model bounces above and below the correct answer (like pushing a swing too hard). Caused by large gradients making weight changes too big. Each overshoot is ~60% of previous; converges but wastes iterations. With even larger learning rate, oscillations can **diverge**.
Tags: ml preprocessing
<!--ID: 1774613880853-->
END

START
Coding Questions
What is the difference between normalization and standardization?
Back:
- **Normalization** — scales to [0, 1] range. Formula: (x - x_min) / (x_max - x_min)
- **Standardization** — centers around 0 with std=1. Formula: (x - μ) / σ
- Standardization preferred when data has **outliers** (outliers won't compress rest into tiny range)
Tags: ml preprocessing
<!--ID: 1774613880855-->
END

START
Coding Questions
Why must feature scaling happen after the train-test split?
Back: To prevent **data leakage**. Fit scaler on training data only, then transform both sets. If you scale before splitting, the scaler uses test data statistics — in production you won't have future data. Correct order: split → fit(X_train) → transform(X_train) → transform(X_test).
Tags: ml preprocessing
<!--ID: 1774613880857-->
END
