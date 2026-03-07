import re


def main():
    color = input("enter hexadecimal code: ")
    pattern = r"^#[A-Fa-f0-1]{6}$"
    match = re.search(pattern, color)
    if match:
        print(f"Valid. matched with {match.group()}")
    else:
        print("Invalid")


main()
