def main():
    print("Greeting: ", end="")
    user_input = input()

    print(f"${value(user_input)}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
