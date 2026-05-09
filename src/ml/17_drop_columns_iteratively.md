# Exercise 17: Iterative Column Dropping (Importance Heuristic)

A rough way to estimate which columns matter to a classifier is to drop them and watch
the score change. There are two natural variants:

- **Cumulative drop**: drop the first column, train, score. Then drop the first *and*
  second columns and retrain, score. Continue until only one column is left.
- **Single drop**: at each iteration drop *only* one column, train, score, then put it
  back. The drop in score per missing column is your importance estimate.

Tasks:

1. Load `data.csv` (Titanic) and prepare features:
   - drop `Name`, `Embarked`, `Cabin`, `Ticket` (high-cardinality strings that aren't
     useful here),
   - separate `Survived` as the target,
   - fill NaNs with `0`,
   - one-hot encode the remaining categorical columns with `pd.get_dummies`.
2. Implement the **cumulative drop** version: in a loop, train a `DecisionTreeClassifier`
   on the current `X`, print its score, and then drop the leftmost column. Stop when
   `X` has no columns left.
3. (Optional reflection.) Run it twice and notice the variance — `train_test_split` and
   `DecisionTreeClassifier` both have randomness. Pass a fixed `random_state` to both if
   you want stable comparison.
4. Note the limitation: cumulative drop confounds "the column we just dropped is
   important" with "the columns we dropped on previous iterations were important". Single
   drop is cleaner. Cumulative drop is faster.

The provided solution implements the cumulative-drop variant.
