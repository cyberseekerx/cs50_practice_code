import sys
import csv


def main():
    catch_cli_e()
    text_sec_to_first()


def catch_cli_e():
    if len(sys.argv) > 3:
        sys.exit("too many command-line  arguments")
    if len(sys.argv) < 3:
        sys.exit("too few command-line arguments")
    elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")


def text_sec_to_first():
    students = []
    first_file_r = sys.argv[1]
    # second_file_w = sys.argv[2]
    with open(first_file_r, "r") as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            students.append({"name": row["name"], "house": row["house"]})

    for student in sorted(students, key=lambda student: student["name"]):
        s_name = str({student["name"]})
        new, name = s_name.split(",")

        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()
