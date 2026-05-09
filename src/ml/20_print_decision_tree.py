#!/usr/bin/env python

"""Solution to exercise 21: train a decision tree and print it as text."""

from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

df = pd.read_csv("data.csv")
df.fillna(0, inplace=True)
df.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
y = df["Survived"]
x = pd.get_dummies(df.drop("Survived", axis=1))

print(x.columns)

clf = DecisionTreeClassifier(random_state=0)
clf.fit(x, y)
print(export_text(clf, feature_names=list(x.columns)))
