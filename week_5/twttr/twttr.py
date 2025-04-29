def main():
    input_text = input("Input: ")
    print(shorten(input_text))


def shorten(word):
    voyels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    new_word = ""
    for c in word:
        if c not in voyels:
            new_word += c
    return new_word


if __name__ == "__main__":
    main()
