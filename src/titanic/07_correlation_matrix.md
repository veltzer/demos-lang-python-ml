# Stage 07: Inspect the Correlation Matrix

`DataFrame.corr()` computes the pairwise Pearson correlation of every numeric column.
Two practical uses:

1. **Find columns correlated with the target.** Strong `Survived` correlations point at
   the most predictive features — keep them.
2. **Find columns correlated with each other.** Two features that are nearly perfectly
   correlated carry almost the same information. Dropping one of the pair reduces
   dimensionality without hurting accuracy.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_normalized.csv`, separate `y` from `X` as in earlier stages.
   (Both are kept in the printed correlation matrix; `y` is the `Survived` column.)

## Tasks

1. Print `df.corr()`.

## How to read the output

- Look at the `Survived` row (or column — the matrix is symmetric). The largest
  *absolute* values are the most predictive features. On Titanic, `Sex` should top the
  list with `|corr| ≈ 0.5`.
- Look for off-diagonal cells with `|corr| > 0.7` between two non-target columns.
  Candidates on Titanic include `SibSp` and `Parch` (both family-related) and `Fare` and
  `Pclass` (richer passengers in higher classes).
- Pearson correlation only catches *linear* relationships. A feature that is highly
  predictive in a non-linear way (interactions, thresholds) will look uncorrelated here
  but still help a tree or KNN.

## Pipeline note

Diagnostic only — no output file.
