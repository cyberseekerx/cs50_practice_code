# a string that has a followed by zero or more b's
# and not a digit
# TODO: get the sequence of reqx right
import re 

def string_match(string):
    search = r"^a(b)?[a-zA-Z]$"
    if re.search(search, string):
        return "string matched"
    else:
        return "not matched"

print(string_match("ccc"))
print(string_match("aab"))
print(string_match("aac"))
print(string_match("aa"))
print(string_match("aacb"))
print(string_match("acc"))
#print(string_match("a112!@#"))
#print(string_match("a21"))
#print(string_match("ab123"))




