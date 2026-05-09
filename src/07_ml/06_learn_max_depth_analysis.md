# Exercise: Sweep `max_leaf_nodes` to Find the Sweet Spot

A `DecisionTreeClassifier` with no constraints will grow until every leaf is pure on the
training data — perfect train accuracy and poor test accuracy. Constraining the tree
(via `max_depth`, `max_leaf_nodes`, `min_samples_leaf`, ...) is how you trade overfitting
for underfitting.

This exercise sweeps `max_leaf_nodes` from 2 to 39 and prints the train and test scores
for each. Expect the curves to look like:

- Tiny `max_leaf_nodes` (= 2 or 3): both train and test scores are mediocre — *underfit*.
- Mid range: train and test rise together, then test peaks — *the sweet spot*.
- Large: train keeps climbing toward 1.0 while test plateaus or falls — *overfit*.

## Tasks

1. Loop `i` from 2 to 39.
2. For each `i`, run `num_stability_runs = 10` independent train/test splits to average
   out variance, training a `DecisionTreeClassifier(max_leaf_nodes=i)` each time.
3. Print `i`, the average test score, and the average train score on one line per `i`.
4. Read off the value of `i` where the test score peaks.
