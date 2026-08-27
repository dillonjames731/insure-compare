import re


def extract_total_premium(text: str) -> float | None:
    match = re.search(r"total\s+premium\s*:\s*\$?([\d,]+(?:\.\d{2})?)", text, re.IGNORECASE)
    if not match:
        return None

    amount_str = match.group(1).replace(",", "")
    return float(amount_str)