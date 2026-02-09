Pandas provides three main approaches to create a DataFrame.

## 1. From Arrays (NumPy or Python Lists)

Pass a 2D array where each inner array is a **row**.
Must specify column names separately.

**Using NumPy arrays** (see [[NumPy provides efficient array operations for numerical computing in Python]]):

```python
import pandas as pd
import numpy as np

# Create 2D array (3 rows, 2 columns)
data = np.array([[25, 50000],
                 [30, 65000],
                 [28, 55000]])

df = pd.DataFrame(data, columns=['Age', 'Income'])
```

**Using Python lists**:

```python
import pandas as pd

# List of lists (each inner list is a row)
data = [[25, 50000],
        [30, 65000],
        [28, 55000]]

df = pd.DataFrame(data, columns=['Age', 'Income'])
```

## 2. From Dictionary (Most Common)

Each **key** is a column name, each **value** is a list of row values.

```python
import pandas as pd

data = {
    'Age': [25, 30, 28],
    'Income': [50000, 65000, 55000],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
```

Column names come from keys automatically — no duplication needed.
This is the **most intuitive and commonly used** method.

## 3. From CSV File

Read tabular data directly from files.

```python
import pandas as pd

df = pd.read_csv('data.csv')
```

Pandas automatically:
- Detects column names from first row
- Infers data types for each column
- Handles missing values as NaN

---

**Links**: [[Pandas MOC]]
