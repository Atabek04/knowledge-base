TARGET DECK: Tech-KB::Machine Learning::Model Training
Tags: ml training
**Chapter:** Model Training Concepts
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
What is a parameter in machine learning?
Back: A value the model **learns from data** during training to make predictions. Divided into **weights** (multiply features) and **biases** (add baseline shift). Initially random, adjusted during training, saved and used forever after.
Tags: ml training
<!--ID: 1774613880816-->
END

START
Coding Questions
What do weights represent in a model?
Back: A weight (w) multiplies a feature to tell "how much does this feature affect prediction?" Example: in y = w₁ × sqft + w₂ × bedrooms + b, if w₁=100 then each square foot adds $100 to the prediction.
Tags: ml training
<!--ID: 1774613880818-->
END

START
Coding Questions
What does bias do in a model and what happens without it?
Back: Bias (b) is a number added to **every prediction** regardless of features — the baseline prediction before considering features. Without bias, a house with 0 sqft and 0 bedrooms would cost $0 instead of the land value.
Tags: ml training
<!--ID: 1774613880820-->
END

START
Coding Questions
What is a loss function and why does it square errors?
Back: A formula measuring **how wrong** the model is (lower = better). Squaring prevents positive/negative errors from canceling out and punishes large errors more heavily. MSE for regression: MSE = 1/n Σ(yᵢ - ŷᵢ)².
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
Back: `.predict(X_test)` returns predicted targets using the weight and bias learned during `.fit()`. You pass **features only** — no targets. It does **not** return accuracy — to measure that, you compare `y_pred` vs `y_test` using evaluation metrics separately.
Tags: ml training
<!--ID: 1774613880827-->
END
