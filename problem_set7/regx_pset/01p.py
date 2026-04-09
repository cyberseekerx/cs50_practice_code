#allowed chracters check 
import re


text = str(input("Input: "))
search = r"[a-zA-Z-0-9]$"
#or search = r"\w\d$"
if re.search(search,text):
    print("valid")
else:
    print("invalid")
#check if the string only contains alphanumaricals

