#!/usr/bin/env python

"""
marks notes:
before optimizatin:
    real    0m1.588s
    user    0m1.558s
    sys     0m0.905s

    real    0m1.100s
    user    0m1.101s
    sys     0m0.832s
"""
    
import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier
import numpy.random
from sklearn.model_selection import train_test_split

X = pd.read_csv("data.csv")
X.fillna(0, inplace=True)
# Because we are using DecisionTreeClassifier, and we need to do get_dummies, and name is
# unique (almost) per person, it is useless, and we remove it
X.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
Y = X[["Survived"]]
X.drop(["Survived"], axis=1, inplace=True)
X=pd.get_dummies(X)

for _ in range(X.shape[1]):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    alg = DecisionTreeClassifier()
    alg.fit(X_train, Y_train)
    score = alg.score(X_test, Y_test)
    print("overall score", score)
    X.drop(X.columns[0], axis=1, inplace=True)
