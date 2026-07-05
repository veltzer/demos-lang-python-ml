# Exercise 19: Naive Bayes Classification

Use a Naive Bayes classifier to predict whether a mushroom is poisonous given a set of
categorical attributes.

The original task references the [Kaggle Mushroom Classification
dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification) where every
column is categorical (cap shape, odor, gill color, …) and the target is `class` —
either `e` (edible) or `p` (poisonous).

If you have the Kaggle dataset locally, load it with
`pd.read_csv("mushrooms.csv")`. If you don't, the provided solution **synthesizes** a
small mushroom-like dataset so you can practice the workflow end-to-end without external
data.

Tasks:

1. Load (or synthesize) a DataFrame with categorical columns and a binary `class` target.
2. One-hot encode the categorical columns with `pd.get_dummies`.
3. Split into train and test sets.
4. Fit a `sklearn.naive_bayes.BernoulliNB` (or `CategoricalNB`) classifier.
5. Print the test accuracy.

Why Naive Bayes for this problem: every feature is categorical and conditionally
"sort-of-independent" given the class. Naive Bayes runs in linear time, has no
hyperparameters worth tuning for the basic case, and on truly categorical data with
strong per-feature signals (like mushroom *odor*) it tends to be surprisingly
competitive.
