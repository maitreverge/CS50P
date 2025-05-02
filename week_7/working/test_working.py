import pytest
from working import convert

def test_easy():
    assert convert("9:00 AM to 9:00 PM") == "9:00 to 21:00"
    assert convert("9:33 AM to 9:33 PM") == "9:33 to 21:33"

def test_missing_minutes():
    assert convert("9:33 AM to 9 PM") == "9:33 to 21:00"
    assert convert("9 AM to 9:33 PM") == "9:00 to 21:33"
    assert convert("9 AM to 9 PM") == "9:00 to 21:00"

def test_overflow_hours():
    with pytest.raises(ValueError):
        convert("12:00 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("21:00 AM to 9:00 PM")

def test_incorect_data():
    with pytest.raises(ValueError):
        convert("09:00 AM to 9:00PM")
        convert("09:00 AM to 9:00PM")
