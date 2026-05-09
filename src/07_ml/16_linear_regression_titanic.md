# Exercise 16: Linear Regression on Titanic

Solve the Titanic problem using **linear regression**.

Important caveats:

- Linear regression is an **estimation** algorithm, not a **classification** algorithm.
  It will produce a continuous output (any real number); we threshold it at `0.5` to
  recover a 0/1 prediction.
- For linear regression all input columns must be numeric — encode strings to integers
  first.
- Linear regression assumes each feature is roughly *linearly* correlated with the
  target. Features that are clearly non-linearly related won't help; ones that are
  uncorrelated will only add noise.

## Tasks

1. Load `../../data/titanic.csv`.
2. Drop high-cardinality columns (`Name`, `Cabin`, `Ticket`, `PassengerId`) and any rows
   with NaN in the columns you keep.
3. Encode `Sex` (`male` → 0, `female` → 1) and `Embarked` to integer codes.
4. Separate `y = df["Survived"]` and `X = everything else`.
5. Train/test split with a fixed `random_state`.
6. Fit a `sklearn.linear_model.LinearRegression()`.
7. Predict the continuous values on the test set.
8. Threshold predictions at `0.5` to get 0/1, and compute accuracy with
   `accuracy_score(y_test, (y_pred > 0.5).astype(int))`.

## Reflect

- How does the score compare to a `DecisionTreeClassifier` or `LogisticRegression` on
  the same data?
- Linear regression often does *worse* than logistic regression on classification
  problems precisely because it isn't built for it — predictions can fall outside
  `[0, 1]`, and the loss function it's optimizing (squared error) doesn't match the
  classification objective.
