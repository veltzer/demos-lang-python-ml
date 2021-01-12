#!/usr/bin/python3
import pandas as pd

import random

from sklearn.tree import DecisionTreeClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
import numpy.random

from sklearn.model_selection import train_test_split

ctor = DecisionTreeClassifier

tbl = pd.read_csv("data.csv")
tbl.fillna(0, inplace=True)

tbl = tbl.drop(["Survived"], axis=1,)
tbl['Survived'] = numpy.random.choice([0, 1], tbl.shape[0])

X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]

X = pd.get_dummies(X)
Y = pd.get_dummies(Y)

# split the data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y)

alg = ctor()
alg.fit(X_train, y_train)

score = alg.score(X_test, y_test)
print("overall score", score)
