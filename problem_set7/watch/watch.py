import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    ex = (
        r"^\<iframe.*src=\"(http|https)://(www.)?youtube\.com/embed/(?P<link>[\w?_=-]+)"
    )
    match = re.search(ex, s)
    if match:
        link = match.group("link")
        return f"https://youtu.be/{link}"
    else:
        return "None"


if __name__ == "__main__":
    main()
