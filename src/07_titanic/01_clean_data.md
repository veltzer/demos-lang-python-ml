# Stage 01: Clean the Data

Now you have a sense of the data, time to clean it. Real-world datasets always have
missing values and useless columns; this stage decides what to drop and what to keep.

## Setup

1. Seed `random` and `numpy.random` to `0`.
2. Load `../../data/titanic.csv`.

## Diagnose

Print:

- `df.shape[0]` — the total row count.
- `df.isna().sum()[df.isna().sum() > 0]` — columns that have any NaN, and the count.
- `df["Embarked"].value_counts()` — the distribution of `Embarked` values.

You should see:

```
total number of rows is 891...
Age         177
Cabin       687
Embarked      2
```

## Decisions

Apply this cleaning policy:

- **Drop rows with NaN `Age`.** Age is important and there's no good way to impute it.
  We lose 177 rows out of 891 — painful but acceptable.
- **Drop the `Cabin` column entirely.** 687 of 891 rows are missing it; what's left is too
  sparse to be useful.
- **Drop `PassengerId`, `Name`, `Ticket`.** Either non-numeric with no obvious encoding,
  or unique-per-row (no signal).
- **Drop the 2 rows with NaN `Embarked`.** Two rows is a rounding error.

## Tasks

1. Run the diagnose-print above.
2. `df.dropna(subset=["Age", "Embarked"])` and print the new shape.
3. `df.drop(columns=["Cabin", "PassengerId", "Name", "Ticket"])` and print the new shape.
4. Save the result to `../../data/titanic_clean.csv` with `df.to_csv(..., index=False)`.

## Pipeline note

Stage 02 reads `titanic_clean.csv`. If you don't write it here, nothing downstream works.
