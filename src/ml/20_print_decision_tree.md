# Exercise 21: Print a Trained Decision Tree

A decision tree classifier is unusual among ML models in that you can read the entire
trained model out as text — every split condition and every leaf class. `sklearn.tree`
exposes `export_text` for exactly this.

The output looks like:

```
|--- feature_6 <= 0.50
|   |--- feature_5 <= 26.27
|   |   |--- feature_4 <= 0.50
|   |   |   |--- feature_0 <= 577.00
...
```

Each `|---` line is a node; the indent shows depth.

## Tasks

1. Load `data.csv` (Titanic) and prepare features:
   - drop `Name`, `Embarked`, `Cabin`, `Ticket`,
   - separate `Survived` as the target,
   - fill NaNs with `0`,
   - one-hot encode the remaining categorical columns with `pd.get_dummies`.
2. Print `X.columns` so you can map `feature_0`, `feature_1`, …, back to real column
   names later.
3. Train a `DecisionTreeClassifier` on the full data with a fixed `random_state`.
4. Print the tree using `sklearn.tree.export_text(clf)`.
5. Bonus: pass `feature_names=list(X.columns)` to `export_text` to get readable names
   instead of `feature_0`, `feature_1`, …
