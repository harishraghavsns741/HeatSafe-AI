import pytest
from heat_risk import assess_heat_risk

def test_low_category():
    assert assess_heat_risk(25, 40)["level"] == "Low"

def test_moderate_category():
    assert assess_heat_risk(32, 40)["level"] == "Moderate"

def test_high_category():
    assert assess_heat_risk(38, 40)["level"] == "High"

def test_extreme_category():
    assert assess_heat_risk(43, 40)["level"] == "Extreme"

def test_tamil_guidance():
    result = assess_heat_risk(32, 40, "ta")
    assert "தண்ணீர்" in result["advice"]

def test_invalid_temperature_rejected():
    with pytest.raises(ValueError):
        assess_heat_risk(80, 50)

def test_invalid_humidity_rejected():
    with pytest.raises(ValueError):
        assess_heat_risk(30, 110)

def test_disclaimer_present():
    assert "not WBGT" in assess_heat_risk(30, 50)["disclaimer"]
