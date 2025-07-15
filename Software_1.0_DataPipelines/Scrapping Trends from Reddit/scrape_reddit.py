import requests
import pandas as pd

# Customize your target subreddit
subreddit = "technology"
url = f"https://www.reddit.com/r/{subreddit}/top/.json?t=day&limit=25"

headers = {'User-agent': 'AI Project Portfolio Bot'}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch data: {response.status_code}")
    exit()

data = response.json()
posts = data["data"]["children"]

records = []
for post in posts:
    info = post["data"]
    records.append({
        "Title": info.get("title"),
        "Score": info.get("score"),
        "Comments": info.get("num_comments"),
        "URL": f"https://reddit.com{info.get('permalink')}"
    })

df = pd.DataFrame(records)
df.to_csv("top_reddit_posts.csv", index=False)
print("Scraped top posts and saved to top_reddit_posts.csv")
