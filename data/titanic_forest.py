import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score

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

clf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
precision = precision_score(y_test, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Number of trees: {len(clf.estimators_)}")
print()
print("Feature importances:")
for name, imp in sorted(zip(feature_cols, clf.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name:10s} {imp:.4f}")
print()
for i, tree in enumerate(clf.estimators_):
    print(f"=== Tree {i} ===")
    print(export_text(tree, feature_names=feature_cols))
