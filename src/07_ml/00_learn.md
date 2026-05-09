# Exercise: Basic Machine Learning Pipeline

This is the smallest possible end-to-end ML pipeline on the Titanic dataset.

## Steps

1. Read the Titanic CSV from `../data/titanic.csv`.
2. Set `random.seed(5)` and `numpy.random.seed(5)` so the run is reproducible.
3. Separate features `X` from target `Y` (the `Survived` column).
4. One-hot encode all string columns with `pd.get_dummies(X)`.
5. Split into train and test sets with `sklearn.model_selection.train_test_split`.
6. Fit a `DecisionTreeClassifier(max_depth=4)` and report the training and test scores.

## Tasks

- Implement the pipeline.
- Print both `score_test` and `score_train` so you can see how big the gap is. A large
  gap (train ≫ test) is overfitting; tightening `max_depth` reduces it.
- (Optional.) Swap in a `RandomForestClassifier()` and compare. A random forest usually
  gets more test score for less overfit on Titanic.
