import sys
from lines import get_file

def main():
    test_get_file()


def test_get_file():
    assert get_file("foo") ==  "Not a Python file"




main()
