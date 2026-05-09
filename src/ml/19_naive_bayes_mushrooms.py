#!/usr/bin/env python

"""Solution to exercise 19: Bernoulli Naive Bayes on a synthetic mushroom dataset."""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
n = 2000

cap_shape = rng.choice(["bell", "convex", "flat", "knobbed"], size=n)
odor = rng.choice(["almond", "anise", "fishy", "foul", "none"], size=n)
gill_color = rng.choice(["black", "brown", "pink", "white"], size=n)

odor_poison_prob = {"almond": 0.05, "anise": 0.05, "fishy": 0.9, "foul": 0.95, "none": 0.3}
probs = np.array([odor_poison_prob[o] for o in odor])
poisonous = (rng.random(n) < probs).astype(int)

df = pd.DataFrame({
    "cap_shape": cap_shape,
    "odor": odor,
    "gill_color": gill_color,
    "class": poisonous,
})

x = pd.get_dummies(df.drop("class", axis=1))
y = df["class"]

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
clf = BernoulliNB()
clf.fit(x_train, y_train)
print(f"accuracy: {clf.score(x_test, y_test):.4f}")
