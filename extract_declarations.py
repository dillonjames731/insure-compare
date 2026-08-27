import sys

import pdfplumber
from text_cleanup import split_camel_case

def extract_and_clean(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        raw_text = page.extract_text()

    cleaned_lnes = [split_camel_case(text) for text in raw_text.split("\n")]
    return "\n".join(cleaned_lnes)

if __name__ == "__main__":
    cleaned_text = extract_and_clean("allstate-auto-declarations-sample.pdf", 1)
    print(cleaned_text)