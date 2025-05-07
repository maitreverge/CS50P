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

def test_not_str_input():
    with pytest.raises(ValueError):
        jar = Jar("hehe")

def test_str():
    jar = Jar(3)
    assert jar.size == 0
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(2)
    jar.deposit(1)
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(3)
    jar.deposit(3)
    jar.withdraw(1)
    jar.withdraw(1)
    jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(1)



