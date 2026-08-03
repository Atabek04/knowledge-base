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
In `train_test_split(..., random_state=42)`, what does `random_state` do?
Back: It sets the **seed** for the shuffle that decides which rows go to train vs test → same seed = **same split every run** (reproducible).
- **Without it** → falls back to NumPy's global random number generator (RNG) — one generator shared across the whole `numpy` module — seeded from the system clock → a **different split each run**
Tags: ml preprocessing
<!--ID: 1774613880837-->
END

START
Coding Questions
Besides splitting data, what other ML operations involve randomness that `random_state` controls?
Back: Any step that relies on a random draw — a fixed seed makes each one reproducible.
- **Shuffling** rows before a train/test split
- **Initializing weights** in a model
- **Sampling** rows (e.g. bootstrapping, random subsets in a Random Forest)
Tags: ml preprocessing
<!--ID: 1782414785983-->
END

START
Coding Questions
The model works fine without a fixed `random_state` — so why does it matter?
Back: It matters for **the developer, not the model** — accuracy is fine either way.
- The problem: a different split each run changes your score, so you can't tell if a result came from your code or just a new split
    - e.g. you get 85%, colleague gets 82% on the same code — is it a bug? Can't tell
- A fixed seed buys three things:
    - **Debugging** — reproduce a problem exactly
    - **Fair comparison** — compare model versions on identical splits
    - **Sharing code** — others get your exact results
Tags: ml preprocessing
<!--ID: 1774617459212-->
END

START
Coding Questions
Does the same model give the same accuracy no matter how the data is split?
Back: No — a different split puts different rows in train vs test, so the model trains and is tested on different data → the measured score shifts (e.g. 85% vs 82%).
- The *true* performance is roughly stable; any single split's score just wobbles around it
- That wobble is why you fix the seed — to lock one split and get a reproducible number
Tags: ml preprocessing
<!--ID: 1782455818476-->
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
<!--ID: 1782414568378-->
END

START
Coding Questions
What is a dummy variable and what is the dummy variable trap?
Back:
- **Dummy variable** — binary (0/1) column created by one-hot encoding a category
    - e.g. `Color` (Red/Green/Blue) → 3 columns: `is_Red`, `is_Green`, `is_Blue`
- **Dummy variable trap** — keeping **all** dummy columns makes one column perfectly predictable from the others (**multicollinearity**)
    - e.g. if `is_Red=0` and `is_Green=0`, then `is_Blue` *must* be 1 — the last column adds no new info, it's redundant
- Why it's a problem (why it's a "trap"):
    - redundant column → model can't assign unique weights (infinite weight combos give same prediction)
    - breaks linear models (matrix not invertible) and inflates coefficients, hurting interpretability
- Fix: drop one dummy column → `OneHotEncoder(drop='first')`
    - the dropped category becomes the baseline; no info lost
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
- Caused by **large gradients** (big number from the loss derivative `2·error·x`)
    - large gradient → weight changes too big → overshoot
- Gradient grows with **large error** OR **large feature `x`**
    - big unscaled features inflate the gradient
- **Converge** — overshoots **shrink** each step (~60% of previous)
    - bounces past the answer but reaches it eventually; just wastes iterations
- **Diverge** — with too large a learning rate, overshoots **grow** each step
    - bounces get bigger → loss → ∞ → never finds the answer
- Key: it's the **trend of bounce size** (shrinking vs growing), not bouncing itself, that decides the outcome
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
<!--ID: 1782414568427-->
END

START
Coding Questions
Why is feature scaling done after the train-test split, not before?
Back: To prevent **data leakage** — the model must never see test data, not even indirectly.
- `fit` is the step that **learns** — for any transformer (scaler, imputer, encoder) it captures parameters from whatever data it's given (here: mean/std or min/max)
    - scale *before* splitting → those stats are learned from **test rows too**
    - so test info bleeds into the scaler → into training → over-optimistic scores that won't hold in production
- Fix: fit on training data only, then transform both sets
    - split → fit(X<sub>train</sub>) → transform(X<sub>train</sub>) → transform(X<sub>test</sub>)
Tags: ml preprocessing
<!--ID: 1774613880857-->
END

START
Coding Questions
What is a transformer in scikit-learn, and what are its main categories?
Back: An object that reshapes data through the **`fit`/`transform`** API — `fit(X_train)` learns parameters, `transform(X)` applies them. (A *predictor* uses `predict` instead.)
- **Imputation** — fill missing values
    - `SimpleImputer`, `KNNImputer`
- **Scaling** — rescale feature ranges
    - `StandardScaler`, `MinMaxScaler`
- **Encoding** — categories → numbers
    - `OneHotEncoder`, `OrdinalEncoder`
- **Dimensionality reduction** — fewer features
    - `PCA`
Tags: ml preprocessing
<!--ID: 1782417347427-->
END
