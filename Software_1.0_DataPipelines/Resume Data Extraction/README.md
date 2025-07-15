# 📄 Project 02: Resume Data Extraction

This beginner-level project parses key information from resume PDFs using Python, without requiring large language models.

---

## 💡 Project Description

The goal is to extract structured information such as name, email, education, and skills from unstructured PDF resumes using `PyMuPDF` and regular expressions.

---

## 📦 Features

- Extract raw text from PDFs using `PyMuPDF`
- Normalize text formatting (e.g. whitespace, line breaks)
- Apply regex to extract:
  - Name
  - Email address
  - Phone number
  - Education background
  - Skills
- Save results to CSV for multiple resumes

---

## 🛠️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python extract_resume.py
```

3. Place your PDF resumes in a folder called `resumes/` in the same directory.

---

## 📚 Libraries Used

- `PyMuPDF` (`fitz`)
- `re` (regular expressions)
- `pandas`

---

## ✅ Status

📦 Basic version complete and ready to expand with ML or LLMs later.
