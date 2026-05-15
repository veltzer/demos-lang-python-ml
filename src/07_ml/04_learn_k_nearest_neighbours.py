#!/usr/bin/env python

"""
Unsupervised learning using the k nearest neighbour algorithm
"""

import numpy.random
import sklearn.model_selection
import sklearn.neighbors
import pandas

# always get the same results...
numpy.random.seed(5)

tbl = pandas.read_csv("../../data/titanic.csv")
print(tbl)
for col in tbl.columns:
    tbl[col] = tbl[col].fillna(0 if pandas.api.types.is_numeric_dtype(tbl[col]) else "")

X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]
print(type(Y), type(X))

# turn all columns numeric, if a column is not numeric replace it with 0/1 columns
# that represent it's various states. Could produce a lot of columns...
print(len(X.columns))
X = pandas.get_dummies(X)
print(len(X.columns))

# split the data to train and test
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y)
YY = Y_train.values.ravel()
print(type(YY))

alg = sklearn.neighbors.KNeighborsClassifier(n_neighbors=1)

alg.fit(X_train, YY)

score_test = alg.score(X_test, Y_test)
score_train = alg.score(X_train, Y_train)
print(f"test score {score_test}, train score {score_train}")
