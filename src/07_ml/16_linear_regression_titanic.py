#!/usr/bin/env python

"""Solution to exercise 16: linear regression on Titanic with 0.5 threshold."""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df = df.drop(columns=["Name", "Cabin", "Ticket", "PassengerId"])
df = df.dropna()
df["Sex"] = df["Sex"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

y = df["Survived"]
x = df.drop(columns="Survived")

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
reg = LinearRegression()
reg.fit(x_train, y_train)

y_pred_continuous = reg.predict(x_test)
y_pred = (y_pred_continuous > 0.5).astype(int)
print(f"accuracy: {accuracy_score(y_test, y_pred):.4f}")
