import sys
import csv
import os


def print_usage(message):
    print(message)
    print("Usage : python3 scourgify.py before.csv after.csv")
    sys.exit(1)


def parse_args(args):
    if len(sys.argv) != 3:
        print_usage("Incorrect number of arguments")

    input_file = str(args[1])
    output_file = str(args[2])

    correct_extension = input_file.endswith(".csv") and output_file.endswith(".csv")

    if not correct_extension:
        print_usage("Incorrect file extension")

    # Checks if the file both exists and is readeable
    if not os.access(input_file, os.R_OK):
        print_usage("File not found")

    return input_file, output_file


def parse_file(file):
    students = []

    with open(file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur_last, cur_first = row["name"].split(",")
            # print(f"FIRST NAME = {cur_first}, LAST NAME = {cur_last}")
            students.append(
                {
                    "first": cur_first.strip(),
                    "last": cur_last.strip(),
                    "house": row["house"].strip(),
                }
            )

    return students


def write_file(students, output_file):
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        # Automatically write fieldnames
        writer.writeheader()
        writer.writerows(students)
        writer.extr


def main():
    input, output = parse_args(sys.argv)

    students = parse_file(input)

    write_file(students, output)


if __name__ == "__main__":
    main()
