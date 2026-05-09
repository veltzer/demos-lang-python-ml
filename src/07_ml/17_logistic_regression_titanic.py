#!/usr/bin/env python

"""Solution to exercise 17: logistic regression on Titanic with feature scaling."""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv("../../data/titanic.csv")
df = df.drop(columns=["Name", "Cabin", "Ticket", "PassengerId"])
df = df.dropna()
df["Sex"] = df["Sex"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

y = df["Survived"]
x = df.drop(columns="Survived")

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, random_state=0)
clf = LogisticRegression(max_iter=1000, random_state=0)
clf.fit(x_train, y_train)
print(f"accuracy: {clf.score(x_test, y_test):.4f}")
