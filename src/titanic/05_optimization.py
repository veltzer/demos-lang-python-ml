#!/usr/bin/env python

"""
This is an example of running KNN on clean, numeric, normalized data.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, precision_score, confusion_matrix
import pandas
import numpy
import random
from itertools import combinations

# random.seed(0)
# numpy.random.seed(0)

df = pandas.read_csv("../../data/titanic_normalized.csv")

# y = target column
y = df["Survived"]

# X = everything except target
X = df.drop(columns="Survived")

for col in X:
    X_dropped = df.drop(columns=col)
    X_train, X_test, y_train, y_test = train_test_split(X_dropped, y)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"col={col},{accuracy_score(y_test, y_pred)}")

print("======================================")

for col1, col2 in combinations(df.columns, 2):
    X_dropped = df.drop(columns=[col1, col2])
    X_train, X_test, y_train, y_test = train_test_split(X_dropped, y)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    print(f"col1={col1},col2={col2},{accuracy_score(y_test, y_pred)}")
