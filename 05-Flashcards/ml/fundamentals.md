TARGET DECK: Tech-KB::Machine Learning::Fundamentals
Tags: ml fundamentals
**Chapter:** Overview + Core Vocabulary
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
How do AI, ML, Deep Learning, and GenAI relate to each other?
Back:
- **AI** — broadest term: systems that imitate human intelligence
- **ML** — subset of AI: systems learn patterns from data instead of hard-coded rules
- **DL** — subset of ML: uses neural networks with many layers for complex patterns
- **GenAI** — AI systems (usually DL-based) that create new content (text, images, music)
Tags: ml fundamentals
<!--ID: 1774613880859-->
END

START
Coding Questions
What are the three main types of machine learning?
Back:
- **Supervised** — learns from labeled data (input + correct answer)
- **Unsupervised** — finds hidden patterns in unlabeled data (no correct answers)
- **Reinforcement** — learns via trial-and-error with rewards and penalties
Tags: ml fundamentals
<!--ID: 1774613880860-->
END

START
Coding Questions
What are the five stages every ML project follows?
Back:
1. **Problem Framing** — define objective, determine if ML is needed
2. **Data Preparation** — collection, cleaning, feature engineering, splitting
3. **Modeling** — selection, training, hyperparameter tuning
4. **Evaluation** — metrics, validation, compare with baseline
5. **Deployment & Monitoring** — production integration, performance monitoring
Tags: ml fundamentals
<!--ID: 1774613880862-->
END

START
Coding Questions
What is a feature in machine learning?
Back: An input variable the model uses to make predictions. Example: in house price prediction, features are square footage, bedrooms, location.
Tags: ml fundamentals
<!--ID: 1774613880864-->
END

START
Coding Questions
What is a target in machine learning?
Back: The output variable the model learns to predict (also called label or dependent variable). Continuous target → regression; categorical target → classification.
Tags: ml fundamentals
<!--ID: 1774613880866-->
END

START
Coding Questions
Why is X uppercase and y lowercase in ML notation?
Back: **X** = features matrix (multiple columns) → uppercase = matrix. **y** = target vector (single column) → lowercase = vector. Convention from linear algebra.
Tags: ml fundamentals
<!--ID: 1774613880867-->
END

START
Coding Questions
What is supervised learning?
Back: The model learns from labeled data where the correct answer is already known. Each row has input features (X) and a label (y). Two types: regression (continuous) and classification (discrete).
Tags: ml fundamentals
<!--ID: 1774613880869-->
END

START
Coding Questions
How do you decide between regression and classification?
Back:
- **Regression** — answer is "how much?" or "how many?" → continuous number (price, temperature)
- **Classification** — answer is "which one?" or "what type?" → discrete category (spam/not spam, cat/dog)
Tags: ml fundamentals
<!--ID: 1774613880871-->
END

START
Coding Questions
Why is it called "machine learning" instead of just programming?
Back: Because the **machine discovers patterns from data on its own** instead of a human writing explicit rules. In traditional programming, you code if-else rules. In ML, you provide examples and the model adjusts its weights to reduce error through repeated cycles — that iterative self-improvement is the "learning."
Tags: ml fundamentals
<!--ID: 1774613880873-->
END

START
Coding Questions
Why is supervised learning called "supervised"?
Back: Because **labeled data acts as a supervisor** — it tells the model the correct answer for each example. The model predicts, gets corrected by comparing to the label, and improves. Without labels (no supervisor), it becomes unsupervised learning.
Tags: ml fundamentals
<!--ID: 1774613880874-->
END
