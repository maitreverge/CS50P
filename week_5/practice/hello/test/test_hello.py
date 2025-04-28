from hello import hello


def test_hello():
    assert hello("David") == "Hello, David !"
    assert hello("Josh") == "Hello, Josh !"

def test_empty():
    assert hello() == "Hello, World !"