import pytest
from datetime import date, timedelta
import sys
from seasons import DOB

def test_init_with_valid_date():
    
    test_date = date.today() - timedelta(days=365)
    dob = DOB(test_date)
    assert dob._days_since == 365
    assert dob._minutes == 365 * 24 * 60

def test_multiple_years():
    
    test_date = date.today() - timedelta(days=1000)
    dob = DOB(test_date)
    assert dob._days_since == 1000
    assert dob._minutes == 1000 * 24 * 60

def test_zero_days():
    """Test with today's date (zero days)."""
    today = date.today()
    dob = DOB(today)
    assert dob._days_since == 0
    assert dob._minutes == 0
    assert str(dob) == "Zero minutes"

def test_one_day():
    yesterday = date.today() - timedelta(days=1)
    dob = DOB(yesterday)
    assert dob._days_since == 1
    assert dob._minutes == 1440  # 24 * 60
    assert str(dob) == "One thousand, four hundred forty minutes"