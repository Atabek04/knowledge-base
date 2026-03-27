TARGET DECK: Tech-KB::Python::Matplotlib
Tags: python matplotlib
**Chapter:** Pyplot Methods
**Related:** [[Python MOC]], [[Pyplot is the convenience module for quick plotting in Matplotlib]]

---

START
Coding Questions
What does `plt.scatter(x, y)` do and when do you use it?
Back: Draws **individual dots** on the chart — one dot per `(x[i], y[i])` pair. "Scatter" means to throw things in different directions. Use it to show **raw data points** (e.g. actual test observations). Does not connect points with lines.
Tags: python matplotlib
<!--ID: 1774613880806-->
END

START
Coding Questions
What does `plt.plot(x, y)` do and how does it draw a line without a function?
Back: Connects data points with **straight line segments** in order — point 1 → point 2 → point 3. It doesn't need a math function; it just joins dots. For linear regression, predictions already lie on a straight line, so connecting them produces a perfect line. **Warning:** if x values are unsorted, the line will zigzag.
Tags: python matplotlib
<!--ID: 1774613880808-->
END

START
Coding Questions
What's the difference between `plt.scatter` and `plt.plot`?
Back:
- `scatter` → **individual dots**, no connections. Use for raw data points.
- `plot` → **connected line** between points. Use for trends and predictions.
Tags: python matplotlib
<!--ID: 1774613880810-->
END

START
Coding Questions
How do you visualize a regression model's predictions vs actual data?
Back:
```python
plt.scatter(X_test, y_test, color='red')   # actual data
plt.plot(X_test, y_pred, color='blue')      # regression line
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
```
`scatter` = real observations, `plot` = predicted line.
Tags: python matplotlib
<!--ID: 1774613880812-->
END

START
Coding Questions
Why must `plt.show()` be called last?
Back: pyplot builds the chart **in memory** as you call scatter, plot, title, etc. Nothing appears until `show()` renders it. Anything added **after** `show()` goes to a new empty chart.
Tags: python matplotlib
<!--ID: 1774613880814-->
END
