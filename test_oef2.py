from oef2optimized import check_number

def test_integer_oef2():
    assert check_number("10", "length") == 10.0


def test_float_oef2():
    assert check_number("10.5", "length") == 10.5


def test_comma_oef2():
    assert check_number("10,5", "length") is False


def test_text_oef2():
    assert check_number("hello", "length") is False
