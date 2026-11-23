#!/usr/bin/env python

"""
This is an example of how to find which columns could be dropped
"""

import random
from itertools import combinations

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

random.seed(0)

df = pd.read_csv("data/titanic_normalized.csv")

# y = target column
y = df["Survived"]

# X = everything except target
X = df.drop(columns="Survived")

print("no columns dropped")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)}")

print("one column dropped")
for col in X:
    X_dropped = X.drop(columns=col)
    X_train, X_test, y_train, y_test = train_test_split(X_dropped, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"col={col},{accuracy_score(y_test, y_pred)}")

print("two columns dropped")
for col1, col2 in combinations(X.columns, 2):
    X_dropped = X.drop(columns=[col1, col2])
    X_train, X_test, y_train, y_test = train_test_split(X_dropped, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"col1={col1},col2={col2},{accuracy_score(y_test, y_pred)}")
