import re


def string_match(text):
    search = r"^[a-z]+_[a-z]+$"
    if re.search(search, text):
        return "string matched", text
    else:
        return "not matched", text


print(string_match("aba_adf"))
print(string_match("234_123"))
print(string_match("!@#_1!@#"))
print(string_match("!@#1ab_sf!@#!@"))
print(string_match("22SF_123"))
print(string_match("FSDF_DSFSD"))
print(string_match("!#ssf_sf"))
print(string_match("JFaz_qe"))
print(string_match("g_g"))
