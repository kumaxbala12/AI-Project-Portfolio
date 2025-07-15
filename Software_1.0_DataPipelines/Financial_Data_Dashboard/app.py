import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import streamlit as st

st.title("📊 Financial Data Dashboard")

ticker = st.text_input("Enter stock ticker (e.g. AAPL)", "AAPL")
start_date = st.date_input("Start date", pd.to_datetime("2022-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2023-01-01"))

if ticker:
    data = yf.download(ticker, start=start_date, end=end_date)

    if not data.empty:
        st.subheader(f"{ticker} Closing Price")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data["Close"], name="Close"))
        fig.update_layout(xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig)

        st.subheader("Moving Averages")
        data['MA10'] = data['Close'].rolling(10).mean()
        data['MA30'] = data['Close'].rolling(30).mean()
        st.line_chart(data[['Close', 'MA10', 'MA30']])
    else:
        st.warning("No data found. Try a different ticker or date range.")
