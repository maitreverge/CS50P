def main():
    user_input = input("CamelCase: ")

    for c in user_input:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")


if __name__ == "__main__":
    main()
