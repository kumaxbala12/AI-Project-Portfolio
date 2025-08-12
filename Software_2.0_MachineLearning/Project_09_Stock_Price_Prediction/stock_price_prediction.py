"""
Stock Price Prediction

This script uses historical stock prices from yfinance and predicts the next-day closing price using LSTM.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error

def load_data(ticker='AAPL', period='1y'):
    df = yf.download(ticker, period=period)
    return df[['Close']]

def prepare_data(data):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data)

    X, y = [], []
    for i in range(60, len(scaled)):
        X.append(scaled[i-60:i])
        y.append(scaled[i])
    return np.array(X), np.array(y), scaler

def train_lstm(X_train, y_train):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=3, batch_size=32)
    return model

def main():
    df = load_data()
    X, y, scaler = prepare_data(df.values)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = train_lstm(X, y)

    y_pred = model.predict(X)
    y_pred_inv = scaler.inverse_transform(y_pred)
    y_true_inv = scaler.inverse_transform(y)

    rmse = np.sqrt(mean_squared_error(y_true_inv, y_pred_inv))
    print("RMSE:", rmse)

if __name__ == "__main__":
    main()
