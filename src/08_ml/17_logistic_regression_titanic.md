# Exercise 17: Logistic Regression on Titanic

Logistic regression is the right linear model for binary classification. It outputs a
probability in `[0, 1]` that the row belongs to the positive class, and it's optimized
for the cross-entropy loss (which actually matches the classification objective, unlike
squared-error linear regression).

## Tasks

1. Load `../../data/titanic.csv`.
2. Drop high-cardinality columns (`Name`, `Cabin`, `Ticket`, `PassengerId`) and any rows
   with NaN in the columns you keep.
3. Encode `Sex` and `Embarked` to integer codes.
4. Separate `y` and `X`.
5. **Standardize the features** with `sklearn.preprocessing.StandardScaler` — logistic
   regression's L2 regularization is sensitive to feature scale.
6. Train/test split.
7. Fit a `sklearn.linear_model.LogisticRegression(max_iter=1000, random_state=0)`.
8. Print the test accuracy.

## Compare

If you've done exercises 16 (linear regression) and 15 (KNN + logreg as two of two)
already, you should see that logistic regression on the same data outperforms linear
regression and is competitive with the strongest non-tree classifiers. On Titanic,
expect ~`0.78–0.82`.
