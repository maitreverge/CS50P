def main():
    print(
        "What is the Answer to the Great Question of Life, the Universe and Everything? ",
        end="",
    )
    user_input = input().lower().strip(" ")

    match user_input:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


if __name__ == "__main__":
    main()
