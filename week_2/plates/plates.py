"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers)
DONE and a minimum of 2 characters.”
“ Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“DONE No periods, spaces, or punctuation marks are allowed.”
"""


def is_valid(input: str) -> bool:
    if not input[:2].isalpha():
        return False

    if len(input) < 2 or len(input) > 6:
        return False

    if not input.isalnum():
        return False

    # Extract the next position of the number
    position = 0
    for c in input:
        if c == "0":
            return False
        elif c.isdigit():
            break
        position += 1

    number_part = input[position:]

    if number_part != "" and not number_part.isdigit():
        return False
    return True


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
