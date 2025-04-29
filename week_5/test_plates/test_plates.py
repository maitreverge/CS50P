from plates import is_valid

"""
-   “All vanity plates must start with at least two letters.”
-   “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
-   “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
-   “No periods, spaces, or punctuation marks are allowed.”

"""

def test_happy_path():
    assert is_valid("JHJA4") == True
    assert is_valid("JHJA44") == True

def test_lenght():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("FF") == True
    assert is_valid("FFJJKKK") == False

def test_letters():
    assert is_valid("FFF") == True
    assert is_valid("1FF") == False
    assert is_valid("F1") == False

def test_numbers_middle():
    assert is_valid("FF1111") == True
    assert is_valid("FF0111") == False
    assert is_valid("FF1011") == True
    assert is_valid("FF101G") == False
    assert is_valid("F101K") == False

def test_punct():
    assert is_valid("FF101 ") == False
    assert is_valid("FF101,") == False
    assert is_valid("FF?101") == False
    assert is_valid("F_F101") == False
    assert is_valid(" FF101") == False