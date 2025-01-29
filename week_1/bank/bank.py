def parse_input(input: str):
    answer = input.strip(" ").lower()

    if answer.startswith("hello"):
        return 0
    elif answer.startswith("h"):
        return 20
    return 100


def main():
    print("Greeting: ", end="")
    user_input = input()

    print(f"${parse_input(user_input)}")


if __name__ == "__main__":
    main()
