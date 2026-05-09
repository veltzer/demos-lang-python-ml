# Exercise: K-Nearest-Neighbours on Titanic

Decision trees aren't the only classifier. KNN classifies a point by looking at the `k`
nearest training examples and taking a majority vote.

## Tasks

1. Set `numpy.random.seed(5)` for reproducibility.
2. Load `data.csv`, fill NaN with `0`, separate `Survived` as the target.
3. One-hot encode the features with `pd.get_dummies`.
4. Train/test split.
5. Fit a `KNeighborsClassifier(n_neighbors=5)`. Note: `KNN.fit` requires `y` as a 1-D
   array, so pass `Y.values.ravel()` not the DataFrame `Y`.
6. Print the train and test scores.

Optional: try `n_neighbors` in `1, 3, 5, 7, 11, 21` and see which gives the best test
score. Small `k` overfits (memorizes individual training points); large `k`
underfits (smooths everything to the dataset majority).
