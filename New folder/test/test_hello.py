from hello import greeting

def test_default():
    assert greeting() == "Hello, World"

def test_argument():
    assert greeting("Marvin") == "Hello, Marvin"