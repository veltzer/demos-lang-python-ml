
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

tbl = pd.read_csv("data.csv")
#Fillna 
tbl['Age'].fillna(tbl['Age'].mean(), inplace=True)
tbl['Cabin'].fillna(0, inplace=True)
tbl['Embarked'].fillna('S', inplace=True)
tbl['Sex'] = tbl['Sex'].replace('male', 0).replace('female', 1)

i_num = 20
score = 0
for i in range(i_num):
    #X = tbl.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1) #score about 0.77 
    X = tbl.drop(['Survived', 'PassengerId', 'Name', 'Cabin'], axis=1) #score about 0.82
    Y = tbl['Survived']
    
    X_d = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X_d, Y)
    
    alg = DecisionTreeClassifier()
    alg.fit(X_train, y_train) 
    score += alg.score(X_test, y_test)
    
before_fe_score = score/i_num    
print(f'overall score BEFORE FEATURE ENGINEERING: {round(before_fe_score, 3)}') # about 0.82

#FEATURE ENGINEERING
fe_columns_org = ['MartialStatus', 'LastName', 'count_lastname', 'Relatives', 
              'Cabin_bool', 'Ticket_bool', 'count_Embarked', 'Cabin_first_letter',
              'ticket_num', 'ticket_letters', 'Cabin_number', 'ticket_cnt']

fe_columns_change = {}
for c in fe_columns_org:
    fe_columns = fe_columns_org.copy()
    fe_columns.remove(c) # in order to drop remaining columns 
    score = 0
    for i in range(i_num):
        X = tbl
        X['MartialStatus'] = X['Name'].str.split(',').str[1].str.split().str[0].str.strip() 
        X['LastName'] = X['Name'].str.split(',').str[0] 
        X['count_lastname'] = X.groupby('LastName')['LastName'].transform('count') 
        X['Relatives'] = X['SibSp'] + X['Parch'] 
        X['Cabin_bool'] = X['Cabin'].where(X['Cabin'] == 0, 1) 
        X['Ticket_bool'] = X['Ticket'].str.contains('[a-zA-Z]').astype(int)
        X['count_Embarked'] = X.groupby('Embarked')['Embarked'].transform('count') 
        X['Cabin_first_letter'] = X['Cabin'].str[:1].fillna(0) 
        X['ticket_num'] = X['Ticket'].str.split().str[-1].replace('LINE', 0).astype('int64') 
        X['ticket_letters'] = X['Ticket'].str.split().str[0].str.replace('\d+', '', regex=True).replace('', 'Z', regex=True).replace(r'\.', '',regex=True).replace('\/', '', regex=True) 
        X['Cabin_number'] = X['Cabin'].str[1:].fillna(0)
        X['ticket_cnt'] = X.groupby('Ticket')['Ticket'].transform('count')
        
        X = X.drop(['Survived', 'PassengerId', 'Name', 'Cabin'] + fe_columns, axis=1)
        Y = tbl['Survived']
        
        X_d = pd.get_dummies(X)
        X_train, X_test, y_train, y_test = train_test_split(X_d, Y)
        
        alg = DecisionTreeClassifier()
        alg.fit(X_train, y_train)     
        score += alg.score(X_test, y_test)
        
    fe_columns_change[c] = round(score/i_num - before_fe_score, 3)
    print(f'overall score AFTER FEATURE ENGINEERING {c}: {round(score/i_num, 3)}')




       
