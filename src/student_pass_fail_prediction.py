from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "student_pass_fail.csv"
MODEL_PATH = BASE_DIR / "models" / "student_pass_fail_model.pkl"

FEATURES = ["Study_Hours_Per_Day","Attendance_Percent","Assignment_Score","Previous_Exam_Score"]

df = pd.read_csv(DATA_PATH)
X, y = df[FEATURES], df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred, labels=["Fail","Pass"]))
print("\nClassification Report:")
print(classification_report(y_test, pred))

joblib.dump(model, MODEL_PATH)
print("\nModel saved to:", MODEL_PATH)

new_student = pd.DataFrame([{
    "Study_Hours_Per_Day": 6.5,
    "Attendance_Percent": 88,
    "Assignment_Score": 82,
    "Previous_Exam_Score": 76
}])
print("\nNew Student Prediction:", model.predict(new_student)[0])
print("Class Probabilities:", model.predict_proba(new_student)[0])
