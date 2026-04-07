#a followed by one or more b's 
import re 

string = input("input: ")

search = r"ab+?"
if re.search(search,string):
    print("valid")
else:
    print("invalid")

