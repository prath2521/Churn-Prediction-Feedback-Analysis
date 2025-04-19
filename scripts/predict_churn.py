import joblib
import pandas as pd

# Load model
model = joblib.load('../model/churn_prediction_model.pkl')

# Example input (you'll change this for real predictions)
sample_input = {
    'gender': 'Female',
    'SeniorCitizen': 0,
    'Partner': 'Yes',
    'Dependents': 'No',
    'tenure': 12,
    'PhoneService': 'Yes',
    'MultipleLines': 'No',
    'InternetService': 'Fiber optic',
    'OnlineSecurity': 'No',
    'OnlineBackup': 'Yes',
    'DeviceProtection': 'No',
    'TechSupport': 'No',
    'StreamingTV': 'Yes',
    'StreamingMovies': 'No',
    'Contract': 'Month-to-month',
    'PaperlessBilling': 'Yes',
    'PaymentMethod': 'Electronic check',
    'MonthlyCharges': 70.35,
    'TotalCharges': 845.5
}

# Convert to DataFrame
df = pd.DataFrame([sample_input])

# Get dummy variables (like during training)
df_encoded = pd.get_dummies(df)

# Add missing columns from training time
model_features = model.feature_names_in_
for col in model_features:
    if col not in df_encoded.columns:
        df_encoded[col] = 0  # add missing columns

# Reorder columns to match model
df_encoded = df_encoded[model_features]

# Predict
prediction = model.predict(df_encoded)[0]

print(f"\n🚀 Churn Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
