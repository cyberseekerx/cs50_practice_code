from bank import value

def main():
    test_()
    test_H_words()
    test_else_words()


def test_():
    assert value("Hello") == 0
    assert value(", Newman") == 0

def test_H_words():
    assert value("Hey") == 20
    assert value("how , you doing?") == 20

def test_else_words():
    assert value("good morning") == 100
    assert value("What's happening?") == 100


if __name__ == "__main__":
    main()
