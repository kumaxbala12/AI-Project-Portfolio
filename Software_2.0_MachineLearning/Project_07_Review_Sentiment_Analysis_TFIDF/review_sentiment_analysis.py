"""
Review Sentiment Analysis

This script loads a dataset of text reviews, performs text preprocessing,
and trains a Logistic Regression model to classify sentiment.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def load_data():
    url = "https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv"
    df = pd.read_csv(url)
    df = df[['label', 'tweet']]
    return df

def preprocess_and_train(df):
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X = tfidf.fit_transform(df['tweet'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

def main():
    df = load_data()
    preprocess_and_train(df)

if __name__ == "__main__":
    main()
