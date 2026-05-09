# Exercise: Decision Tree with Manual Column Pruning

A small refinement of the basic ML pipeline. Instead of one-hot encoding *every* column,
this exercise drops a few columns up front because we know they will not help the
classifier:

- `PassengerId` — a unique identifier per row, no signal.
- `Name` — almost unique per row; would explode `get_dummies` and overfit.
- `Cabin` — high-cardinality and mostly NaN.
- `Ticket` — high-cardinality and mostly noise.

## Tasks

1. Read `data.csv` and `tbl.fillna(0, inplace=True)` so missing values become zero.
2. Separate `X` (features) and `Y` (Survived).
3. Drop `PassengerId`, `Name`, `Cabin`, and `Ticket` from `X`.
4. One-hot encode `X` with `pd.get_dummies`.
5. Train/test split, fit a `DecisionTreeClassifier(min_samples_leaf=5)`, and print both
   the test and train scores.

`min_samples_leaf=5` is a regularizer: a leaf must contain at least 5 training samples,
which prevents the tree from carving up the data into single-row leaves and overfitting
catastrophically.
