# Exercise 19: Voting Ensemble on Titanic

Use scikit-learn's
[`VotingClassifier`](https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier)
to build an ensemble of three different ML models for Titanic, then combine their votes.

The intuition: different model families make different *kinds* of mistakes. A
decision tree's errors don't perfectly overlap with a logistic regression's errors. A
majority vote across diverse models often beats any single one.

## Tasks

1. Load `../../data/titanic.csv`. Drop `Name`, `Cabin`, `Ticket`, `PassengerId`. Drop
   NaN rows.
2. Encode `Sex` and `Embarked` to integer codes.
3. Standardize the features (some of the base classifiers need it).
4. Train/test split.
5. Build three base classifiers — pick three with different inductive biases. The
   provided solution uses:
   - `LogisticRegression` (linear, probabilistic)
   - `RandomForestClassifier` (non-linear, tree ensemble)
   - `KNeighborsClassifier` (instance-based)
6. Combine them in a `VotingClassifier(estimators=[...], voting="hard")`.
7. Print the test accuracy of each base classifier *and* of the ensemble. Compare.

## Soft vs hard voting

- `voting="hard"` — each base classifier votes 0 or 1, majority wins.
- `voting="soft"` — each base classifier outputs a probability, the probabilities are
  averaged, then thresholded at `0.5`. Soft voting usually does better when the base
  models are well-calibrated, but it requires every base model to support
  `predict_proba`.

Try both and see which works better on Titanic.
