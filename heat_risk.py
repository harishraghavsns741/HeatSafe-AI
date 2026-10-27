"""Transparent demo screening rules. Not a medical device or official WBGT calculation."""

def assess_heat_risk(temperature_c: float, relative_humidity: float, language: str = "en") -> dict:
    """Return an illustrative risk category from temperature and relative humidity.

    This intentionally simple rule set is for prototype demonstration only. It does
    not calculate WBGT and must not be used as an occupational safety determination.
    """
    if not isinstance(temperature_c, (int, float)) or not isinstance(relative_humidity, (int, float)):
        raise ValueError("Temperature and humidity must be numeric.")
    if not -10 <= temperature_c <= 60:
        raise ValueError("Temperature must be between -10°C and 60°C.")
    if not 0 <= relative_humidity <= 100:
        raise ValueError("Relative humidity must be between 0% and 100%.")

    # Illustrative screening score; thresholds are not an official safety standard.
    score = temperature_c + max(0, relative_humidity - 40) * 0.08
    if score < 30:
        level = "Low"
    elif score < 36:
        level = "Moderate"
    elif score < 42:
        level = "High"
    else:
        level = "Extreme"

    advice_en = {
        "Low": "Stay hydrated and continue monitoring local conditions.",
        "Moderate": "Drink water regularly, take breaks in shade, and monitor symptoms.",
        "High": "Increase shaded rest breaks, reduce strenuous activity where possible, and follow workplace heat-safety procedures.",
        "Extreme": "Avoid or postpone strenuous outdoor work where feasible. Seek a cooler location and follow official heat-health guidance.",
    }
    advice_ta = {
        "Low": "போதுமான தண்ணீர் குடித்து, உள்ளூர் வானிலை நிலையை தொடர்ந்து கவனிக்கவும்.",
        "Moderate": "தொடர்ந்து தண்ணீர் குடிக்கவும்; நிழலில் ஓய்வு எடுக்கவும்; உடல்நல அறிகுறிகளை கவனிக்கவும்.",
        "High": "நிழலில் ஓய்வு இடைவெளிகளை அதிகரித்து, கடினமான பணியைக் குறைக்கவும்; பணியிட வெப்பப் பாதுகாப்பு வழிமுறைகளைப் பின்பற்றவும்.",
        "Extreme": "சாத்தியமானால் கடினமான வெளிப்புறப் பணியைத் தவிர்க்கவும் அல்லது ஒத்திவைக்கவும். குளிர்ச்சியான இடத்திற்குச் சென்று அதிகாரப்பூர்வ வழிகாட்டுதலைப் பின்பற்றவும்.",
    }
    return {
        "level": level,
        "score": round(score, 1),
        "advice": (advice_ta if language == "ta" else advice_en)[level],
        "disclaimer": (
            "Illustrative prototype screening only. This is not WBGT, a medical diagnosis, "
            "or an official occupational safety threshold. Follow local authorities and "
            "workplace heat-safety procedures."
        ),
    }
