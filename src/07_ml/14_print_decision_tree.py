#!/usr/bin/env python

"""Solution to exercise 14: train a decision tree, print it, and render it as a PNG."""

from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df.fillna(0, inplace=True)
df.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
y = df["Survived"]
x = pd.get_dummies(df.drop("Survived", axis=1))

print(x.columns)

clf = DecisionTreeClassifier(max_depth=4, random_state=0)
clf.fit(x, y)
print(export_text(clf, feature_names=list(x.columns)))

fig, ax = plt.subplots(figsize=(20, 10))
plot_tree(clf, feature_names=list(x.columns), class_names=["died", "survived"],
          filled=True, fontsize=8, ax=ax)
fig.savefig("/tmp/14_decision_tree.png", dpi=150, bbox_inches="tight")
