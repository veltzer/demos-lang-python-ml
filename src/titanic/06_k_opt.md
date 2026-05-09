# Stage 06: Find the Optimal `k` for KNN

The `n_neighbors` (`k`) parameter is the single most important knob on a KNN classifier:

- `k = 1` memorizes the training set perfectly and overfits.
- Very large `k` smooths everything to the dataset majority and underfits.
- Somewhere in between lies the sweet spot. We find it by sweeping.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_normalized.csv`, separate target/features as before.
3. Make a single `train_test_split` *outside* the loop so every `k` is evaluated against
   the same test set. This isolates the effect of `k` from the noise of resampling.

## Tasks

For each odd `n` in `range(3, 9, 2)` (i.e. `3, 5, 7`):

1. Fit `KNeighborsClassifier(n_neighbors=n)` on `X_train, y_train`.
2. Predict on `X_test`.
3. Print `f"k={n},{accuracy_score(y_test, y_pred)}"`.

## Why odd `k`?

For binary classification, even `k` can produce ties (e.g. with `k = 4`, two neighbors
vote `0` and two vote `1`). KNN tie-breaking is implementation-defined and adds noise.
Odd `k` avoids the issue.

## Extending the sweep

The provided range is short for demonstration. In a real evaluation you would:
- sweep a wider range (e.g. `range(1, 41, 2)`),
- average over several train/test splits at each `k` to smooth out noise,
- and plot the resulting curve.

## Pipeline note

Diagnostic only — no output file.
