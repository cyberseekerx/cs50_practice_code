from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten('twitter') == 'twttr'
    assert shorten('what is your name') == 'wht s yr nm'
    assert shorten('hello, WORLD') == 'hll, WRLD'
    assert shorten('cs50') == 'cs50'
    assert shorten('MIT 6.042J') == 'MT 6.042J'
    assert shorten('HELLO') == 'HLL'
    assert shorten('TWitter') == 'TWttr'


if __name__ == "__main__":
    main()
