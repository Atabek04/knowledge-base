TARGET DECK: Machine Learning::Model Training
Tags: ml training
**Chapter:** Model Training Concepts
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
What is a parameter in machine learning?
Back: A value the model **learns from data** during training to make predictions. Divided into **weights** (multiply features) and **biases** (add baseline shift). Initially random, adjusted during training, saved and used forever after.
Tags: ml training
<!--ID: 1771415062796-->
END

START
Coding Questions
What do weights represent in a model?
Back: A weight (w) multiplies a feature to tell "how much does this feature affect prediction?" Example: in y = w₁ × sqft + w₂ × bedrooms + b, if w₁=100 then each square foot adds $100 to the prediction.
Tags: ml training
<!--ID: 1771415062800-->
END

START
Coding Questions
What does bias do in a model and what happens without it?
Back: Bias (b) is a number added to **every prediction** regardless of features — the baseline prediction before considering features. Without bias, a house with 0 sqft and 0 bedrooms would cost $0 instead of the land value.
Tags: ml training
<!--ID: 1771415062802-->
END

START
Coding Questions
What is a loss function and why does it square errors?
Back: A formula measuring **how wrong** the model is (lower = better). Squaring prevents positive/negative errors from canceling out and punishes large errors more heavily. MSE for regression: MSE = 1/n Σ(yᵢ - ŷᵢ)².
Tags: ml training
<!--ID: 1771415062803-->
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
<!--ID: 1771415062805-->
END
