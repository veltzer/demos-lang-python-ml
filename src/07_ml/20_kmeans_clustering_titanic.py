#!/usr/bin/env python

"""Solution to exercise 20: K-Means clustering on Titanic with elbow plot."""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
df = df.dropna()
df["Sex"] = df["Sex"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

survived = df["Survived"]
features = df.drop(columns="Survived")

scaler = StandardScaler()
x_scaled = scaler.fit_transform(features)

ks = list(range(2, 15))
inertias = []
for k in ks:
    km = KMeans(n_clusters=k, random_state=0, n_init=10)
    km.fit(x_scaled)
    inertias.append(km.inertia_)

fig, ax = plt.subplots()
ax.plot(ks, inertias, marker="o")
ax.set_xlabel("k")
ax.set_ylabel("inertia")
ax.set_title("K-Means elbow plot")
fig.savefig("/tmp/20_kmeans_elbow.png")

best_k = 4
km = KMeans(n_clusters=best_k, random_state=0, n_init=10)
labels = km.fit_predict(x_scaled)
df_with_clusters = features.copy()
df_with_clusters["cluster"] = labels
df_with_clusters["Survived"] = survived.values
print(df_with_clusters.groupby("cluster")["Survived"].agg(["mean", "count"]))
