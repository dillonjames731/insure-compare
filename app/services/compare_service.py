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