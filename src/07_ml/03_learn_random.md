# Exercise: Sanity Check — Train on Random Labels

Before believing any classifier's "good" score, run this sanity check: replace the real
target column with **uniform random 0/1 labels** and re-train. The classifier should now
get roughly **50% test accuracy** (chance level for a balanced binary target).

If you get significantly more than 50%, something is leaking from the features into the
labels — usually a bug in your pipeline.

## Tasks

1. Load `data.csv`. Drop the real `Survived` column.
2. Replace it with `numpy.random.choice([0, 1], len(tbl))` — a brand-new random target.
3. Run the rest of the standard pipeline: `get_dummies`, `train_test_split`,
   `DecisionTreeClassifier().fit(X_train, y_train)`, score on the test set.
4. Print the test score. Expected: ~`0.5`. Anything well above `0.55` is suspicious and
   you should hunt for label leakage.
