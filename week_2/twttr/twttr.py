def main():
    user_input = input("Input: ")
    voyels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    for c in user_input:
        if c in voyels:
            continue
        print(c, end="")


if __name__ == "__main__":
    main()
