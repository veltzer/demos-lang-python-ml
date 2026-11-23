#!/usr/bin/env python

"""Solution to exercise 17: cumulative column dropping on Titanic data."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv("data/titanic.csv")
X = X.fillna(0)
X = X.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1)
Y = X[["Survived"]]
X = X.drop(["Survived"], axis=1)
X = pd.get_dummies(X)

for _ in range(X.shape[1]):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    alg = DecisionTreeClassifier()
    alg.fit(X_train, Y_train)
    score = alg.score(X_test, Y_test)
    print("overall score", score)
    X = X.drop(X.columns[0], axis=1)
