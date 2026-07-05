#!/usr/bin/env python

"""Solution to exercise 19: VotingClassifier ensemble of 3 diverse base models."""

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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

logreg = LogisticRegression(max_iter=1000, random_state=0)
rf = RandomForestClassifier(random_state=0)
knn = KNeighborsClassifier(n_neighbors=5)
ensemble = VotingClassifier(
    estimators=[("logreg", logreg), ("rf", rf), ("knn", knn)],
    voting="hard",
)

for name, clf in [("logreg", logreg), ("rf", rf), ("knn", knn), ("ensemble", ensemble)]:
    clf.fit(x_train, y_train)
    print(f"{name}: {clf.score(x_test, y_test):.4f}")
