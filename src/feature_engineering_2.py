#!/usr/bin/env python

"""
Another example of feature engineering
"""

import numpy
import sklearn.neighbors
import sklearn.tree
import sklearn.naive_bayes
import pandas

# features
f_embarked=False
f_dummies=False
f_drop=True
f_nor=False
f_age=False
f_fare=False
f_title=False
f_eng_alone=True
f_turn_column_sex_into_male_female=True
f_fillna=True

# Set random seed to get stable results for debugging
numpy.random.seed(5)

# Fill missing Embarked with most frequent value
tbl = pandas.read_csv("data.csv")

if f_fillna:
    tbl.fillna(0, inplace=True)

if f_turn_column_sex_into_male_female:
    tbl["sex_new"]=numpy.where(tbl["Sex"]=="male",1.0,0.0)
    tbl.drop(["Sex"], axis=1, inplace=True)

if f_embarked:
    tbl["Embarked"] = tbl["Embarked"].fillna(tbl["Embarked"].value_counts().index[0])
else:
    tbl.drop(["Embarked"], axis=1, inplace=True)

# Fill missing Fare based on mean ticket price for each Pclass
if f_fare:
    pclassFareMean = tbl[tbl["Fare"] > 0].groupby(["Pclass", "Embarked"])["Fare"].mean()
    for item, fare in pclassFareMean.items():
        tbl.loc[(tbl["Pclass"] == item[0]) & (tbl["Embarked"] == item[1]) & (tbl["Fare"].isnull()), "Fare"] = fare

# Create and reduce Title column
if f_title:
    titleDictionary = {"Master": "Master", "Miss": "Miss", "Mlle": "Miss", "Mme": "Ms", "Ms": "Ms", "Mr": "Mr",
                       "Countess": "Ms", "Mrs": "Ms", "Jonkheer": "Mr", "Don": "Mr", "Dr": "Mr", "Rev": "Mr", "Lady": "Ms",
                       "Major": "Senior", "Sir": "Senior", "Col": "Senior", "Capt": "Senior"}
    tbl["Title"] = tbl["Name"].str.extract(r"([A-Za-z]+)\.", expand=True)
    tbl = tbl.replace({"Title": titleDictionary})

# Fill missing Age based on mean age for each title
if f_age and f_title:
    titleAgeMean = tbl[tbl["Age"] > 0].groupby("Title")["Age"].mean()
    for title, age in titleAgeMean.items():
        tbl.loc[(tbl["Title"] == title) & (tbl["Age"].isnull()), "Age"] = age

# Add new features IsAlone
if f_eng_alone:
    tbl["IsAlone"] = (tbl["SibSp"] + tbl["Parch"] == 0) * 1

# Build dummy columns
if f_dummies:
    tbl = pandas.get_dummies(tbl, columns=["Pclass", "Embarked", "Title"], drop_first=False)

# Drop extra columns
if f_drop:
    tbl = tbl.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)

# Normalize columns
if f_nor:
    tbl = ((tbl - tbl.min()) / (tbl.max() - tbl.min()))

# print(tbl.to_string())
# print(tbl.corr().to_string())

X = tbl.drop(["Survived"], axis=1)
Y = tbl[["Survived"]]

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y)

treeClassifier = sklearn.tree.DecisionTreeClassifier(max_depth=15)
treeClassifier.fit(X_train, Y_train.values.ravel())
score_train = treeClassifier.score(X_train, Y_train)
score_test = treeClassifier.score(X_test, Y_test)
print(f"Decision Tree Train (depth={15}): {score_train}, Test: {score_test}")
