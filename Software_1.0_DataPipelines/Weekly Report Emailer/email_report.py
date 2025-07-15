import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# URL to scrape job listings from
URL = "https://ai-jobs.net/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []
for job in soup.select("div.job"):
    title = job.select_one("h2").text.strip()
    company = job.select_one("h3").text.strip()
    link = "https://ai-jobs.net" + job.select_one("a")["href"]
    jobs.append({"Title": title, "Company": company, "Link": link})

df = pd.DataFrame(jobs)
df.to_csv("weekly_jobs.csv", index=False)

# Email credentials
sender_email = "youremail@gmail.com"
receiver_email = "recipient@example.com"
password = "your-app-password"

# Email body
message = MIMEMultipart("alternative")
message["Subject"] = "Weekly AI Job Report"
message["From"] = sender_email
message["To"] = receiver_email

html = "<h2>Weekly AI Jobs</h2><ul>"
for _, row in df.iterrows():
    html += f"<li><a href='{row['Link']}'>{row['Title']} - {row['Company']}</a></li>"
html += "</ul>"

part = MIMEText(html, "html")
message.attach(part)

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent! Summary saved to weekly_jobs.csv")
