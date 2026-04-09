import re


def string_match(text):
    search = r"ab{2,3}"
    if re.search(search, text):
        return "string matched"
    else:
        return "not matched"


print(string_match("abb"))
print(string_match("cabb"))
print(string_match("234abs"))
print(string_match("sfsf"))
print(string_match("cabbb"))
print(string_match("abbbb"))
