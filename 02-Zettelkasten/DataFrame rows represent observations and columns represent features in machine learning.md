
In machine learning, a DataFrame organizes data as a **2D table** where structure maps directly to ML concepts.

## Pandas Terminology

**DataFrame**: 2D structure (like a spreadsheet with rows and columns).

**Series**: 1D structure (single column only).

**Index**: Row headings/labels (left-most column identifying each row).

**NaN**: Empty cells — stands for "Not a Number" (missing data).

## Structure Mapping

**Columns = <mark style="background: #FFF3A3A6;">Features</mark>** (variables, attributes, predictors)
Each column represents one measurable property or characteristic.

**Rows = <mark style="background: #BBFABBA6;">Observations</mark>** (samples, instances, examples)
Each row represents one complete data point or record.

## Data Type Rule

**<mark style="background: #ADCCFFA6;">Each column must have one consistent data type</mark>** (int, float, string, datetime, etc.).

Mixed types in a single column are technically allowed (stored as `object` dtype) but break ML algorithms and hurt performance.

## ML Workflow Context

This structure feeds directly into ML algorithms:
- **X** (features): <mark style="background: #ABF7F7A6;">All columns except target</mark>
- **y** (target): <mark style="background: #FFF3A3A6;">One column to predict</mark>

---

**Links**: [[Pandas MOC]]
