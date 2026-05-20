import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score

df = pd.read_csv("titanic.csv")
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

feature_cols = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
X = df[feature_cols]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

logreg = LogisticRegression(max_iter=1000, random_state=42)
logreg.fit(X_train_s, y_train)
y_pred_lr = logreg.predict(X_test_s)

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
y_pred_dt = tree.predict(X_test)

def report(name, y_true, y_pred):
    print(f"{name}")
    print(f"  Accuracy : {accuracy_score(y_true, y_pred):.4f}")
    print(f"  Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"  Recall   : {recall_score(y_true, y_pred):.4f}")
    print(f"  F1       : {f1_score(y_true, y_pred):.4f}")

report("Logistic Regression", y_test, y_pred_lr)
print()
report("Decision Tree (max_depth=3)", y_test, y_pred_dt)
print()
print("Logistic Regression coefficients (on standardized features):")
for name, coef in sorted(zip(feature_cols, logreg.coef_[0]), key=lambda x: -abs(x[1])):
    print(f"  {name:10s} {coef:+.4f}")
print(f"  intercept  {logreg.intercept_[0]:+.4f}")
