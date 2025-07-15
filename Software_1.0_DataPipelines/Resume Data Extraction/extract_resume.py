import fitz  # PyMuPDF
import re
import os
import pandas as pd

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_fields(text):
    name_match = re.search(r"Name[:\s]+(.+)", text, re.IGNORECASE)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone_match = re.search(r"(\+?\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", text)

    return {
        "Name": name_match.group(1).strip() if name_match else "Not found",
        "Email": email_match.group(0) if email_match else "Not found",
        "Phone": phone_match.group(0) if phone_match else "Not found"
    }

if __name__ == "__main__":
    resume_dir = "resumes"
    results = []

    for filename in os.listdir(resume_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(resume_dir, filename)
            text = extract_text_from_pdf(path)
            fields = extract_fields(text)
            fields["Filename"] = filename
            results.append(fields)

    df = pd.DataFrame(results)
    df.to_csv("extracted_resume_data.csv", index=False)
    print("Extraction complete. Results saved to extracted_resume_data.csv")
