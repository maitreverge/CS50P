import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    pattern = r'([\s \.\?!,:]*|[^\w])[U|u]m([\s \.\?!,:]*|[^\w])'
    matches = re.findall(pattern, s)
    print(matches)
    return len(matches)


if __name__ == "__main__":
    main()
