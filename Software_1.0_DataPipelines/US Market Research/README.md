# 📊 Project 05: US Market Research

This project collects and visualizes US economic data — like interest rates, inflation, and job stats — using public APIs and Python data tools.

---

## 💡 Project Description

By leveraging APIs from trusted sources like FRED (Federal Reserve Economic Data), we pull real-time US economic indicators and generate clear charts to support basic economic research and business insights.

---

## 📦 Features

- Pulls economic indicators (e.g., unemployment, inflation, interest rates)
- Uses the `fredapi` to connect with Federal Reserve Bank of St. Louis data
- Visualizes data using `matplotlib`
- Exports results as PNG charts and CSV

---

## 🛠️ How to Run

1. Get a free [FRED API Key](https://fred.stlouisfed.org/)
2. Save your API key in a `.env` file:
```env
FRED_API_KEY=your_api_key_here
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run:
```bash
python market_research.py
```

---

## 📚 Libraries Used

- `fredapi`
- `matplotlib`
- `pandas`
- `dotenv`

---

## ✅ Status

📦 Functional economic trend visualizer — ready to be expanded for reports or dashboards.
