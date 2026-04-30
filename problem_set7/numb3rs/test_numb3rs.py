from numb3rs import validate


def test_first_byte():
    assert validate("129.519.345.81") == False


def test_numbers():
    assert validate("192.168.1.1.1") == False
    assert validate("92.123.69.1") == True
    assert validate("01.10.10.10") == False
    assert validate(".*213") == False


def test_lessbytes():
    assert validate("1.2.3") == False
    assert validate("111") == False


def test_alpha():
    assert validate("cat") == False
    assert validate("dog") == False
