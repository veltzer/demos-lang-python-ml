#!/usr/bin/env python

"""
Show how to make your machine learning script deterministic by setting the random seeds.
"""

import random

import pandas as pd

# from sklearn.linear_model import LogisticRegression  # noqa: ERA001  teaching: kept in the comment for the reader
# from sklearn.neighbors import KNeighborsClassifier  # noqa: ERA001  teaching: kept in the comment for the reader
# from sklearn.svm import SVC  # noqa: ERA001  teaching: kept in the comment for the reader
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

random.seed(0)

ctor = DecisionTreeClassifier

tbl = pd.read_csv("data/titanic.csv")
tbl = tbl.fillna(0)

X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]

X = pd.get_dummies(X)
Y = pd.get_dummies(Y)

# split the data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

alg = ctor(random_state=0)
alg.fit(X_train, y_train)

score = alg.score(X_test, y_test)
print("overall score", score)
