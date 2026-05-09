#!/usr/bin/env python

"""Solution to exercise 16: compare baseline vs. two engineered features on Titanic."""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def score(x: pd.DataFrame, y: pd.Series, seed: int = 0) -> float:
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=seed)
    clf = DecisionTreeClassifier(random_state=seed)
    clf.fit(x_train, y_train)
    return float(clf.score(x_test, y_test))


def prepare(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(["Name", "Ticket", "Cabin", "Embarked"], axis=1)
    df = df.fillna(0)
    return pd.get_dummies(df)


def main() -> None:
    df = pd.read_csv("data.csv")
    y = df["Survived"]
    base = prepare(df.drop("Survived", axis=1))
    print("baseline:", score(base, y))

    engineered = df.copy()
    engineered["family_size"] = engineered["SibSp"] + engineered["Parch"] + 1
    engineered["is_alone"] = (engineered["family_size"] == 1).astype(int)
    x_eng = prepare(engineered.drop("Survived", axis=1))
    print("with family_size + is_alone:", score(x_eng, y))


if __name__ == "__main__":
    main()
