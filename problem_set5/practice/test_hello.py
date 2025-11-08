import pytest

from hello import hello

def test_defautlt():
    assert hello() == "hello, world"


def test_aurgment():
    assert hello("name") == "hello, name"

