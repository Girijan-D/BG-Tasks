
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix

data = pd.read_csv("movie_data.csv")

print("\nOriginal Dataset:")
print(data)

data = data.fillna(data.mean(numeric_only=True))

data["Result"] = data["Result"].map({"Flop": 0, "Hit": 1})

print("\nPreprocessed Dataset:")
print(data)

X = data[["Budget", "Duration", "Rating", "Promotion"]]
y = data["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("\nTraining Data:", len(X_train))
print("Testing Data:", len(X_test))


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr_model = LogisticRegression()
lr_model.fit(X_train_scaled, y_train)

lr_prediction = lr_model.predict(X_test_scaled)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_prediction = rf_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_prediction)
lr_precision = precision_score(y_test, lr_prediction)

rf_accuracy = accuracy_score(y_test, rf_prediction)
rf_precision = precision_score(y_test, rf_prediction)

print("\n========== MODEL COMPARISON ==========")

print("\nLogistic Regression:")
print("Accuracy:", lr_accuracy)
print("Precision:", lr_precision)
print("Confusion Matrix:")
print(confusion_matrix(y_test, lr_prediction))

print("\nRandom Forest:")
print("Accuracy:", rf_accuracy)
print("Precision:", rf_precision)
print("Confusion Matrix:")
print(confusion_matrix(y_test, rf_prediction))

print("\n========== FINAL RESULT ==========")

if lr_accuracy > rf_accuracy:
    print("Logistic Regression performed better.")
elif rf_accuracy > lr_accuracy:
    print("Random Forest performed better.")
else:
    print("Both models have the same accuracy.")
