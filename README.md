# Machine Learning Mini Project #003 — Student Pass/Fail Prediction Using Python

## FutureTech Simulation Academy

GitHub Repository:
https://github.com/santhulak/futuretech-ml-student-pass-fail-prediction

## Project Overview

This beginner-friendly project introduces **binary classification** by predicting whether a student is likely to Pass or Fail using a Decision Tree Classifier.

Projects #001 and #002 introduced regression. Project #003 moves into classification.

## Learning Objectives

- Understand classification and binary classification
- Understand Decision Trees
- Prepare features and targets
- Split data into training and testing sets
- Use stratified sampling
- Train a Decision Tree Classifier
- Evaluate accuracy
- Read a confusion matrix
- Understand precision, recall and F1-score
- Generate class probabilities
- Visualize a decision tree
- Save and reuse a trained model

## Real-World Scenario

A college could use historical academic data to identify students who may need additional academic support.

This educational project uses:
- Study hours per day
- Attendance percentage
- Assignment score
- Previous exam score

Output:
- Pass
- Fail

This repository uses a synthetic dataset for learning. A real student-risk system would require validated institutional data, privacy safeguards, fairness checks and appropriate human oversight.

## Machine Learning Details

Machine Learning Type: Supervised Learning

Problem Type: Binary Classification

Algorithm: Decision Tree Classifier

Target: Result

Classes: Pass, Fail

## Dataset

The dataset contains 160 synthetic student records.

Features:
- Study_Hours_Per_Day
- Attendance_Percent
- Assignment_Score
- Previous_Exam_Score

Target:
- Result

## Why Decision Tree?

A Decision Tree learns a sequence of feature-based decision rules and uses them to assign a class. Scikit-learn's DecisionTreeClassifier supports fitting, class prediction, probability prediction and accuracy scoring.

## Workflow

Dataset → Data Exploration → Feature Selection → Train/Test Split → Decision Tree Training → Prediction → Evaluation → Visualization → Model Saving

## Project Structure

futuretech-ml-student-pass-fail-prediction/
- README.md
- requirements.txt
- .gitignore
- data/student_pass_fail.csv
- src/student_pass_fail_prediction.py
- notebooks/student_pass_fail_prediction.ipynb
- models/student_pass_fail_model.pkl
- outputs/confusion_matrix.png
- outputs/decision_tree.png

## Technology Stack

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib and Jupyter Notebook.

## Installation

pip install -r requirements.txt

## Run the Project

python src/student_pass_fail_prediction.py

The program loads the dataset, trains the model, evaluates it, saves the model and predicts the result for a sample student.

## Model Configuration

DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

The max_depth setting limits tree complexity and makes the example easier to study.

## Evaluation

The project reports:
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-score

A confusion matrix compares actual and predicted classes and can be used to identify true positives, true negatives, false positives and false negatives.

## Current Model Result

Using the included synthetic dataset and fixed 80/20 stratified split:

Accuracy: 0.8125

The result is specific to this educational dataset and should not be interpreted as real-world prediction performance.

## Example Prediction

Sample student:
- Study Hours: 6.5 per day
- Attendance: 88%
- Assignment Score: 82
- Previous Exam Score: 76

The model returns a predicted Pass/Fail class and class probabilities.

## Understanding Overfitting

Decision Trees can become overly complex and memorize training data. Experiment with max_depth values such as 2, 3, 4, 6 and None, then compare training and testing accuracy.

## Practical Exercises

1. Add quiz score and project score.
2. Compare max_depth values.
3. Compare Decision Tree with Logistic Regression.
4. Compare Decision Tree with Random Forest.
5. Build a Streamlit prediction interface.
6. Add ROC-AUC and precision-recall analysis.
7. Create a model comparison table.
8. Investigate class imbalance.

## Common Beginner Mistakes

- Treating classification like regression
- Looking only at accuracy
- Allowing an unrestricted tree to overfit
- Data leakage
- Assuming feature importance proves causation
- Treating synthetic results as real-world evidence

## Portfolio Description

Developed a Python-based student performance classification system using a Decision Tree Classifier to predict Pass/Fail outcomes from study hours, attendance, assignment performance and previous exam scores. Evaluated the model using accuracy, confusion matrix, precision, recall and F1-score, visualized the decision tree and saved the trained model for reuse.

## Interview Questions

1. What is classification?
2. What is binary classification?
3. How is classification different from regression?
4. What is a Decision Tree?
5. What is Gini impurity?
6. What is entropy?
7. What is overfitting?
8. How does max_depth affect a Decision Tree?
9. What is a confusion matrix?
10. What are precision and recall?
11. What is F1-score?
12. Why can accuracy be misleading?
13. What is stratified splitting?
14. What is feature importance?
15. How would you deploy this model?

## Future Enhancements

- Logistic Regression
- Random Forest
- XGBoost
- Hyperparameter tuning
- Cross-validation
- Feature engineering
- ROC-AUC
- SHAP explainability
- Streamlit deployment
- REST API
- Database integration

## GitHub

Complete source code and project files:
https://github.com/santhulak/futuretech-ml-student-pass-fail-prediction

FutureTech Simulation Academy
Don't Just Learn Technology. Simulate the Job.
