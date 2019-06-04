#!/usr/bin/python3

import pandas as pd

from sklearn.tree import DecisionTreeClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split

ctor = DecisionTreeClassifier
# ctor = SVC
# ctor = LogisticRegression
# ctor = KNeighborsClassifier

tbl = pd.read_csv("train.csv")
tbl.fillna(0, inplace=True)

X = tbl.drop(
    ["Survived"],
    axis=1,
)

Y = tbl[["Survived"]]

X = pd.get_dummies(X)
Y = pd.get_dummies(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y)

alg = ctor()
alg.fit(X_train, y_train)

score = alg.score(X_test, y_test)
print("overall score", score)
