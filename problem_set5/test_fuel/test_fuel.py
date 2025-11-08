from fuel import convert, gauge
import pytest

def main():
   test_convert()


def test_convert():
    assert convert("99/100") == 99

def test_conver_errors():
    with pytest.raises(ValueError):
        convert("cat/dogs")
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == f"{50}%"


if __name__ == "__main__":
    main()
