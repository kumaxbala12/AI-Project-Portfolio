"""
Credit Card Fraud Detection

This script loads the credit card dataset, applies SMOTE to balance classes,
trains a Random Forest model, and evaluates it.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

def load_data():
    url = "https://www.dropbox.com/s/8j5k2dfsmcfa8kx/creditcard.csv?dl=1"
    return pd.read_csv(url)

def train_and_evaluate(df):
    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    scaler = StandardScaler()
    X_train_res = scaler.fit_transform(X_train_res)
    X_test = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_res, y_train_res)
    y_pred = model.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

def main():
    df = load_data()
    train_and_evaluate(df)

if __name__ == "__main__":
    main()
