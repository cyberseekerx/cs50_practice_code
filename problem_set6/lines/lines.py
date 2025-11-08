import sys 

def main():
    try:
        if len(sys.argv) > 2  :
            sys.exit("too many command-line arguments")
        if not sys.argv[1].endswith('.py') :
            sys.exit("Not a Python file")
        count_lines(sys.argv[1])

    except IndexError:
        sys.exit("Too few command-line  arguments")
def count_lines(f):
    try:
        alphabates = tuple('abcdefghijklmnopqrstuvwxyz"""')
        i = 0
        with open(f,"r") as s:
            for lines in s :
                if not (lines.lstrip().startswith("#") or lines.strip() == ""):
                    i += 1
            print(i)
    except FileNotFoundError:
        sys.exit("File not found")
if __name__ == "__main__":
    main()
