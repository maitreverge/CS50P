import pytest
from numb3rs import validate


def test_empty():
    assert validate("") == False


def test_dots():
    assert validate("....") == False
    assert validate("...") == False
    assert validate("..") == False
    assert validate(".") == False


def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("0.1.0.1") == True
    assert validate("254.33.12.1") == True


def test_overflow_nb():
    assert validate("256.33.12.1") == False
    assert validate("25.256.12.1") == False
    assert validate("25.33.256.1") == False
    assert validate("25.33.256.256") == False
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    


def test_shitty_input():
    assert validate("a.33.25.26") == False
    assert validate("Hello") == False
