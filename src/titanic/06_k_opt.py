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

# random.seed(0)
# numpy.random.seed(0)

df = pandas.read_csv("../../data/titanic_normalized.csv")

# y = target column
y = df["Survived"]

# X = everything except target
X = df.drop(columns="Survived")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# training
for n in range(3,9,2):
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"k={n},{accuracy_score(y_test, y_pred)}")
