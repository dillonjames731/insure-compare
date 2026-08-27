import sys

import pdfplumber

with pdfplumber.open("allstate-auto-declarations-sample.pdf") as pdf:
    page = pdf.pages[1]
    text = page.extract_text()
    print(text)