import sys
import os.path

def print_usage(message):
    print(message)
    print("Usage : python3 lines.py file.py")
    sys.exit(1)

def parse_args(args):
    if len(sys.argv) != 2:
        print_usage("Incorrect number of arguments")
    
    file = str(args[1])

    if not file.endswith(".py"):
        print_usage("Incorrect file extension")
    
    # Checks if the file both exists and is readeable
    if not os.access(file, os.R_OK):
        print_usage("File not found")

    return file

def main():
    file = parse_args(sys.argv)

    result = 0

    with open(file) as file:
        for row in file:
            if row.isspace():
                continue
            elif row.strip().startswith("#"):
                continue
            else:
                result += 1
    print(result)


if __name__ == "__main__":
    main()