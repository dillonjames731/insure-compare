import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    pages_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            pages_text.append(text)
    return "\n".join(pages_text).strip()