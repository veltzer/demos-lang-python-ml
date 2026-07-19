# Stage 08: Class Imbalance — Oversampling and Undersampling

Titanic's `Survived` column is imbalanced (~62% perished, ~38% survived). A KNN trained
on the raw split will lean toward predicting the majority class — many true positives
become false negatives.

Two standard fixes:

- **Oversampling.** Duplicate minority-class rows (with replacement) until the two
  classes match in size. Training set grows; class balance is restored.
- **Undersampling.** Drop majority-class rows until the two classes match. Training set
  shrinks; class balance is restored.

Each has its trade-off:

| | Pros | Cons |
|---|---|---|
| Oversampling | uses all the data | duplicates inflate apparent training accuracy |
| Undersampling | smaller, balanced set | discards potentially useful data |

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_normalized.csv`, separate `y` and `X`.
3. `train_test_split(X, y)` once, outside any loop. Print `y_train.value_counts()` to
   see the class imbalance you're starting from.

## Tasks

For each of the three regimes below, fit `KNeighborsClassifier()`, predict on the
unchanged `X_test`/`y_test`, and print accuracy plus `classification_report`:

1. **Baseline (no resampling).** Fit on `X_train, y_train` directly. Label
   `"=== Baseline (no resampling) ==="`.
2. **Oversampling.** Combine `X_train` and `y_train` into one frame; split by class;
   `minority.sample(n=len(majority), replace=True)`; concatenate back. Print the new
   training-set size and class counts. Fit and score. Label `"=== Oversampling ==="`.
3. **Undersampling.** Same pattern but `majority.sample(n=len(minority))` (no
   replacement). Print the new size and counts. Fit and score. Label
   `"=== Undersampling ==="`.

## What to compare

Don't focus only on accuracy. Look at **recall on the minority class** in
`classification_report` — that's the metric resampling is trying to fix. Accuracy can
even drop slightly while recall on `Survived = 1` improves substantially, which is
usually a good trade.

## Pipeline note

Last stage of the pipeline. There's no output file; this is the final evaluation step.
