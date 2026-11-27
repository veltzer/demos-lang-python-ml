#!/usr/bin/env python

"""
Learn and print the decision tree which is the result of the learning
"""

import pandas as pd
import sklearn.tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ctor = DecisionTreeClassifier
tbl = pd.read_csv("data/titanic.csv")
tbl = tbl.fillna(0)
tbl = tbl.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1)
X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]
X = pd.get_dummies(X)
Y = pd.get_dummies(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y)
alg = ctor()
alg.fit(X_train, y_train)
#score = alg.score(X_test, y_test)  # noqa: ERA001  teaching: kept in the comment for the reader
#print("overall score", score)  # noqa: ERA001  teaching: kept in the comment for the reader
print(X.columns)
print(sklearn.tree.export_text(alg))
