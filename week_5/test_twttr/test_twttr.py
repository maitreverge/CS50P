from twttr import shorten


def test_no_voyels():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"


def test_voyels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("cAEIOU") == "c"
    assert shorten("aeiouc") == "c"
    assert shorten("AEIOUc") == "c"
    assert shorten("caeiou") == "c"
    assert shorten("AEcIOU") == "c"
    assert shorten("aeciou") == "c"


def test_numbers():
    assert shorten("aeciou1") == "c1"
    assert shorten("aec1iou1") == "c11"
    assert shorten("0AEIOU") == "0"


def test_punct():
    assert shorten("a,$!c") == ",$!c"


def test_empty():
    assert shorten("") == ""
