import re


def string_matched(text):
    search = r"([A-Z]{1}[a-z]{1})"
    matches = re.findall(search, text)
    if matches:
        return "string matched", text

    else:
        return "not matched", text


print(string_matched("abcs"))
print(string_matched("AbBA"))
print(string_matched("abcs"))
print(string_matched("abcs"))
