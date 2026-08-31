def compare_premiums(current_premium: float | None, new_premium: float | None) -> dict:
    if current_premium is None or new_premium is None:
        return {
            "status": "insufficient_data",
            "difference": None,
            "summary": "I? could not find premium in one or both documents yet."
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

