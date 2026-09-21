def compare_terms(current_term: int | None, new_term: int | None) -> dict:
    if current_term is None or new_term is None:
        return {
            "status": "insufficient_data",
            "difference": None,
            "summary": "I could not find policy term in one or both documents yet."
        }

    difference = new_term - current_term

    if difference > 0:
        summary = f"The new quote term is {difference} month(s) longer."
    elif difference < 0:
        summary = f"The new quote term is {abs(difference)} month(s) shorter."
    else:
        summary = "Both policy terms are the same length."

    return {
        "status": "ok",
        "difference": difference,
        "summary": summary,
    }
def compare_premiums(current_premium: float | None, new_premium: float | None) -> dict:
    if current_premium is None or new_premium is None:
        return {
            "status": "insufficient_data",
            "difference": None,
            "summary": "I could not find premium in one or both documents yet."
        }

    difference = round(new_premium - current_premium, 2)

    if difference < 0:
        summary = f"The new quote is ${abs(difference):,.2f} cheaper."
    elif difference > 0:
        summary = f"The new quote is ${difference:,.2f} more expensive."
    else:
        summary = "Both premiums are the same."

    return {
        "status": "ok",
        "difference": difference,
        "summary": summary,
    }
def compare_deductibles(current_value: int | None, new_value: int | None, label: str) -> dict:
    if current_value is None or new_value is None:
        return {
            "status": "insufficient_info",
            "difference": None,
            "summary": f"I could not find {label} deductible in one or both documents yet."
        }
    difference = new_value - current_value

    if difference > 0:
        summary = f"The quote you are comparing has a {label} deductible of ${difference:,.0f} more."
    elif difference < 0:
        summary = f"The quote you are comparing has a {label} deductible of ${abs(difference):,.0f} less."
    else:
        summary = f"Both quotes have the same {label} deductible of ${difference:,.0f}."
        return {
                "status": "ok",
                "difference": difference,
                "summary": summary,
        }