import csv,sys

def main():
    pizza(catch_errors_cli())


def catch_errors_cli():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        return sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
def pizza(argv):
    try:
        with open(argv,newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        sys.exit("File not found")
