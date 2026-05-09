# Stage 04: Fit a KNN Classifier

The data is now clean, numeric, and normalized. Time to fit a model and see what
accuracy we get.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_normalized.csv`.

## Tasks

1. Split into target and features:

   ```
   y = df["Survived"]
   X = df.drop(columns="Survived")
   ```

2. Train/test split with `train_test_split(X, y)`.
3. Fit a default `KNeighborsClassifier()`.
4. Predict on the test set: `y_pred = knn.predict(X_test)`.
5. Report the model's quality with **four** different metrics, because accuracy alone
   doesn't tell the whole story when classes are imbalanced:
   - `accuracy_score(y_test, y_pred)` — overall fraction correct.
   - `precision_score(y_test, y_pred)` — of those predicted survived, how many actually did.
   - `classification_report(y_test, y_pred)` — also shows recall and F1 per class.
   - `confusion_matrix(y_test, y_pred)` — the raw 2x2 count.

## What to expect

On clean+numeric+normalized Titanic data with default KNN you should see test accuracy
around `0.75–0.80`. Stages 05–08 will probe whether we can squeeze more out of this.

## Pipeline note

Stages 05, 06, 07, 08 all read the same `titanic_normalized.csv` and try different
optimizations against this same baseline.
