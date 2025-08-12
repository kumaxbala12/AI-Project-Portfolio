"""
Customer Churn Prediction Model

This script loads the Telco Customer Churn dataset,
preprocesses it, trains a Random Forest model, and evaluates its performance.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def load_data():
    # Replace with your actual dataset path or URL
    url = "https://raw.githubusercontent.com/blastchar/telco-churn/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    return pd.read_csv(url)

def preprocess_data(df):
    df = df.drop(columns=["customerID"])
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)

    # Encode categorical variables
    for col in df.select_dtypes(include=["object"]).columns:
        if col != "Churn":
            df[col] = LabelEncoder().fit_transform(df[col])
    df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
    return df

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def main():
    df = load_data()
    df = preprocess_data(df)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("
Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
