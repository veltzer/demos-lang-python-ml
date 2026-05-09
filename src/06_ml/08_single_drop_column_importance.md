# Exercise 18: Single-Column Drop Importance

This is a refinement of the cumulative-drop method from exercise 17.

In exercise 17 you drop column `0`, then drop columns `0, 1`, then `0, 1, 2`, … and watch
the score collapse. The problem: by iteration `k`, you cannot tell whether the score
dropped because column `k` is important or because the columns you removed earlier were.

**Single drop** disentangles them:

1. Train on the full feature set, record the baseline score.
2. For each column `c` in turn: drop only `c`, train, score, record. Then put `c` back.
3. The score drop relative to baseline is your importance estimate for column `c`. The
   bigger the drop, the more important the column.

Tasks:

1. Load `data.csv` (Titanic) and prepare features the same way as exercise 17 (drop
   `Name`/`Embarked`/`Cabin`/`Ticket`, fill NaNs, one-hot encode, separate `Survived`).
2. Train a baseline `DecisionTreeClassifier` with a fixed random state and print its
   score.
3. Loop over each column: drop it, retrain (also fixed random state), print
   `<column_name>: <score>` and `<column_name>: drop = baseline - score`.
4. Reflection: did the cumulative-drop estimate (exercise 17) and the single-drop
   estimate agree on which columns matter? They often disagree because cumulative drop
   confounds correlated columns.

**Note:** Never drop the `Survived` column itself — it is the target, not a feature.
