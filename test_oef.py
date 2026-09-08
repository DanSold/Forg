from oef2optimized import check_number

def test_integer():
    assert check_number("10", "length") == 10.0


def test_float():
    assert check_number("10.5", "length") == 10.5


def test_comma():
    assert check_number("10,5", "length") is False


def test_text():
    assert check_number("hello", "length") is False
