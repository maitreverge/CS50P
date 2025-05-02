import re
import sys

TEST = "9:55 AM to 10 PM"


def main():
    # print(convert(input("Hours: ").strip()))
    print(convert(TEST))


def convert(s):
    # pattern = r'([\d]|0[1-9]|1[0-2]):() AM to 5:00 PM'
    pattern = r'^([1-9]|0[1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|0[1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$'
    if matches := re.search(pattern, s):
        print(matches.groups())


if __name__ == "__main__":
    main()
