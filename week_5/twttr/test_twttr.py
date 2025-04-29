from twttr import shorten

def test_no_voyels():
    assert shorten("wdcfvb") == "wdcfvb"
    assert shorten("WDCFV") == "WDCFV"

def test_voyels():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aeciou") == "c"
    assert shorten("AEIOUc") == "c"
    assert shorten("cAEIOU") == "c"
    assert shorten("AEcIOU") == "c"

def test_empty():
    assert shorten("") == ""