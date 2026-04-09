import re


def string_matche(text):
    pattern = r"^\w*\S"
    matches = re.search(pattern, text)
    if matches:
        return matches.group()
    else:
        return "not matched", text


print(string_matche("the fox crossed the river"))
print(string_matche("blindsfox crossed the river"))
