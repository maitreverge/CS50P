import sys
import csv
import os
from tabulate import tabulate

def print_usage(message):
    print(message)
    print("Usage : python3 pizza.py file.csv")
    sys.exit(1)

def parse_args(args):
    if len(sys.argv) != 2:
        print_usage("Incorrect number of arguments")
    
    file = str(args[1])

    if not file.endswith(".csv"):
        print_usage("Incorrect file extension")
    
    # Checks if the file both exists and is readeable
    if not os.access(file, os.R_OK):
        print_usage("File not found")

    return file

def main():
    file = parse_args(sys.argv)

    rows = []

    with open(file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    
    print(tabulate(rows, headers="keys", tablefmt="grid"))




if __name__ == "__main__":
    main()