#  string that has an 'a' follwed by exactly 3 b's
import re


def string_match(text):
    search = r"(\w+)?a(b{3})"
    if re.search(search, text):
        return "string matched"
    else:
        return "not matched"


print(string_match("ab"))
print(string_match("abbb"))
print(string_match("ewrabbb"))
print(string_match("absc"))
