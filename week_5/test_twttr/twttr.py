def main():
    prompt = input("What's the word? ")
    print(shorten(prompt))


def shorten(word):
    voyels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    new_word = ""

    for c in word:
        if c not in voyels:
            new_word += c

    return new_word


if __name__ == "__main__":
    main()
