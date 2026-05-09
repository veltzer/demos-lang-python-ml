# Exercise 22: Two Classification Algorithms on Titanic

Recommended reading first:
[Overview of Classification Methods in Python with
scikit-learn](https://stackabuse.com/overview-of-classification-methods-in-python-with-scikit-learn/).

Then go to the [scikit-learn supervised learning
docs](https://scikit-learn.org/stable/supervised_learning.html), find the list of
classification algorithms, and pick **two** — preferably *not*
`DecisionTreeClassifier`, which we have already used to death.

Tasks:

1. Load `data.csv` (Titanic) and prepare features (drop `Name`/`Embarked`/`Cabin`/
   `Ticket`, separate `Survived`, fill NaNs, `get_dummies`).
2. Pick two classifiers. Read their docs and try a few hyperparameter values for each.
3. Train both on the same train/test split. Print the test accuracy of each.
4. Reflect: which one performed better on this data? Why might that be? Do not
   over-interpret a single train/test split — repeat with a few random seeds if you
   want a more honest comparison.

The provided solution uses `KNeighborsClassifier` and `LogisticRegression` as the two
choices.

**Note:** No feature engineering is required for this exercise — focus on the algorithms.
