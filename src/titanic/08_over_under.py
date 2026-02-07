#!/usr/bin/env python

"""
This is an example of how to over-sample and under-sample using the titanic data.
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
print(y_train.value_counts())

# Baseline - no resampling
print("=== Baseline (no resampling) ===")
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(f"accuracy is {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Oversampling - duplicate minority class samples to match majority
train_df = pandas.concat([X_train, y_train], axis=1)
majority = train_df[train_df["Survived"] == 0]
minority = train_df[train_df["Survived"] == 1]
minority_oversampled = minority.sample(n=len(majority), replace=True)
train_oversampled = pandas.concat([majority, minority_oversampled])
X_train_over = train_oversampled.drop(columns="Survived")
y_train_over = train_oversampled["Survived"]

print("=== Oversampling ===")
print(f"Training set size: {len(y_train_over)} (was {len(y_train)})")
print(y_train_over.value_counts())
knn = KNeighborsClassifier()
knn.fit(X_train_over, y_train_over)
y_pred = knn.predict(X_test)
print(f"accuracy is {accuracy_score(y_test, y_pred)}")

# Undersampling - reduce majority class samples to match minority
majority_undersampled = majority.sample(n=len(minority))
train_undersampled = pandas.concat([majority_undersampled, minority])
X_train_under = train_undersampled.drop(columns="Survived")
y_train_under = train_undersampled["Survived"]

print("=== Undersampling ===")
print(f"Training set size: {len(y_train_under)} (was {len(y_train)})")
print(y_train_under.value_counts())
knn = KNeighborsClassifier()
knn.fit(X_train_under, y_train_under)
y_pred = knn.predict(X_test)
print(f"accuracy is {accuracy_score(y_test, y_pred)}")
