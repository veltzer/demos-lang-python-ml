#!/usr/bin/env python

import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier
import numpy.random
from sklearn.model_selection import train_test_split

num_stability_runs=10
for i in range(2, 40):
    score=0
    score_train=0
    for j in range(num_stability_runs):
        tbl = pd.read_csv("data.csv")
        tbl.fillna(0, inplace=True)

        X = tbl.drop(["Survived"], axis=1,)
        Y = tbl[["Survived"]]
        X = pd.get_dummies(X)
        Y = pd.get_dummies(Y)
        X_train, X_test, y_train, y_test = train_test_split(X, Y)
        # alg = DecisionTreeClassifier(max_depth=i) 
        alg = DecisionTreeClassifier(max_leaf_nodes=i) 
        alg.fit(X_train, y_train)
        score += alg.score(X_test, y_test)
        score_train += alg.score(X_train, y_train)
    print(f"{i} {score/num_stability_runs} {score_train/num_stability_runs}")
