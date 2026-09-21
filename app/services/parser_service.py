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
    pattern = rf"{coverage_name}[^\n]{{0,120}}deductible[^\n]{{0,80}}\$([\d,]+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return None

    amount_str = match.group(1).replace(",", "")
    value = int(amount_str)

    if value <= 0:
        return None

    if value > 20000:
        return None

    return value

def extract_policy_term_months(text: str) -> int | None:
    match = re.search(r"term\s*:\s*(\d+)\s*month(?:\(s\)|s)?", text, re.IGNORECASE)
    if not match:
        return None

        return int(match.group(1))

    return int(match.group(1))

def extract_policy_with_keywords(text: str, keywords: list[str]) -> int | None:
    for keyword in keywords:
        value = extract_deductible(text, keyword)
        if value is not None:
            return value
    return None