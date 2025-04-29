import pytest
from fuel import convert, gauge

def test_gauge_full_empty():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_not_full_empty():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"

def test_convert_happy_path():
    assert convert("1/1") == 100
    assert convert("0/1") == 0
    assert convert("50/100") == 50
    assert convert("25/100") == 25

def test_convert_not_slash():
    with pytest.raises(ValueError):
        convert("11")
    with pytest.raises(ValueError):
        convert("22")
    with pytest.raises(ValueError):
        convert("12/1")

def test_convert_not_slash():
    with pytest.raises(ValueError):
        convert("hehehe")
    with pytest.raises(ValueError):
        convert("/1")
    with pytest.raises(ValueError):
        convert("1/")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("12/0")