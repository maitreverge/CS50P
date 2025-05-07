import pytest
from jar import Jar

def test_no_input():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    assert str(jar) == ""

def test_pos_input():
    jar = Jar(1)
    assert jar.size == 0
    assert jar.capacity == 1
    assert str(jar) == ""

def test_neg_input():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_neg_input():
    with pytest.raises(ValueError):
        jar = Jar("hehe")
