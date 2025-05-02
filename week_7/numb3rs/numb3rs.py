import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        numbers = matches.groups()
        # Convert the string list into a int list
        numbers = [int(nb) for nb in numbers]
        for nb in numbers:
            if nb > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
