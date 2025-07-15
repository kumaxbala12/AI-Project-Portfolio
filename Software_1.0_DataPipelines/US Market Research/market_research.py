import os
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
from dotenv import load_dotenv

# Load API key
load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# Define indicators
indicators = {
    "UNRATE": "Unemployment Rate",
    "CPIAUCSL": "Consumer Price Index (CPI)",
    "FEDFUNDS": "Federal Funds Rate"
}

# Pull and plot
for code, label in indicators.items():
    data = fred.get_series(code)
    df = pd.DataFrame(data)
    df.columns = [label]
    df.plot(title=label, legend=True)
    plt.savefig(f"{code}_{label.replace(' ', '_')}.png")
    df.to_csv(f"{code}_{label.replace(' ', '_')}.csv")
    plt.clf()

print("Charts and CSV files saved.")
