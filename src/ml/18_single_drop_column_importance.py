#!/usr/bin/env python

"""Solution to exercise 18: per-column importance via single-drop ablation."""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

SEED = 0


def fit_and_score(x: pd.DataFrame, y: pd.Series) -> float:
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=SEED)
    clf = DecisionTreeClassifier(random_state=SEED)
    clf.fit(x_train, y_train)
    return float(clf.score(x_test, y_test))


def main() -> None:
    df = pd.read_csv("data.csv")
    df.fillna(0, inplace=True)
    df.drop(["Name", "Embarked", "Cabin", "Ticket"], axis=1, inplace=True)
    y = df["Survived"]
    x = pd.get_dummies(df.drop("Survived", axis=1))

    baseline = fit_and_score(x, y)
    print(f"baseline: {baseline:.4f}")

    for col in x.columns:
        s = fit_and_score(x.drop(col, axis=1), y)
        print(f"{col}: {s:.4f}  drop = {baseline - s:+.4f}")


if __name__ == "__main__":
    main()
