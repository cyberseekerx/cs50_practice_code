import re

email = input("type you're email? ").strip()

if re.search(r"^\w+@\w+\.com$", email):
    print("valid")
else:
    print("invalid")
