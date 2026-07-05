# Exercise: Make Your ML Run Deterministic

`DecisionTreeClassifier` and `train_test_split` both have non-determinism: each call
gives slightly different splits and trees, which means slightly different scores. That
makes A/B comparison impossible — was your "improvement" real or just noise?

The fix: pin every source of randomness *before* doing anything else.

## Tasks

1. Call `random.seed(0)` and `numpy.random.seed(0)` at the top of your script.
2. Load `data.csv`, prepare features as in earlier exercises (drop nothing extra, fill
   NaN with `0`, `get_dummies` everything, separate `Survived`).
3. Train a `DecisionTreeClassifier()` and print the test score.
4. Run the script three times. The score should be **exactly the same** every time.
5. Comment out the `seed` calls and run again three times. Now the score will jitter.

This is the bare minimum reproducibility hygiene for any ML script.
