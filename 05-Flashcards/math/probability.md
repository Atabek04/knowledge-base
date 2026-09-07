TARGET DECK: Math::Probability
Tags: math probability
**Chapter:** Mean, Median
**Related:** [[Math for ML MOC]]

---

START
Coding Questions
What is the mean and when is it misleading?
Back: **Sum of all values divided by count**: x̄ = Σxᵢ / n. It's misleading when data has **outliers** — e.g., salaries [30k, 35k, 32k, 28k, 33k, 500k] give mean = 109k, but nobody except the CEO earns near that. Use median instead for skewed data.
Tags: math probability
<!--ID: 1774613880782-->
END

START
Coding Questions
What is the median and why is it preferred over mean for skewed data?
Back: The **middle value** when data is sorted. Odd count → pick middle. Even count → average of two middle values. Median **ignores outliers** — whether the largest value is 100 or 1,000,000, the median stays the same. That's why it's the preferred imputation strategy for data with outliers.
Tags: math probability
<!--ID: 1774613880784-->
END
