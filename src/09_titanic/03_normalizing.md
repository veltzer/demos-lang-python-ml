# Stage 03: Normalize Numeric Features

KNN measures distances. If `Age` ranges 0..80 and `Pclass` ranges 1..3, the distance
calculation will be completely dominated by `Age` and `Pclass` will be essentially
ignored. The fix: normalize each feature so they all live on a comparable scale.

`sklearn.preprocessing.StandardScaler` rescales each column to have **mean 0 and standard
deviation 1**. After scaling, every feature contributes roughly equally to a Euclidean
distance.

## Setup

1. Seed both RNGs to `0`.
2. Load `../../data/titanic_numeric.csv` (output of stage 02).

## Tasks

1. Build a scaler: `scaler = StandardScaler()`.
2. Fit-transform every column **except `Survived`** — the target should not be scaled.

   ```text
   cols_to_scale = df.columns.drop("Survived")
   df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
   ```

3. Save the result to `../../data/titanic_normalized.csv`.

## A subtle point about leakage

Strictly speaking you should `fit` the scaler on the train split only, then `transform`
both train and test, to avoid letting test-set statistics leak into training. We're
skipping that here for simplicity — when you scale the full dataset you slightly
underestimate the test error you'd see in production.

## Pipeline note

All later stages (04 through 08) read `titanic_normalized.csv`.
