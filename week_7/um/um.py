import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    # ! Notes : \b is the boundary of \w, making the punct check useless
    # pattern = r'[\s\.\?!,:]*\b[U|u]m\b[\s\.\?!,:]*'
    pattern = r"\b[U|u]m\b"
    matches = re.findall(pattern, s)
    # print(matches)
    return len(matches)


if __name__ == "__main__":
    main()
