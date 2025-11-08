from plates import is_valid

def main():
    test_two_letters()
    test_allowed_length()


def test_two_letters():
    assert is_valid("Aa") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False

def test_allowed_length():
    assert is_valid("cs") == True
    assert is_valid("sfhsdlfhslk") == False

def test_zero():
    assert is_valid("AA91") == True
    assert is_valid("AA01") == False
    assert is_valid("AA10") == True

def test_number_place():
    assert is_valid("AAA222") == True 
    assert is_valid("AA22A") ==  False
    assert is_valid("AA222") == True

def test_symbols():
    assert is_valid("cs,.3.") == False
    assert is_valid("cs$@$") == False 



if __name__ == "__main__":
    main()

