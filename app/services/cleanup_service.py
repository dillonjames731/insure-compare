import re

def normalize_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()
