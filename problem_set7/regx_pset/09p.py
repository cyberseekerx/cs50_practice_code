import re


def string_matched(text):
    if re.search(r"^[a-zA-Z]*a*b$", text):
        return "string matched", text
    else:
        return "not matched", text


print(string_matched("hallb"))
print(string_matched("ab"))
print(string_matched("123ab"))
print(string_matched("!@#a!@#b"))
print(string_matched("catb"))
