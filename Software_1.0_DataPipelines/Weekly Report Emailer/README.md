# 📬 Project 04: Weekly Report Emailer

This project automates the process of sending a weekly summary email containing job listings or scraped content using Python.

---

## 💡 Project Description

Using `requests`, `BeautifulSoup`, and `smtplib`, this script scrapes a job board, filters relevant listings, formats them into a clean summary, and sends it via email.

---

## 📦 Features

- Scrapes job listings from AI job boards or custom websites
- Extracts job title, company, and URL
- Sends a summary via email (plain text or HTML)
- Easily customizable for different sources or scheduling

---

## 🛠️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update email configuration inside `email_report.py`:
   - Your email
   - App password (e.g., Gmail App Password)
   - Recipient email

3. Run the script:
```bash
python email_report.py
```

---

## 📚 Libraries Used

- `requests`
- `beautifulsoup4`
- `pandas`
- `smtplib`, `email.mime` (standard Python library)

---

## 🔒 Email Setup Notes

- For Gmail, enable **2FA** and create an **App Password**
- Never hardcode real credentials into public scripts

---

## ✅ Status

📦 Script-based emailer complete — ready for cron or Task Scheduler automation.
