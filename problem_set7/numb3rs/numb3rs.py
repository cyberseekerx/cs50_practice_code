import re


def main():
    while True:
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    ex = r"(([0-9])|([1-9][0-9])|(([1][0-9][0-9])|[2]([5][0-5]|[0-4][0-9])))"
    matches = re.search(rf"^({ex}\.){{3}}{ex}$", ip)
    if matches:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
