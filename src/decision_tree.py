#!/usr/bin/env python

import pandas
import sklearn.tree
import sklearn.model_selection

tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)

X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]

# drop un-needed columns...
X = X.drop(["PassengerId","Name","Cabin", "Ticket"], axis=1,)

# turn all columns numeric, if a column is not numeric replace it with 0/1 columns
# that represent it's various states. Could produce a lot of columns...
X = pandas.get_dummies(X)
# print(X.shape)
# print(X)

# split the data to train and test
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y)

# alg = sklearn.tree.DecisionTreeClassifier(max_depth=7)
alg = sklearn.tree.DecisionTreeClassifier(min_samples_leaf=5)
alg.fit(X_train, Y_train)

score_test = alg.score(X_test, Y_test)
score_train = alg.score(X_train, Y_train)
print(f"test score {score_test}, train score {score_train}")
