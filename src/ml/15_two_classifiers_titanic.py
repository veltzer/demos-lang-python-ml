#!/usr/bin/env python

"""Solution to exercise 22: KNN and Logistic Regression on Titanic data."""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd

SEED = 0

df = pd.read_csv("data.csv")
df.fillna(0, inplace=True)
df.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
y = df["Survived"]
x = pd.get_dummies(df.drop("Survived", axis=1))

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=SEED)

scaler = StandardScaler()
x_train_s = scaler.fit_transform(x_train)
x_test_s = scaler.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train_s, y_train)
print(f"KNN (k=5): {knn.score(x_test_s, y_test):.4f}")

logreg = LogisticRegression(max_iter=1000, random_state=SEED)
logreg.fit(x_train_s, y_train)
print(f"LogisticRegression: {logreg.score(x_test_s, y_test):.4f}")
