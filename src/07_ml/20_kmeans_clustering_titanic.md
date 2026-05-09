# Exercise 20: K-Means Clustering on Titanic

So far every exercise has been **supervised** — we use `Survived` as a label and ask the
model to predict it. This exercise is **unsupervised**: we ignore `Survived` entirely
and ask "what natural groups exist in the rest of the data?"

K-means partitions the rows into `k` clusters, where each row joins the cluster whose
centroid is nearest in feature space. The number of clusters `k` is a hyperparameter you
have to choose.

## Setup tasks

To get meaningful clusters you must:

1. Drop irrelevant or non-numeric columns (`PassengerId`, `Name`, `Ticket`, `Cabin`).
2. Convert remaining strings to numeric (`Sex`, `Embarked`).
3. Drop NaN rows.
4. **Normalize the data.** K-means uses Euclidean distance, so unscaled features
   dominate the distance and the clusters become uninterpretable. Use
   `StandardScaler`.

## Clustering tasks

5. Sweep `n_clusters` from 2 to 14 (don't try `891` — that just memorizes the rows).
6. For each `k`, fit `KMeans(n_clusters=k, random_state=0, n_init=10)` and record the
   `inertia_` (sum of squared distances to nearest centroid).
7. Plot `k` vs `inertia_` (the "elbow plot"). The elbow — where the curve sharply bends
   from steep to flat — is a reasonable choice for `k`.

Save the elbow plot to `/tmp/20_kmeans_elbow.png`.

## Reflect

- Pick the `k` at the elbow. Re-fit `KMeans` with that `k`.
- For each cluster, compute the mean `Survived` rate. Even though `Survived` was *not*
  used during clustering, you may find that some clusters strongly skew toward one class
  — that's the unsupervised algorithm rediscovering structure on its own.
