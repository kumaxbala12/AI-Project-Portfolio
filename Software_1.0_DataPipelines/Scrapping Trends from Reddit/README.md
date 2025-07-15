# 📢 Project 03: Scraping Trends from Reddit

This intermediate-level project scrapes top trending posts from any subreddit and saves structured insights for further analysis.

---

## 💡 Project Description

We use Reddit’s JSON endpoints to extract the top daily posts from a given subreddit. We then parse and save post titles, scores, and comment counts using `requests` and `pandas`.

---

## 📦 Features

- Scrapes Reddit top posts from any public subreddit (default: r/technology)
- Collects:
  - Post title
  - Upvotes (score)
  - Number of comments
  - Direct post URL
- Saves data to a CSV file
- Easy to modify or schedule with cron for daily scraping

---

## 🛠️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python scrape_reddit.py
```

3. Optional: Change the `subreddit` variable in the script to target different communities.

---

## 📚 Libraries Used

- `requests`
- `pandas`

---

## ✅ Status

📦 Functional CLI-based Reddit scraper — can be expanded into a dashboard or time-series pipeline.
