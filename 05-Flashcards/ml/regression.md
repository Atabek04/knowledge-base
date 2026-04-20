TARGET DECK: Tech-KB::Machine Learning::Regression
Tags: ml regression
**Chapter:** Simple Linear Regression
**Related:** [[Machine Learning MOC]]

---

START
Coding Questions
What is simple linear regression and what is its equation?
Back: **Regressing** a continuous target from **one** feature by fitting the best straight line through data.
- Equation: **y = b₀ + b₁x**
- b₀ = intercept/bias, b₁ = slope
Tags: ml regression
<!--ID: 1774613880830-->
END

START
Coding Questions
What does OLS (Ordinary Least Squares) do and why does it square the errors?
Back: OLS finds the best-fit line by minimizing the **sum of squared errors**.
- Squaring prevents positive/negative errors from canceling out
- Punishes large errors more heavily (50² = 2500 vs 10² = 100)
- Uses calculus to find exact b₀ and b₁ directly — no iterations needed
Tags: ml regression
<!--ID: 1774613880832-->
END

START
Coding Questions
When should you use OLS vs Gradient Descent for linear regression?
Back:
- **OLS** — linear model AND < ~10,000 features. One-step solution via Normal Equation: θ̂ = (XᵀX)⁻¹Xᵀy. No scaling or learning rate needed.
- **Gradient Descent** — non-linear model OR > ~10,000 features. Iterative steps. Requires feature scaling and learning rate tuning.
- OLS becomes too slow at high dimensions because matrix inversion is O(n³).
Tags: ml regression
<!--ID: 1774613880833-->
END
