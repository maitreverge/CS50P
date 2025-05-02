import pytest
from um import count

# def test_():
def test_upper_lower():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 0 # Edge case for orthograph ?

def test_multi_upper_lower():
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("um Um") == 2
    assert count("um Um um Um") == 4
    assert count("Um um") == 2
    assert count("Um um Um um") == 4
    assert count("uM uM") == 0

def test_spaces():
    assert count("um             um") == 2
    assert count("    Um um        ") == 2
    assert count("    Um   um        ") == 2
    assert count(" um um um umNOPE um um ") == 5
    assert count(" um um um umNOPE um um") == 5
    assert count(" um um um NOPEum um um ") == 5
    assert count(" um um um NOPEum um um") == 5

def test_easy():
    assert count("Um, hello, um David") == 2
    assert count(" Um um     um, um ") == 4

def test_punct():
    assert count("um?") == 1
    assert count("um;") == 1
    assert count("um:") == 1
    assert count("um.") == 1
    assert count("um, ") == 1
    assert count("um!") == 1

def test_multi_punct():
    assert count("um?um") == 2
    assert count("um;um") == 2
    assert count("um:um") == 2
    assert count("um.um") == 2
    assert count("um,um") == 2
    assert count("um!um") == 2

    assert count("um? um") == 2
    assert count("um; um") == 2
    assert count("um: um") == 2
    assert count("um. um") == 2
    assert count("um, um") == 2
    assert count("um! um") == 2

    assert count("um ?um") == 2
    assert count("um ;um") == 2
    assert count("um :um") == 2
    assert count("um .um") == 2
    assert count("um ,um") == 2
    assert count("um !um") == 2

    assert count("um ? um") == 2
    assert count("um ; um") == 2
    assert count("um : um") == 2
    assert count("um . um") == 2
    assert count("um , um") == 2
    assert count("um ! um") == 2

def test_false_friend():
    assert count("Where is the album?") == 0
    assert count("Where is the album um?") == 1
    assert count("umu") == 0
    assert count("umumumum") == 0
    assert count("u mu mu mu m") == 0
    assert count("umnope") == 0
