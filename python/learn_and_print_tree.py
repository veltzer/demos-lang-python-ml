#!/usr/bin/python3
import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

ctor = DecisionTreeClassifier
tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)
tbl.drop(["Name", "Embarked", "Cabin", "Ticket"], inplace=True, axis=1)
X = tbl.drop(["Survived"], axis=1,)
Y = tbl[["Survived"]]
X = pandas.get_dummies(X)
Y = pandas.get_dummies(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y)
alg = ctor()
alg.fit(X_train, y_train)
score = alg.score(X_test, y_test)
#print("overall score", score)
print(X.columns)
text_representation = tree.export_text(alg)
print(text_representation)
