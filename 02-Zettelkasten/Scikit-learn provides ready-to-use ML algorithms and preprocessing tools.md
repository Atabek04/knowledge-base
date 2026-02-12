---
created: 2026-02-12
aliases: [Scikit-learn, sklearn]
tags:
  - python/libraries
  - ml/tools
---
 
> **Scikit-learn** (imported as `sklearn`) is Python's main [[A Python module is a single file and a package is a folder of modules|library]] for machine learning — it provides ready-to-use algorithms, preprocessing, and evaluation tools.

The name: **Sci**entific tool**kit** for machine **learn**ing. Originally built as a SciPy extension.

---

### Most used modules

| Module                    | Purpose                                                                                                     | Example                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `sklearn.preprocessing`   | [[Feature scaling transforms features to similar ranges for efficient training\|Feature scaling]], encoding | `StandardScaler`, `LabelEncoder`, `OneHotEncoder` |
| `sklearn.impute`          | [[Missing data must be handled because most ML algorithms cannot compute with NaN\|Handle missing data]]    | `SimpleImputer`                                   |
| `sklearn.model_selection` | [[Train-test split evaluates model performance on unseen data\|Train-test split]], cross-validation         | `train_test_split`, `GridSearchCV`                |
| `sklearn.linear_model`    | Linear/logistic regression                                                                                  | `LinearRegression`, `LogisticRegression`          |
| `sklearn.tree`            | Decision trees                                                                                              | `DecisionTreeClassifier`                          |
| `sklearn.ensemble`        | Random forest, boosting                                                                                     | `RandomForestClassifier`, `GradientBoosting`      |
| `sklearn.svm`             | Support vector machines                                                                                     | `SVC`, `SVR`                                      |
| `sklearn.neighbors`       | K-nearest neighbors                                                                                         | `KNeighborsClassifier`                            |
| `sklearn.metrics`         | Evaluation metrics                                                                                          | `accuracy_score`, `confusion_matrix`              |
| `sklearn.cluster`         | Unsupervised clustering                                                                                     | `KMeans`, `DBSCAN`                                |

<mark style="background: yellow">You never import all of sklearn — you import only the specific module you need.</mark>

```python
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
```

---

Read more:
- [[A Python module is a single file and a package is a folder of modules]]
- [[Python MOC]]
- [[Machine Learning MOC]]
