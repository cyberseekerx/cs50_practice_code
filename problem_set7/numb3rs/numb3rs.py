import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ex = r"([0-1]|[0-9])"
    matches = re.search(f"^{ex}\.$", ip)
    if matches:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
