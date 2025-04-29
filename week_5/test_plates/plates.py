def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(input):
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


if __name__ == "__main__":
    main()
