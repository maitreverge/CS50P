import pytest
from working import convert


def test_easy():
    assert convert("9:00 AM to 9:00 PM") == "09:00 to 21:00"
    assert convert("9:33 AM to 9:33 PM") == "09:33 to 21:33"


def test_missing_minutes():
    assert convert("9:33 AM to 9 PM") == "09:33 to 21:00"
    assert convert("9 AM to 9:33 PM") == "09:00 to 21:33"
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"


def test_midday_midnight():
    assert convert("11:59 PM to 12 AM") == "23:59 to 00:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"
    assert convert("12 AM to 12:01 AM") == "00:00 to 00:01"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("11:59 AM to 12 PM") == "11:59 to 12:00"
    assert convert("11:59 AM to 12:00 PM") == "11:59 to 12:00"
    assert convert("12:00 PM to 12:01 PM") == "12:00 to 12:01"
    assert convert("12:59 PM to 01:00 PM") == "12:59 to 13:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_egde_case_mid():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


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
    with pytest.raises(ValueError):
        convert("09:00AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("09:00AM 9:00 PM")
