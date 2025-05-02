import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # pattern = r'([\d]|0[1-9]|1[0-2]):() AM to 5:00 PM'
    pattern = r'():() ([AM]|[PM]) to 5:00 ([AM]|[PM])'
    matches = re.search(pattern, s)


if __name__ == "__main__":
    main()
