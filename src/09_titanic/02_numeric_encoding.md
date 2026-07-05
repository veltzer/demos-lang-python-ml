# Stage 02: Convert Categorical Columns to Numeric

`KNeighborsClassifier` (which we'll fit in stage 04) works on Euclidean distances over
numeric features. Any string column needs an integer encoding first.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_clean.csv` (the output of stage 01).

## Tasks

1. Print the names of all non-numeric columns:

   ```
   df.select_dtypes(exclude="number").columns
   ```

   You should see `Sex` and `Embarked`.

2. Encode each as integer category codes:

   ```
   df["Sex"]      = df["Sex"].astype("category").cat.codes
   df["Embarked"] = df["Embarked"].astype("category").cat.codes
   ```

   `cat.codes` assigns `0, 1, 2, …` to the unique values in alphabetic order.

3. Save the result to `../../data/titanic_numeric.csv`.

## A caveat about `cat.codes` for KNN

`cat.codes` produces an *ordinal* encoding — it implies that `Embarked = 0` is closer to
`Embarked = 1` than to `Embarked = 2`. That isn't true for `Embarked` (the three ports
have no natural order). For a more correct setup you would use one-hot encoding instead.
For this exercise pipeline we keep it simple and accept the imperfection.

## Pipeline note

Stage 03 reads `titanic_numeric.csv`.
