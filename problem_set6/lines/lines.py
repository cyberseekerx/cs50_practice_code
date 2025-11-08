import sys 


alphabates = tuple("abcdefghijklmnopqrstuvwxyz")

i = 0
with open(sys.argv[1],"r") as s:
    for lines in s :
        if lines.lstrip().lower().startswith(alphabates):
            i += 1

print(i)
"""hello"""
