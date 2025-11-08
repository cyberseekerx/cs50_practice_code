import sys, string


alphabates = tuple(string.ascii_lowercase)

i = 0
next_line_check = False
with open(sys.argv[1],"r") as s:
    for lines in s :

        print(lines)
        if next_line_check == True:
            next_line_check = False

        elif lines.startswith("#"):
            next_line_check = True

        else:
            if lines.lstrip().lower().startswith(alphabates):
                i += 1

print(i)

