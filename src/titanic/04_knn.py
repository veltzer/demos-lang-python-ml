#!/usr/bin/env python

"""
This is an example of running KNN on clean, numeric, normalized data.
"""

import random
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, precision_score, confusion_matrix
import pandas

random.seed(0)
numpy.random.seed(0)

df = pandas.read_csv("../../data/titanic_normalized.csv")

# y = target column
y = df["Survived"]

# X = everything except target
X = df.drop(columns="Survived")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# training
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Evaluate
print(f"accuracy is {accuracy_score(y_test, y_pred)}")
print(f"prevision is {precision_score(y_test, y_pred)}")
# print recall
# print F1
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
