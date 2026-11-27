#!/usr/bin/env python

"""
an example of feature engineering
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

o_tbl = pd.read_csv("data/titanic.csv")
#o_tbl['Age'].fillna(o_tbl['Age'].mean(), inplace=True)  # noqa: ERA001  teaching: kept in the comment for the reader
#o_tbl['Cabin'].fillna(0, inplace=True)  # noqa: ERA001  teaching: kept in the comment for the reader
o_tbl['Embarked'] = o_tbl['Embarked'].fillna('S')
o_tbl['Sex'] = o_tbl['Sex'].replace('male', 0).replace('female', 1)
o_tbl = o_tbl.fillna(0)
tbl=o_tbl.drop([
    #'Embarked',
    'PassengerId',
    'Name',
    ], axis=1)
tbl=pd.get_dummies(tbl)
X = tbl.drop(["Survived"], axis=1)
Y = tbl[["Survived"]]

def run_it(title):
    print(f"number of columns is {len(X.columns)}")
    score: float = 0
    num_runs=40
    for _ in range(num_runs):
        alg = DecisionTreeClassifier()
        x_train, x_test, y_train, y_test = train_test_split(X, Y)
        alg.fit(x_train, y_train)
        score += float(alg.score(x_test, y_test))
    print(f"avg {title} is {score/num_runs}")

run_it("before fe")

# IDEA 1: add column with number of people with the same last name
o_tbl['LastName'] = o_tbl['Name'].str.split(',').str[0]
#X['count_lastName'] = o_tbl.groupby('LastName')['LastName'].transform('count')  # noqa: ERA001  teaching: kept in the comment for the reader
#X['Relatives'] = o_tbl['SibSp'] + o_tbl['Parch']  # noqa: ERA001  teaching: kept in the comment for the reader
#X['IsAlone'] = np.where(X['Relatives']>0,0,1)  # noqa: ERA001  teaching: kept in the comment for the reader
#X['Kids'] = o_tbl.apply(lambda row: row['Name'].find('Master', 0) != -1 or row['Name'].find('Miss', 0) != -1, axis=1)  # noqa: ERA001  teaching: kept in the comment for the reader
#X['Kids_int'] = X.apply(lambda row: int(row['Kids'])+1, axis=1)  # noqa: ERA001  teaching: kept in the comment for the reader
#X['Royalty'] = o_tbl.apply(lambda row: row['Name'].find('Dr.', 0) != -1 or row['Name'].find('Sir.', 0) != -1, axis=1)  # noqa: ERA001  teaching: kept in the comment for the reader
#X['Royalty_int'] = X.apply(lambda row: int(row['Royalty'])+1, axis=1)  # noqa: ERA001  teaching: kept in the comment for the reader
#X['count_Embarked'] = o_tbl.groupby('Embarked')['Embarked'].transform('count')  # noqa: ERA001  teaching: kept in the comment for the reader
run_it("after fe")
