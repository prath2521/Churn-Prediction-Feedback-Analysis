import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Step 1: Drop CustomerID
    df = df.drop(['customerID'], axis=1)

    # Step 2: Convert TotalCharges to numeric (some values are blanks)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Step 3: Drop rows with missing TotalCharges
    df = df.dropna()

    # Step 4: Convert Churn Yes/No to 1/0
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

    return df

if __name__ == '__main__':
    # Replace this path with your actual dataset location
    data = load_data('../data/telco_churn.csv')
    cleaned_data = clean_data(data)

    print(cleaned_data.head())  # Show the first few rows
