import pandas as pd

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

# ctor = tree.DecisionTreeClassifier
# ctor = LogisticRegression
# ctor = KNeighborsClassifier
ctor = svm.SVC

tbl = pd.read_csv("train.csv")
tbl = tbl.drop(labels=["Cabin", "Age"], axis=1)
tbl.Embarked.fillna("S", inplace=True)
tbl.Fare.fillna(0, inplace=True)
tbl = tbl.drop("Embarked", axis=1)
X = tbl.drop(
    ["Survived"],
    axis=1,
)

Y = tbl[["Survived"]]

# tbl = None

X = pd.get_dummies(X)
Y = pd.get_dummies(Y)

X_train, X_test, y_train, y_test =\
    train_test_split(X, Y)

alg = ctor(kernel="poly", degree=4)
alg.fit(X_train, y_train)

score = alg.score(X_test, y_test)
print("overall score", score)

# for column_name in list(tbl):
#     tbl_new = tbl.copy()
#     Y = tbl_new[["Survived"]]
#     X = tbl_new.drop(["Survived", column_name], axis=1)
#     X = pd.get_dummies(X)
#     Y = pd.get_dummies(Y)
#     X_train, X_test, y_train, y_test = train_test_split(X, Y)
#     alg = ctor()
#     alg.fit(X_train, y_train)
#     score = alg.score(X_test, y_test)
#     print(column_name, score)
#
# tbl_new = tbl.copy()
# Y = tbl_new[["Survived"]]
# # print(list(tbl_new))
# X = tbl_new["Sex"]
# X = pd.get_dummies(X)
# Y = pd.get_dummies(Y)
# X_train, X_test, y_train, y_test = train_test_split(X, Y)
# alg = ctor()
# alg.fit(X_train, y_train)
# score = alg.score(X_test, y_test)
# print('only sex', score)
