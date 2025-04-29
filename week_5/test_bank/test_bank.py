from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hElLo") == 0


def test_h():
    assert value("heeeeeey") == 20
    assert value("Heeeeeey") == 20


def test_no_h():
    assert value("BONJOUR") == 100
    assert value("Baguette") == 100


def test_nb_punct():
    assert value("1Hello") == 100
    assert value("1hello") == 100
    assert value(",?hello") == 100


def test_empty():
    assert value("") == 100
