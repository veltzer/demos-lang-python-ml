# Stage 05: Find Columns Worth Dropping

Not every feature helps. A column that contributes pure noise actively hurts a KNN
classifier — it adds a dimension to the distance calculation that pushes truly-similar
neighbors apart. This stage tries dropping subsets of columns and prints the resulting
test accuracy for each.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_normalized.csv`, separate `y = df["Survived"]` from
   `X = df.drop(columns="Survived")`.

## Tasks

Print the test accuracy for each of three regimes, all using `KNeighborsClassifier(n_neighbors=5)`:

1. **No columns dropped (baseline)** — fit on the full feature set and print the test
   accuracy. Label the line `"no columns dropped"`.
2. **One column dropped** — for each column `col` in `X`, drop it, fit, score, and print
   `f"col={col},{accuracy}"`. Label the section `"one column dropped"`.
3. **Two columns dropped** — for every unordered pair `(col1, col2)` from
   `itertools.combinations(X.columns, 2)`, drop both, fit, score, and print
   `f"col1={col1},col2={col2},{accuracy}"`. Label the section `"two columns dropped"`.

## How to read the output

- If dropping a column **raises** accuracy, that column was hurting the model — drop it.
- If dropping it **lowers** accuracy, that column was carrying real signal — keep it.
- A single train/test split has noise of `±0.02` or so. Don't over-interpret tiny
  differences; the strong signal is when an accuracy clearly jumps `0.05+` either way.

## Pipeline note

This stage is diagnostic only — it doesn't write a file. Use the insights to inform
which columns you actually keep in stage 04, or to plan further feature engineering.
