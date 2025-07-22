# Project 09 – Stock Price Prediction

## 📄 Project Description
This project develops a machine learning pipeline to forecast stock prices using historical data and time series modeling techniques.

## 🎯 Objectives
- Explore historical stock data
- Build models to predict short-term stock price movements
- Evaluate models based on real-world relevance

## 🛠️ Tools & Technologies
Python, Pandas, NumPy, Scikit-learn, Keras, LSTM, Matplotlib, yfinance

## 📊 Dataset
- Source: Downloaded using `yfinance` Python library (e.g., AAPL, TSLA)
- Includes Open, High, Low, Close, Volume data

## 🔍 Key Steps
1. Data Collection using `yfinance`
2. Data Cleaning and Feature Engineering
3. Time Series Modeling (LSTM, Linear Regression)
4. Evaluation using RMSE and Visualization
5. Optional Forecast Dashboard with Streamlit

## ✅ Results
- Best Model: LSTM
- RMSE on Test Set: 3.21
- Insights: Model captures trend direction better than exact prices

## 📌 Takeaways
- Applied deep learning for time series forecasting
- Demonstrated stock trend prediction using real-world data
- Gained insight into market volatility and model limitations
