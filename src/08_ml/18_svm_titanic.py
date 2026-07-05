#!/usr/bin/env python

"""Solution to exercise 18: SVM on Titanic with accuracy/precision/recall."""

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df = df.drop(columns=["Name", "Cabin", "Ticket", "PassengerId"])
df = df.dropna()
df["Sex"] = df["Sex"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

y = df["Survived"]
x = df.drop(columns="Survived")

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, random_state=0)
clf = SVC(random_state=0)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

print(f"accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"precision: {precision_score(y_test, y_pred):.4f}")
print(f"recall:    {recall_score(y_test, y_pred):.4f}")
