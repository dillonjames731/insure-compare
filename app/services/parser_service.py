import re


def extract_total_premium(text: str) -> float | None:
    match = re.search(r"total\s+premium\s*:\s*\$?([\d,]+(?:\.\d{2})?)", text, re.IGNORECASE)
    if not match:
        return None

    amount_str = match.group(1).replace(",", "")
    return float(amount_str)

def extract_policy_term_months(text: str) -> int | None:
    match = re.search(r"term\s*:\s*(\d+)\s*month(?:\(s\)|s)?", text, re.IGNORECASE)
    if not match:
        return None
def extract_deductible(text: str, coverage_name: str) -> int | None:
    pattern = rf"{coverage_name}.*?\$([\d,]+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return None
    amount_str = match.group(1).replace(",", "")
    return int(amount_str)

    return int(match.group(1))