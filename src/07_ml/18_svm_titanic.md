# Exercise 18: Support Vector Machine on Titanic

Solve the Titanic problem with an [SVM](https://scikit-learn.org/stable/modules/svm.html)
and compare its precision against the other classifiers you've tried.

SVMs find the hyperplane that maximally separates the two classes. With the `rbf` kernel
(the default) they can fit non-linear boundaries.

## Tasks

1. Load `../../data/titanic.csv`. Drop `Name`, `Cabin`, `Ticket`, `PassengerId`. Drop
   rows with NaN.
2. Encode `Sex` and `Embarked` to integer codes.
3. **Standardize the features.** SVM with `rbf` kernel is *very* sensitive to feature
   scale — without scaling the result is meaningless.
4. Train/test split.
5. Fit `sklearn.svm.SVC(random_state=0)`.
6. Predict on the test set.
7. Print:
   - **accuracy** (`accuracy_score`)
   - **precision** (`precision_score` — fraction of predicted-survived that actually
     survived)
   - **recall** (`recall_score` — fraction of actually-survived correctly identified)

## Compare

You're being asked specifically about *precision* — how does SVM's precision compare to
KNN, logistic regression, and decision tree on the same data? On Titanic, SVM with `rbf`
typically lands somewhere between logistic regression and a tuned random forest in
overall accuracy, but precision/recall trade-offs vary by classifier and threshold.
