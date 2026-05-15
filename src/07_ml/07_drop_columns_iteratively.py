#!/usr/bin/env python

"""Solution to exercise 17: cumulative column dropping on Titanic data."""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

X = pd.read_csv("data/titanic.csv")
X.fillna(0, inplace=True)
X.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
Y = X[["Survived"]]
X.drop(["Survived"], axis=1, inplace=True)
X = pd.get_dummies(X)

for _ in range(X.shape[1]):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    alg = DecisionTreeClassifier()
    alg.fit(X_train, Y_train)
    score = alg.score(X_test, Y_test)
    print("overall score", score)
    X.drop(X.columns[0], axis=1, inplace=True)
