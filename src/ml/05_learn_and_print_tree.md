# Exercise: Train and Print a Decision Tree

Decision trees are unusual among classifiers in that the trained model is a small,
human-readable structure: every node is a `(feature, threshold)` test and every leaf is
a class. `sklearn.tree.export_text` prints it.

## Tasks

1. Load `data.csv`, fill NaN with `0`, drop `Name`, `Embarked`, `Cabin`, `Ticket`.
2. Separate `Survived` as `Y`. One-hot encode `X` with `pd.get_dummies`.
3. Train a default `DecisionTreeClassifier()` on a train/test split.
4. Print `X.columns` so you can map the feature indices in the tree back to real column
   names.
5. Print `sklearn.tree.export_text(alg)`.

You will see lines like:

```
|--- feature_6 <= 0.50
|   |--- feature_5 <= 26.27
|   |   |--- ...
```

`feature_6` is the seventh column of `X` after `get_dummies` — usually `Sex_male` or
`Sex_female`. Tree depth on Titanic without `max_depth` typically blows up to 15-20
levels; if you want to see a tighter tree, pass `max_depth=4` to the classifier.
