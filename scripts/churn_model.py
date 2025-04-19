import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from data_preprocessing import load_data, clean_data

# Load and clean data
data = load_data('../data/telco_churn.csv')
data = clean_data(data)

# Split features & target
X = data.drop('Churn', axis=1)  # Features
y = data['Churn']               # Target

# Convert categorical columns to dummy variables
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Build model
model = LogisticRegression(max_iter=1000)  # Allow more iterations
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


import joblib

# Save the model
joblib.dump(model, '../model/churn_prediction_model.pkl')

print("✅ Model saved to 'model/churn_prediction_model.pkl'")
